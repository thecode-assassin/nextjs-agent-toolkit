#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const args = process.argv.slice(2);
const jsonOnly = args.includes("--json");
const targetArg = args.find((arg) => arg !== "--json") ?? ".";
const root = path.resolve(targetArg);

function readJson(file) {
  try { return JSON.parse(fs.readFileSync(file, "utf8")); } catch { return null; }
}
function exists(...parts) { return fs.existsSync(path.join(root, ...parts)); }
function firstExisting(names) { return names.find((name) => exists(name)) ?? null; }
function packageVersion(pkg, name) {
  return pkg?.dependencies?.[name] ?? pkg?.devDependencies?.[name] ?? null;
}
function readText(file) {
  try { return fs.readFileSync(path.join(root, file), "utf8"); } catch { return null; }
}

const pkg = readJson(path.join(root, "package.json"));
const configFile = firstExisting(["next.config.ts", "next.config.mts", "next.config.js", "next.config.mjs", "next.config.cjs"]);
const configText = configFile ? readText(configFile) : null;
const packageManager = exists("pnpm-lock.yaml") ? "pnpm" : exists("yarn.lock") ? "yarn" : exists("bun.lockb") || exists("bun.lock") ? "bun" : exists("package-lock.json") ? "npm" : null;
const appDirectory = exists("src", "app") ? "src/app" : exists("app") ? "app" : null;
const middlewareConvention = firstExisting(["src/proxy.ts", "proxy.ts", "src/proxy.js", "proxy.js", "src/middleware.ts", "middleware.ts", "src/middleware.js", "middleware.js"]);
const dependencies = {
  authjs: packageVersion(pkg, "next-auth") ?? packageVersion(pkg, "@auth/core"),
  tanstackQuery: packageVersion(pkg, "@tanstack/react-query"),
  tailwind: packageVersion(pkg, "tailwindcss"),
  shadcn: exists("components.json") ? "components.json" : null,
  vitest: packageVersion(pkg, "vitest"),
  playwright: packageVersion(pkg, "@playwright/test"),
};
const dynamicConfig = Boolean(configText && /process\.env|await\s|import\(|require\(/.test(configText));
const literal = (pattern) => {
  if (!configText) return null;
  const match = configText.match(pattern);
  return match ? match[1] : null;
};
const context = {
  projectRoot: root,
  packageManager,
  versions: { next: packageVersion(pkg, "next"), react: packageVersion(pkg, "react"), node: pkg?.engines?.node ?? null },
  appDirectory,
  config: {
    file: configFile,
    dynamic: dynamicConfig,
    cacheComponents: dynamicConfig ? "unknown" : literal(/cacheComponents\s*:\s*(true|false)/),
    output: dynamicConfig ? "unknown" : literal(/output\s*:\s*["']([^"']+)["']/),
  },
  requestInterception: middlewareConvention,
  asyncRequestApisExpected: (() => {
    const value = packageVersion(pkg, "next");
    const match = value?.match(/(\d+)/);
    return match ? Number(match[1]) >= 15 : "unknown";
  })(),
  integrations: dependencies,
  deploymentHints: {
    vercel: exists("vercel.json") || Boolean(pkg?.scripts?.["vercel-build"]),
    docker: exists("Dockerfile") || exists("docker-compose.yml") || exists("compose.yml"),
    staticExport: !dynamicConfig && literal(/output\s*:\s*["'](export)["']/) === "export",
  },
  notes: [
    ...(pkg ? [] : ["package.json could not be read"]),
    ...(configFile && dynamicConfig ? ["configuration is dynamic; flagged values are unknown unless statically evident"] : []),
    ...(!appDirectory ? ["App Router directory not found"] : []),
  ],
};

if (jsonOnly) console.log(JSON.stringify(context, null, 2));
else {
  console.log(`Next.js context: ${root}`);
  console.log(`  version: ${context.versions.next ?? "unknown"}`);
  console.log(`  app: ${appDirectory ?? "not found"}`);
  console.log(`  package manager: ${packageManager ?? "unknown"}`);
  console.log(`  config: ${configFile ?? "none"}${dynamicConfig ? " (dynamic)" : ""}`);
  console.log(`  request interception: ${middlewareConvention ?? "none"}`);
  console.log(`  integrations: ${Object.entries(dependencies).filter(([, value]) => value).map(([key]) => key).join(", ") || "none detected"}`);
}

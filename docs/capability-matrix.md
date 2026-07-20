# Capability matrix

| Area | Skill | Core |
| --- | --- | :---: |
| Project setup and config | `nextjs-project-configuration` | Yes |
| Routing and navigation | `nextjs-routing-and-navigation` | Yes |
| Rendering, reads, cache | `nextjs-rendering-and-data` | Yes |
| Mutations and forms | `nextjs-mutations-and-forms` | Yes |
| HTTP endpoints | `nextjs-route-handlers` | Yes |
| Auth and security boundaries | `nextjs-auth-and-security` | Yes |
| Loading and recovery | `nextjs-loading-errors-and-recovery` | Yes |
| UI and accessibility | `nextjs-ui-and-accessibility` | Yes |
| Metadata and SEO | `nextjs-metadata-and-seo` | Yes |
| Internationalization | `nextjs-i18n-and-localization` | Yes |
| Performance | `nextjs-performance` | Yes |
| Observability | `nextjs-observability` | Yes |
| Provider-neutral deployment | `nextjs-deployment` | Yes |
| Test-layer selection | `nextjs-testing-strategy` | Yes |
| Upgrades and migrations | `nextjs-upgrades` | Yes |
| Pull request review | `nextjs-pr-review` | Yes |
| Auth.js | `nextjs-authjs` | Adapter |
| TanStack Query | `nextjs-tanstack-query` | Adapter |
| Tailwind and shadcn/ui | `nextjs-tailwind-shadcn-ui` | Adapter |
| Vitest | `nextjs-vitest` | Adapter |
| Playwright | `nextjs-playwright` | Adapter |
| Vercel | `nextjs-vercel` | Adapter |
| External HTTP backend | `nextjs-external-backend-transport` | Adapter |
| Spring Boot contracts | `spring-boot-nextjs-contracts` | Adapter |

The core covers the complete framework workflow without requiring an optional UI, auth, data, testing, backend, or hosting library. Adapters add operational detail only when their technology is present or explicitly requested.

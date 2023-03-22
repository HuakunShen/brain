// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/github");
const darkCodeTheme = require("prism-react-renderer/themes/dracula");
const math = require("remark-math");
const katex = require("rehype-katex");
const sectionPrefix = require("./src/remark/section-prefix");
// const mathjax = require("rehype-mathjax");
// const rehypeMathjax = require("rehype-mathjax");

async function createConfig() {
  // ES Modules are imported with `import()` instead of `require()`, and are imported asynchronously
  const rehypeMathjax = (await import("rehype-mathjax")).default;
  return {
    markdown: {
      mermaid: true,
    },
    themes: [
      "@docusaurus/theme-mermaid",
      [
        require.resolve("@easyops-cn/docusaurus-search-local"),
        /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
        ({
          // ... Your options.
          // `hashed` is recommended as long-term-cache of index file is possible.
          hashed: true,
          // For Docs using Chinese, The `language` is recommended to set to:
          // ```
          // language: ["en", "zh"],
          // ```
        }),
      ],
    ],
    title: "Huakun's World",
    tagline: "Welcome to My Site",
    url: "https://huakun.tech",
    baseUrl: "/",
    onBrokenLinks: "warn",
    onBrokenMarkdownLinks: "warn",
    favicon: "img/anonymous-face.jpg",

    // GitHub pages deployment config.
    // If you aren't using GitHub pages, you don't need these.
    organizationName: "HuakunShen", // Usually your GitHub org/user name.
    projectName: "Huakun's Brain", // Usually your repo name.

    // Even if you don't use internalization, you can use this field to set useful
    // metadata like html lang. For example, if your site is Chinese, you may want
    // to replace "en" with "zh-Hans".
    i18n: {
      defaultLocale: "en",
      locales: ["en"],
    },
    presets: [
      [
        "classic",
        /** @type {import('@docusaurus/preset-classic').Options} */
        ({
          googleAnalytics: {
            trackingID: "G-9EFF9NK198",
          },
          gtag: {
            trackingID: "G-9EFF9NK198",
          },
          docs: {
            sidebarPath: require.resolve("./sidebars.js"),
            exclude: ['**/LearnAlgorithm/LeetCode/Crawler/**'],
            // Please change this to your repo.
            // Remove this to remove the "edit this page" links.
            // editUrl:
            //   "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
            remarkPlugins: [math, sectionPrefix],
            rehypePlugins: [katex],
          },
          blog: {
            showReadingTime: true,
            // Please change this to your repo.
            // Remove this to remove the "edit this page" links.
            // editUrl:
            //   "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
            remarkPlugins: [math],
            rehypePlugins: [katex],
          },
          theme: {
            customCss: require.resolve("./src/css/custom.css"),
          },
        }),
      ],
    ],
    plugins: [
      [
        '@docusaurus/plugin-content-docs',
        {
          id: 'projects', // omitted => default instance
          path: 'projects',
          routeBasePath: 'projects',
          sidebarPath: require.resolve('./sidebars.js'),
          // ... other options
        },
      ],
      [
        '@docusaurus/plugin-content-docs',
        {
          id: 'videos', // omitted => default instance
          path: 'videos',
          routeBasePath: 'videos',
          sidebarPath: require.resolve('./sidebars.js'),
          // ... other options
        },
      ],
    ],
    stylesheets: [
      {
        href: "https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css",
        type: "text/css",
        integrity:
          "sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM",
        crossorigin: "anonymous",
      },
    ],
    themeConfig:
      /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
      ({
        // announcementBar: {
        //   id: 'migration',
        //   content:
        //     'This is my new website, migration is not fully completed. Some content may be missing. See <a target="_blank" rel="noopener noreferrer" href="https://huakunshen.com">My Old Website</a> for more info.',
        //   backgroundColor: '#fafbfc',
        //   textColor: '#091E42',
        //   isCloseable: true,
        // },
        colorMode: {
          defaultMode: 'dark',
          disableSwitch: true,
          respectPrefersColorScheme: false,
        },
        mermaid: {
          theme: { light: "neutral", dark: "dark" },
        },
        // announcementBar: {
        //   id: "pre-alpha-warning",
        //   content:
        //     "CrossCopy is still in alpha stage and is planned to be published by January 2023. Documentation is still under development. If you want to use this app, please subscribe to updates.",
        //   isCloseable: true,
        // },
        metadata: [
          {
            name: "keywords",
            content: "Huakun, Notes, Knowledge Base",
          },
        ],
        navbar: {
          title: "Huakun's Brain",
          logo: {
            alt: "My Site Logo",
            src: "img/anonymous-face.jpg",
            style: {borderRadius: '50%'},
          },
          items: [
            {
              type: "doc",
              docId: "intro",
              position: "left",
              label: "Notes",
            },
            {
              docsPluginId: 'projects',
              type: "doc",
              docId: "projects",
              position: "left",
              label: "Projects",
            },
            {
              docsPluginId: 'videos',
              type: "doc",
              docId: "videos",
              position: "left",
              label: "Videos",
            },
            { to: "/blog", label: "Blog", position: "left" },
            {
              href: "https://github.com/HuakunShen/brain",
              label: "GitHub",
              position: "right",
            },
          ],
        },
        footer: {
          style: "dark",
          links: [
            {
              title: "Docs",
              items: [
                {
                  label: "Notes",
                  to: "/docs/intro",
                },
              ],
            },
            {
              title: "Links",
              items: [
                {
                  label: "LinkedIn",
                  href: "https://www.linkedin.com/in/huakun-shen/",
                },
                {
                  label: "YouTube",
                  href: "https://www.youtube.com/channel/UC1gJeFbvRcQXDC_C8nKetdA",
                },
                {
                  label: "GitHub",
                  href: "https://github.com/HuakunShen",
                },
                {
                  label: "Email",
                  href: "mailto:huakun.shen@huakunshen.com",
                },
              ],
            },
            {
              title: "More",
              items: [
                {
                  label: "Blog",
                  to: "/blog",
                },
              ],
            },
          ],
          copyright: `Copyright © ${new Date().getFullYear()} Huakun Shen. Built with Docusaurus.`,
        },
        prism: {
          theme: lightCodeTheme,
          darkTheme: darkCodeTheme,
          additionalLanguages: ['java', 'powershell', 'rust'],
        },
      }),
  };
}

/** @type {import('@docusaurus/types').Config} */
// const config = {
//   title: "Huakun's World",
//   tagline: "Welcome to My Site",
//   url: "https://brain.huakunshen.com",
//   baseUrl: "/",
//   onBrokenLinks: "warn",
//   onBrokenMarkdownLinks: "warn",
//   favicon: "img/favicon.ico",

//   // GitHub pages deployment config.
//   // If you aren't using GitHub pages, you don't need these.
//   organizationName: "HuakunShen", // Usually your GitHub org/user name.
//   projectName: "Huakun's Brain", // Usually your repo name.

//   // Even if you don't use internalization, you can use this field to set useful
//   // metadata like html lang. For example, if your site is Chinese, you may want
//   // to replace "en" with "zh-Hans".
//   i18n: {
//     defaultLocale: "en",
//     locales: ["en"],
//   },
//   presets: [
//     [
//       "classic",
//       /** @type {import('@docusaurus/preset-classic').Options} */
//       ({
//         docs: {
//           sidebarPath: require.resolve("./sidebars.js"),
//           // Please change this to your repo.
//           // Remove this to remove the "edit this page" links.
//           // editUrl:
//           //   "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
//           remarkPlugins: [require("mdx-mermaid"), math, sectionPrefix],
//           rehypePlugins: [katex],
//         },
//         blog: {
//           showReadingTime: true,
//           // Please change this to your repo.
//           // Remove this to remove the "edit this page" links.
//           // editUrl:
//           //   "https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/",
//           remarkPlugins: [require("mdx-mermaid"), math],
//           rehypePlugins: [katex],
//         },
//         theme: {
//           customCss: require.resolve("./src/css/custom.css"),
//         },
//       }),
//     ],
//   ],

//   stylesheets: [
//     {
//       href: "https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css",
//       type: "text/css",
//       integrity:
//         "sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM",
//       crossorigin: "anonymous",
//     },
//   ],
//   themeConfig:
//     /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
//     ({
//       // announcementBar: {
//       //   id: "pre-alpha-warning",
//       //   content:
//       //     "CrossCopy is still in alpha stage and is planned to be published by January 2023. Documentation is still under development. If you want to use this app, please subscribe to updates.",
//       //   isCloseable: true,
//       // },
//       metadata: [
//         {
//           name: "keywords",
//           content: "Huakun, Notes, Knowledge Base",
//         },
//       ],
//       navbar: {
//         title: "Huakun's Brain",
//         logo: {
//           alt: "My Site Logo",
//           src: "img/logo.svg",
//         },
//         items: [
//           {
//             type: "doc",
//             docId: "intro",
//             position: "left",
//             label: "Notes",
//           },
//           { to: "/blog", label: "Blog", position: "left" },
//           {
//             href: "https://github.com/HuakunShen/brain",
//             label: "GitHub",
//             position: "right",
//           },
//         ],
//       },
//       footer: {
//         style: "dark",
//         links: [
//           {
//             title: "Docs",
//             items: [
//               {
//                 label: "Notes",
//                 to: "/docs/intro",
//               },
//             ],
//           },
//           {
//             title: "Links",
//             items: [
//               {
//                 label: "LinkedIn",
//                 href: "https://www.linkedin.com/in/huakun-shen/",
//               },
//               {
//                 label: "YouTube",
//                 href: "https://www.youtube.com/channel/UC1gJeFbvRcQXDC_C8nKetdA",
//               },
//               {
//                 label: "GitHub",
//                 href: "https://github.com/HuakunShen",
//               },
//               {
//                 label: "Email",
//                 href: "mailto:huakun.shen@huakunshen.com",
//               },
//             ],
//           },
//           {
//             title: "More",
//             items: [
//               {
//                 label: "Blog",
//                 to: "/blog",
//               },
//             ],
//           },
//         ],
//         copyright: `Copyright © ${new Date().getFullYear()} Huakun Shen. Built with Docusaurus.`,
//       },
//       prism: {
//         theme: lightCodeTheme,
//         darkTheme: darkCodeTheme,
//       },
//     }),
// };

// module.exports = config;
module.exports = createConfig;

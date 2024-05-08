import { themes as prismThemes } from "prism-react-renderer";
import type { Config } from "@docusaurus/types";
import type * as Preset from "@docusaurus/preset-classic";

import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";

const config: Config = {
  title: "Huakun's World",
  tagline: "Welcome to My Brain",
  favicon: "img/favicon.ico",
  stylesheets: [
    {
      href: "https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css",
      type: "text/css",
      integrity:
        "sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM",
      crossorigin: "anonymous",
    },
  ],
  themes: [
    "@docusaurus/theme-mermaid",
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      {
        // ... Your options.
        // `hashed` is recommended as long-term-cache of index file is possible.
        hashed: true,
        // For Docs using Chinese, The `language` is recommended to set to:
        // ```
        // language: ["en", "zh"],
        // ```
        docsRouteBasePath: ["/notes", "/projects", "/videos"]
      },
    ],
  ],
  markdown: { mermaid: true },
  // Set the production url of your site here
  url: "https://huakun.tech",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "HuakunShen", // Usually your GitHub org/user name.
  projectName: "brain", // Usually your repo name.

  // onBrokenLinks: "throw",
  onBrokenLinks: "warn",
  onBrokenMarkdownLinks: "warn",

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      {
        googleAnalytics: {
          trackingID: "G-9EFF9NK198"
        },
        gtag: {
          trackingID: "G-9EFF9NK198"
        },
        docs: {
          // id: "notes",
          path: "docs/notes",
          routeBasePath: "notes",
          sidebarPath: "./sidebars.ts",
          exclude: ["**/LearnAlgorithm/LeetCode/Crawler/**"],
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: "https://github.com/HuakunShen/brain/edit/main/",
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: "https://github.com/HuakunShen/brain/edit/main/",
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          blogSidebarTitle: "All Posts",
          blogSidebarCount: "ALL",
        },
        theme: {
          customCss: "./src/css/custom.css",
        },
      } satisfies Preset.Options,
    ],
  ],
  plugins: [
    [
      "@docusaurus/plugin-content-docs",
      {
        id: "projects", // omitted => default instance
        path: "docs/projects",
        routeBasePath: "projects",
        sidebarPath: require.resolve("./sidebars.ts"),
        // ... other options
      },
    ],
    [
      "@docusaurus/plugin-content-docs",
      {
        id: "videos", // omitted => default instance
        path: "docs/videos",
        routeBasePath: "videos",
        sidebarPath: require.resolve("./sidebars.ts"),
        // ... other options
      },
    ],
  ],
  themeConfig: {
    // Replace with your project's social card
    image: "img/docusaurus-social-card.jpg",
    colorMode: {
      defaultMode: "dark",
      disableSwitch: true,
      respectPrefersColorScheme: false,
    },
    mermaid: {
      theme: { light: "neutral", dark: "dark" },
    },
    metadata: [{ name: "keywords", content: "Huakun, Notes, Knowledge Base" }],
    navbar: {
      title: "Huakun's Brain",
      logo: {
        alt: "My Site Logo",
        src: "img/anonymous-face.jpg",
        style: { borderRadius: "50%" },
      },
      items: [
        {
          type: "docSidebar",
          sidebarId: "tutorialSidebar",
          position: "left",
          label: "Notes",
        },
        { to: "/blog", label: "Blog", position: "left" },
        { to: "/projects", label: "Projects", position: "left" },
        { to: "/videos", label: "Videos", position: "left" },
        {
          href: "https://github.com/HuakunShen/",
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
              to: "/notes/intro",
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
            {
              label: "My Main Website",
              href: "https://huakunshen.com",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Huakun.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ["java", "powershell", "rust", "yaml", "graphql"],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;

import React from "react";
import clsx from "clsx";
import Link from "@docusaurus/Link";
import useDocusaurusContext from "@docusaurus/useDocusaurusContext";
import Layout from "@theme/Layout";
import HomepageFeatures from "@site/src/components/HomepageFeatures";

import styles from "./index.module.css";

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx("hero hero--primary", styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro"
          >
            The Knowledge Base
          </Link>
        </div>
      </div>
    </header>
  );
}

function Header() {
  return (
    <div style={{ textAlign: "center", height: "98vh" }}>
      <h1
        style={{
          margin: 0,
          position: "absolute",
          top: "30%",
          left: "50%",
          fontSize: "3em",
          translate: "-50%",
        }}
      >
        Welcome To Huakun's World
      </h1>
      <iframe
        v-show="iframeLoaded"
        src="https://git-skyline.huakun.tech/contribution/github/huakunshen/embed?enableZoom=false&autoRotate=false"
        width="100%"
        height="100%"
        frameborder="0"
      ></iframe>
    </div>
  );
}

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="My Knowledge Base <head />"
    >
      {/* <HomepageHeader /> */}
      <Header />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}

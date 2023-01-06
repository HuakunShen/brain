import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";
const YouTubeLogo = require("@site/static/img/youtube-logo.svg").default;
const CrossCopyLogo = require("@site/static/img/CrossCopy-Logo.svg").default;

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<"svg">>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: "CrossCopy",
    Svg: require("@site/static/img/CrossCopy-Logo.svg").default,
    description: (
      <>
        CrossCopy is a Cross-Platform Realtime Clipboard Syncing Service that
        allows user to seamlessly sync clipboard data across all devices, no
        matter which device/platform is used
        <br />
        <a href="https://crosscopy.io">CrossCopy</a>
      </>
    ),
  },
  {
    title: "YouTube",
    Svg: require("@site/static/img/youtube-logo.svg").default,
    description: (
      <>
        My YouTube Channel
        <br />
        <a href="https://www.youtube.com/channel/UC1gJeFbvRcQXDC_C8nKetdA">
          YouTube Channel
        </a>
      </>
    ),
  },
];

function Feature({ title, Svg, description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div style={{ textAlign: "center" }}>
          <h1 style={{ fontSize: "2em" }}>Highlights</h1>
        </div>
        <div className="row">
          {/* {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))} */}
          <div className={clsx("col col--4")}>
            <div className="text--center">
              <CrossCopyLogo className={styles.featureSvg} />
            </div>
            <div className="text--center padding-horiz--md">
              <h3>CrossCopy</h3>
              <p>
                CrossCopy is a Cross-Platform Realtime Clipboard Syncing Service
                that allows user to seamlessly sync clipboard data across all
                devices, no matter which device/platform is used
              </p>
              <br />
              <a href="https://crosscopy.io">CrossCopy</a>
            </div>
          </div>

          <div className={clsx("col col--4")}>
            <div className="text--center">
              <YouTubeLogo className={styles.youtubeLogo} />
            </div>
            <div className="text--center padding-horiz--md">
              <h3>YouTube</h3>
              <p>
                I make YouTube videos about what I learnt, projects I made,
                problems I solved, and tutorials.
              </p>
              <br />
              <a href="https://www.youtube.com/channel/UC1gJeFbvRcQXDC_C8nKetdA">
                YouTube Channel
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

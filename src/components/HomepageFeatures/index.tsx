import clsx from "clsx";
import Heading from "@theme/Heading";
import styles from "./styles.module.css";

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
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

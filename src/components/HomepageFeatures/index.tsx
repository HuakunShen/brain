import clsx from "clsx";
import Heading from "@theme/Heading";
import styles from "./styles.module.css";

type FeatureItem = {
  title: string;
  // Svg?: React.ComponentType<React.ComponentProps<"svg">>;
  image: string;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: "Kunkun",
    image: "/img/kunkun-logo-150x150.png",
    description: (
      <>
        Jarvis is a open-source and cross-platform extensible app launcher.
        An alternative to Alfred and Raycast, Jarvis is designed to be highly customizable and extensible, 
        allowing users to create extension with web tech. Any web app can be integrated into Jarvis as an extension with 
        a few lines of code.
        <br />
        <a href="https://kunkun.sh">Jarvis</a>
      </>
    ),
  },
  // {
  //   title: "CrossCopy",
  //   image: "/img/CrossCopy-Logo.svg",
  //   description: (
  //     <>
  //       CrossCopy is a Cross-Platform Realtime Clipboard Syncing Service that
  //       allows user to seamlessly sync clipboard data across all devices, no
  //       matter which device/platform is used
  //       <br />
  //       <a href="https://crosscopy.io">CrossCopy</a>
  //     </>
  //   ),
  // },
  {
    title: "YouTube",
    image: "/img/youtube-logo.webp",
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

function Feature({ title, image, description }: FeatureItem) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <img src={image} alt="" height={250} />
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

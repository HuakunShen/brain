# SEO: Search Engine Optimization
The goal of SEO is to create a strategy that will increase your rankings position in search engine results and get more traffic.

## Three Pillars of Optimization
1. Technical: Optimize for web crawlers
2. Creation: Content strategy to target specific keywords
3. Popularity: Make search engines believe your site is a trusted source through [backlinks](https://moz.com/learn/seo/backlinks), referenced from other websites.
## Four Main Responsibilities
1. **Crawling:** going through the web and parse contents in all websites.
2. **Indexing:** Store scraped data and index the data for quicker search time.
3. **Rendering:** Some websites may render pages with JavaScript. Search Engine might not render the page to collect data, thus client-side rendering isn't good for SEO.
4. **Ranking:** Query data based on user input. Rank the data returned for bettern user experience.

See [Googlebot](Googlebot.md) for how Goole crawls the web.

## Rendering and Ranking
### URL Structure in Ranking
- **Semantic:** Use semantic URL, i.e. words instead of ids
- **Logical and Consistent Patterns**
- **Keyword focused:** Use keywords in url
- **Not Parameter Based:** Not a good idea to build URLs with parameters, which are not semantic in most cases.

### Metadata
Metadata is the abstract of the website's content.
Attach a title, description and an image.
#### Title
One of the most important SEO elements, use keywords in title.
```html
<title>Website Title</title>
```
#### Description
```html
<meta
  name="description"
  content="Check out iPhone 12 XR Pro and iPhone 12 Pro Max. Visit your local store and for expert advice."
/>
```
#### Open Graph
Can be used to display rich cards when sharing a URL.
This doesn't offer any benefit to search engine rankings.
```html
<meta property="og:title" content="Social Title for Cool Page" />
<meta
  property="og:description"
  content="And a social description for our cool page"
/>
<meta
  property="og:image"
  content="https://example.com/images/cool-page.jpg"
/>
```

#### Structured Data and JSON-LD
Structured data facilitates the understanding of your pages to search engines.


### On Page SEO
Headings (h1, h2) indicate importance in the document and links connect the web together.

### Internal Links
Google started this principle with the invention of the [PageRank Algorithm](https://web.stanford.edu/class/cs54n/handouts/24-GooglePageRankAlgorithm.pdf).

The PageRank algorithm, at a high level, is an algorithm that goes through every link on a database and scores domains based on how many links they receive (quantity) and from which domains (quality).

## Web Performance & Core Web Vitals
[Web Vitals](https://web.dev/vitals/) is an initiative created by Google to provide unified guidance and metrics to measure end-user page experience on the web.
[Core Web Vitals](https://developers.google.com/search/blog/2020/11/timing-for-page-experience) is a subset of Web Vitals, and currently consists of three metrics that measure loading, interactivity, and visual stability.
These metrics are [Largest Contentful Paint (LCP)](https://nextjs.org/learn/seo/web-performance/lcp), [First Input Delay (FID)](https://nextjs.org/learn/seo/web-performance/fid), and [Cumulative Layout Shift (CLS)](https://nextjs.org/learn/seo/web-performance/cls).

**Largest Contentful Paint (LCP)** metric looks at the **loading performance** of your page. LCP measures the time it takes to get the largest element on the page visible within the viewport.

The **First Input Delay (FID)** metric is the perception of an end user’s experience while **interacting** with a web page.

The **Cumulative Layout Shift (CLS)** metric is a measure of your site’s overall layout stability. A site that unexpectedly shifts layout as the page loads can lead to accidental user error and distraction.

### Lighthouse (v6) Weights for Vitals

The three metrics are not necessarily valued equally. In [Lighthouse](https://developers.google.com/web/tools/lighthouse), different weights are assigned to each of the Core Web Vitals:

-   **Largest Contentful Paint**: 25%
-   **Total Blocking Time***: 25%
-   **First Contentful Paint**: 15%
-   **Speed Index**: 15%
-   **Time to Interactive**: 15%
-   **Cumulative Layout Shift**: 5%
*This is similar to [First Input Delay](https://nextjs.org/learn/seo/web-performance/fid).




## Readings
- [SEO Starer Guide](https://developers.google.com/search/docs/beginner/seo-starter-guide)
- [MDN: User-Agents](https://developer.mozilla.org/es/docs/Web/HTTP/Headers/User-Agent)


## Reference
- https://nextjs.org/learn/seo/introduction-to-seo/importance-of-seo
- https://nextjs.org/learn/seo/crawling-and-indexing/metatags
- https://nextjs.org/learn/seo/rendering-and-ranking/metadata
- https://nextjs.org/learn/seo/web-performance
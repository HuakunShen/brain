# SEO
See [SEO](../../Common/SearchEngine/SEO.md) for more general information.
## Status Code
### 200
[`HTTP 200 OK`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)

### 301/308
[`HTTP 301 Moved Permanently`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/301)
**Note:** [Next.js permanent redirects](https://nextjs.org/docs/api-reference/next.config.js/redirects) use 308 by default instead of 301 as it is the newer version and considered the better option.
```jsx
// pages/about.js
export async function getStaticProps(context) {
  return {
    redirect: {
      destination: '/',
      permanent: true // triggers 308
    }
  }
}
```
or
```js
// next.config.js
module.exports = {
  async redirects() {
    return [
      {
        source: '/about',
        destination: '/',
        permanent: true // triggers 308
      }
    ]
  }
}
```
### 302
[`HTTP 302 Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302)
The HyperText Transfer Protocol (HTTP) **`302 Found`** redirect status response code indicates that the resource requested has been temporarily moved to the URL given by the [`Location`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Location) header.

### 404
[`HTTP 404 Not Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
Resource not found.
```jsx
export async function getStaticProps(context) {
  return {
    notFound: true // triggers 404
  }
}
```
#### Custom 404 Page
```jsx
// pages/404.js
export default function Custom404() {
  return <h1>404 - Page Not Found</h1>
}
```

### 410
[`HTTP 410 Gone`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410)
Target resource is no longer available at the origin server and that this condition is likely to be permanent.
Used for content that are removed, e.g. threads deleted by user, blog post removed from site.

### 500
[`HTTP 500 Internal Server Error`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500)
Next.js will automatically return a `500` status code for an unexpected application error. You can [create a custom `500` error page](https://nextjs.org/docs/advanced-features/custom-error-page#500-page) that is statically generated at build time by creating `pages/500.js`.

```jsx
// pages/500.js
export default function Custom500() {
  return <h1>500 - Server-side error occurred</h1>
}
```

### 503
The [`HTTP 503 Service Unavailable`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503) server error response code indicates that the server is not ready to handle the request.
Used when website is down and predicted that it will be down by an extended period of time. This prevents losing rankings on a long-term basis.

## robots.txt
See [robots.txt](../../Common/SearchEngine/robots.md).
`robots.txt` specifies which routes can be crawled and which are not.
In Next.js, add `robots.txt` to `public` folder.
```
// robots.txt
# Block all crawlers for /accounts
User-agent: *
Disallow: /accounts

# Allow all crawlers
User-agent: *
Allow: /
```
File available at `http://<host>:<port>/robots.txt`.

## Sitemaps
Read [Sitemaps](../../Common/SearchEngine/Sitemaps.md).
![[Sitemaps]]
### Add sitemaps to Next.js
#### Manual
For a simple site, add `public/sitemap.xml`
```html
<!-- public/sitemap.xml -->
<xml version="1.0" encoding="UTF-8">
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
 <url>
   <loc>http://www.example.com/foo</loc>
   <lastmod>2021-06-01</lastmod>
 </url>
</urlset>
</xml>
```

#### getServerSideProps
Generate dynamic sitemaps with `getServerSideProps`.
Make file `pages/sitemap.xml.js`.
```js
// pages/sitemap.xml.js
const EXTERNAL_DATA_URL = 'https://jsonplaceholder.typicode.com/posts'

function generateSiteMap(posts) {
  return `<?xml version="1.0" encoding="UTF-8"?>
   <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
     <!--We manually set the two URLs we know already-->
     <url>
       <loc>https://jsonplaceholder.typicode.com</loc>
     </url>
     <url>
       <loc>https://jsonplaceholder.typicode.com/guide</loc>
     </url>
     ${posts
       .map(({ id }) => {
         return `
       <url>
           <loc>${`${EXTERNAL_DATA_URL}/${id}`}</loc>
       </url>
     `
       })
       .join('')}
   </urlset>
 `
}

function SiteMap() {
  // getServerSideProps will do the heavy lifting
}

export async function getServerSideProps({ res }) {
  // We make an API call to gather the URLs for our site
  const request = await fetch(EXTERNAL_DATA_URL)
  const posts = await request.json()

  // We generate the XML sitemap with the posts data
  const sitemap = generateSiteMap(posts)

  res.setHeader('Content-Type', 'text/xml')
  // we send the XML to the browser
  res.write(sitemap)
  res.end()

  return {
    props: {}
  }
}

export default SiteMap
```

## Special Meta Tags for Search Engines
See [Special Meta Tags for Search Engines](../../Common/SearchEngine/MetaTag.md).
![[MetaTag]]


### Sample Code
```jsx
import Head from 'next/head'

function IndexPage() {
  return (
    <div>
      <Head>
        <title>Meta Tag Example</title>
        <meta name="google" content="nositelinkssearchbox" key="sitelinks" />
        <meta name="google" content="notranslate" key="notranslate" />
      </Head>
      <p>Here we show some meta tags off!</p>
    </div>
  )
}

export default IndexPage
```

## Canonical Tag
See [Canonical Tag](../../Common/SearchEngine/CanonicalTag.md).
![[CanonicalTag]]

## Rendering Strategies
> The most important thing for SEO is that page data and metadata is available on page load without JavaScript.

- SSG (Static Site Generation)
- SSR (Server-Side Rendering)
- ISR (Incremental Static Regeneration)
	- When there is a large amount of pages taking too much time to generate at build time. Next.js allows you to create or update static pages after you have built your site. 
	- [Incremental Static Regeneration](https://nextjs.org/docs/basic-features/data-fetching#incremental-static-regeneration) enables developers and content editors to use static generation on a per-page basis, without needing to rebuild the entire site. With ISR, you can retain the benefits of static while scaling to millions of pages
- CSR (Client Side Rendering)

See [Rendering Strategies](https://nextjs.org/learn/seo/rendering-and-ranking/rendering-strategies) and [Nextjs Basics](./Basics.md) for more details.

## AMP
Nextjs supports [AMP](https://nextjs.org/learn/seo/rendering-and-ranking/amp).

## Performance & Core Web Vitals
See [SEO](../../Common/SearchEngine/SEO.md) for details.
### Auto Image Optimization
[Tutorial](https://nextjs.org/learn/seo/improve/images)
#### On-demand Optimization
Instead of optimizing images at build time, Next.js optimizes images on-demand as users request them. Unlike static site generators and static-only solutions, build times don't increase, whether shipping ten images or ten million images.
#### Lazy Loaded Images
Images are lazy loaded by default. Page speed won't be penalized for images housed outside of the viewport. Images only load when they come into view.
#### Avoids CLS
Images are always rendered to avoid Cumulative Layout Shift (CLS).
#### Sample Code
```jsx
import Image from 'next/image'
return <Image src="" alt="" width={1920} height={1080}/>
```

### Dynamic Imports
[Tutorial 1](https://nextjs.org/learn/seo/improve/dynamic-imports)
[Tutorial 2](https://nextjs.org/learn/seo/improve/dynamic-import-components)
Goal: reduce the amount of JavaScript loaded during initial page load from third-party libraries.

```jsx
import dynamic from 'next/dynamic'
import CodeSampleModal from '../components/CodeSampleModal'

// Dynamic Import
const CodeSampleModal = dynamic(() => import('../components/CodeSampleModal'), {
  ssr: false
})
```

### Optimizing Fonts
[Tutorial](https://nextjs.org/learn/seo/improve/fonts)
Next.js has built-in [Automatic Webfont Optimization](https://nextjs.org/docs/basic-features/font-optimization). By default, Next.js will automatically inline font CSS at build time, eliminating an extra round trip to fetch font declarations. This results in improvements to First Contentful Paint (FCP) and Largest Contentful Paint (LCP).

```jsx
// regular version
<link href="https://fonts.googleapis.com/css2?family=Inter" rel="stylesheet" />
// optimized fonts
<style data-href="https://fonts.googleapis.com/css2?family=Inter">
  @font-face{font-family:'Inter';font-style:normal.....
</style>
```

### Optimizing Third-Party Scripts
[Tutorial](https://nextjs.org/learn/seo/improve/third-party-scripts)
Embedding third-party authored code can delay page content from rendering and affect user performance if it is loaded too early.
Next.js provides a built-in [Script component](https://nextjs.org/docs/basic-features/font-optimization) that optimizes loading for any third-party script, while giving developers the option to **decide when to fetch and execute it**.
```jsx
import Head from 'next/head'
import Script from 'next/script'

function IndexPage() {
  return (
    <div>
      <Head>
        <script src="https://www.googletagmanager.com/gtag/js?id=123" />
		<!-- Optimized -->
		<Script
			strategy="afterInteractive"
			src="https://www.googletagmanager.com/gtag/js?id=123"
		/>
      </Head>
    </div>
  )
}

```

## Monitoring your Core Web Vitals
[Link](https://nextjs.org/learn/seo/monitor)

### Next.js Analytics
[Next.js Analytics](https://nextjs.org/analytics) allows you to analyze and measure the performance of pages using Core Web Vitals.

### Custom Reporting
It is also possible to use the built-in relayer Next.js Analytics uses and send the data to your own service or push them to Google Analytics.
Add the following to `pages/_app.js`.
```js
export function reportWebVitals(metric) {
  console.log(metric)
}
```
### Data Studio
https://nextjs.org/learn/seo/monitor/data-studio
Use [Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report) dataset.






## Reference
- https://nextjs.org/learn/seo/crawling-and-indexing/status-codes
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- https://nextjs.org/learn/seo/crawling-and-indexing/metatags
- https://nextjs.org/learn/seo/rendering-and-ranking/rendering-strategies
- https://nextjs.org/learn/seo/rendering-and-ranking/metadata
- https://nextjs.org/learn/seo/web-performance
- https://nextjs.org/learn/seo/improve/images
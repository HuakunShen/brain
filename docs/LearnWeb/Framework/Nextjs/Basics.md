# NEXT.js Basics
## NEXT.js's Basic Features
- Styling
	- `styled-jsx`: define styles within `jsx` files.
	- Built in support for importing `css` and `scss` files directly within JavaScript files.
		- Builtin sass support, `npm i -D sass` before using sass.
		- Regular (non-global) `css` files must be named `*.module.css`. They are 
	- Global Styles: define a `css` file and import it from within `pages/_app.js`.
	- Toggle classnames with `classnames` library
	- Out of the box, `Next.js` compiles CSS using [PostCSS](https://postcss.org/), create a top level file `postcss.config.js` to customize. For example, when using [Tailwind](https://tailwindcss.com/).
- `next/link` can link to another page (within the website) without refreshing the web page.
- `next/image` resize and optimize images.
- `next/head` define head for a page
- `next/script` is an extension of regular `script` tag, with extra functions: `onLoad` callback, strategy (when to load). It can be defined within `<Head>` tag.

## Pre-rendering and Data Fetching
[Data Fetching](https://nextjs.org/docs/basic-features/data-fetching/overview)
- 2 forms of pre-rendering: 
	- Static Generation (with or without data)
		- Pre-rendered and saved, basically serving static files.
		- Use Static Generation whenever possible, pages can be served by CDN, much faster than server-side rendering.
		- Without data: client-side rendering
	- Server-side Rendering
		- Render page on server and send back to client (requires a server running)
		- When content is dynamic (load from database), you may have to use server-side rendering or client-side rendering to keep data displayed always up to date. It's still possible to use Static Generation with a remote CMS.
Pre-rendering is on per-page basis, i.e. choose different modes for different pages
### Static Generation with Data using `getStaticProps` (SSG)
Export an `async` function called `getStaticProps` and return the data fetched as props to UI component.
#### Sample Code
```jsx
export default function Home(props) { ... }

export async function getStaticProps() {
  // Get external data from the file system, API, DB, etc.
  const data = ...

  // The value of the `props` key will be
  //  passed to the `Home` component
  return {
    props: ...
  }
}
```
- `getStaticProps` never runs on client side, so it's ok to write server side code such as database connection.
- `getStaticProps` can only be exported from a page.
### Fetching Data at Request Time (SSR)
Use Server-side rendering instead.
Export an `async` function called `getServerSideProps`, which will be called on server for every request.
#### Sample Code
```jsx
function Page({ data }) {
  // Render data...
}

// This gets called on every request
export async function getServerSideProps() {
  // Fetch data from external API
  const res = await fetch(`https://.../data`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}

export default Page
```
### Client-side Rendering
If you **do not** need to pre-render the data, try client-side rendering. 
Client-side rendering is usually used in private, user-specific pages where SEO is not relevant.
- Statically generate (pre-render) parts of the page that don't rely on external data.
- Fetch external data on client side within the browser using JavaScript, then render the page.

#### SWR
Use SWR in client-side rendering. It handles caching, revalidation, focus tracking, refetching on interval, and more.
```jsx
import useSWR from 'swr'

function Profile() {
  const { data, error } = useSWR('/api/user', fetch)

  if (error) return <div>failed to load</div>
  if (!data) return <div>loading...</div>
  return <div>hello {data.name}!</div>
}
```

## Dynamic Routes
### Statically Generate Pages with Dynamic Routes
Support dynamic routes like `/posts/<id>`, where `id` is a variable, linking to different post pages. 
Route `posts/<id>` can be achieved by creating file `pages/pots/[id].js`.
Add async functions `getStaticPaths` and `getStaticProps`. 
```jsx
export default function Post() {
  return <Layout>...</Layout>
}

export async function getStaticPaths() {
  // Return a list of possible value for id
}

export async function getStaticProps({ params }) {
  // Fetch necessary data for the blog post using params.id
}
```

Notice that the `getStaticProps` function now has a props called `params`. 

The return type of `getStaticPaths` should be
```ts
type Params = {
	params: {
		id: string
	}
}[]

type RetType = {
	paths: Params
	fallback: Boolean
}
```
The attribute in `Params` (`id`) should correspond to the filename `[id].js`.

`getStaticPaths` can also fetch data from external API.

## API Routes
[API Routes] lets you create API endpoints inside a Next.js app. 
Create a function under `pages/api` directory.
```jsx
// req = HTTP incoming message, res = HTTP server response
export default function handler(req, res) {
  res.status(200).json({text: 'hello'})
}
```


## Reference
- https://nextjs.org/learn/basics/create-nextjs-app
- https://nextjs.org/docs/getting-started
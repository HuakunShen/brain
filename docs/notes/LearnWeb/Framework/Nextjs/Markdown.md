# Markdown in NEXT.js
`remark` and `remark-html` packages are used to render html.
After rendering markdown syntax into html, the html can be added to the page using
```jsx
<div dangerouslySetInnerHTML={{ __html: postData.contentHtml }} />
```

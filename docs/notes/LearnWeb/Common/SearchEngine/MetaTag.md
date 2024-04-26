## Special Meta Tags for Search Engines
**Meta robot tags** are directives that search engines will always respect. Adding these robots tags can make the indexation of your website easier.
**Meta robots tags** or[`robots.txt`](https://nextjs.org/learn/seo/crawling-and-indexing/robots-txt) files are **directives** and will always be obeyed. **Canonical tags** are **recommendations** that Google can decide to obey or not.

```html
<meta name="robots" content="noindex,nofollow" />
```
The `robots` tag is very common, by default, it has value `index,follow`, `all` is also valid.
- noindex
	- Not show this page in search results.
	- Omitting `noindex` will nidicate the page can be indexed and shown in search results.
	- Sample Use Cases: Settings, policies, internal search pages.
- nofollow
	- To not follow links on this page.
	- Omitting this will **allow robots to crawl and follow links on this page**. Links found on other pages may enable crawling, so if `link A` appears in pages`X` and `Y`, and `X` has a `nofollow` robots tag, but `Y` doesn't, Google may decide to crawl the link.

You can see a [full list of directives](https://developers.google.com/search/docs/advanced/robots/robots_meta_tag#directives) in the Google official documentation.

### Googlebot Tags
```html
<meta name="googlebot" content="noindex,nofollow" />
```
> Googlebox specific tag.

```html
<meta name="google" content="nositelinkssearchbox" />
```
> When users search for your site, Google Search results sometimes display a search box specific to your site, along with other direct links to your site. This tag tells Google not to show the sitelinks search box.

```html
<meta name="google" content="notranslate" />
```
> Ask google not to provide a translation for the page.


## Reference
- https://nextjs.org/learn/seo/crawling-and-indexing/metatags
# Googlebot
![[googlebot-workflow.png]]
## Overview
1. **Find URLs:** Search for URLs from websites or[XML sitemaps](https://developers.google.com/search/docs/advanced/sitemaps/overview).
2. **Add to Crawl Queue:** Queue task to be executed.
3. HTTP Request: The crawler makes an HTTP request to get the headers and acts according to the returned status code
	-   `200` - it crawls and parses the HTML.
	-   `30X` - it follows the redirects.
	-   `40X` - it will note the error and not load the HTML
	-   `50X` - it may come back later to check if the status code has changed.
4. **Render Queue:** Render queue costs more resources, so your site might not be rendered. 
5. **Ready to be indexed:** If all criteria are met, page will be eligible to be indexed and shown in search results.


## Readings
- [SEO Starer Guide](https://developers.google.com/search/docs/beginner/seo-starter-guide)
- [MDN: User-Agents](https://developer.mozilla.org/es/docs/Web/HTTP/Headers/User-Agent)

## Reference
- https://nextjs.org/learn/seo/introduction-to-seo/webcrawlers



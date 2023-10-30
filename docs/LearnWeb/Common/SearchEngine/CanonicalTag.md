# Canonical Tag
A **canonical** URL is the URL of the page that search engines think is most representative from a set of duplicate pages on your site.

If Google finds several URLs that have the same content, it might decide to demote them in search results because they can be considered duplicated.

This also happens across domains, if you run two different websites and post the same content in each one, search engines can decide to pick one of them to be ranked, or directly demote both.

This is where canonical tags are extremely useful. They let Google know which URLs are the original source of truth and which are duplicated. Lots of duplicated pages across same or different domains can lead to bad rankings or even penalizations.

Both are valid, working URLs, but we use canonical to prevent the detection of duplicate content that we own. If we decided that `https://example.com/products/phone` should be considered for rankings, we would create a canonical tag:

```html
<link rel="canonical" href="https://example.com/products/phone" />
```

## Reference
- https://nextjs.org/learn/seo/crawling-and-indexing/canonical
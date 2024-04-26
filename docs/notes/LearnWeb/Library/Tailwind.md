# Tailwind

[Official Website](https://tailwindcss.com/)

> A utility-first CSS framework packed with classes like `flex`, `pt-4`, `text-center` and `rotate-90` that can be composed to build any design, directly in your markup.

Tailwind is not a component library like [Material UI](https://mui.com/) or [Vuetify](https://vuetifyjs.com/en/). With tailwind, all stylings will need to added in html tags as class names. There are many built-in definitions so developer don't need to spend much time in css files, instead, just add a class to an element.

It can get messy if many class names are added to an element, and there will be duplicate code. There are 2 solutions:

1. Build your own components in React, Vue, Angular, etc.
2. Use `@apply` in css to build a new class

```css
.btn-blue {
  @apply py-2 px-4 bg-blue-500 text-white rounded-lg shadow-md hover:bg-blue-700;
}
```

It sounds similar to Bootstrap. Bootstrap is a high level library, it has prebuild components already, which is similar to the React and Vue component libraries except that bootstrap also uses class names. Tailwind let's you customize and construct your own components with serveral tailwind classes.

## Conditional Styles

Styles can be applied conditionally using class names.
Different styles can be applied based on screen size for responsize designs, element state and color theme.

- `sm:p-2 lg:p-4`
- `hover:shadow`
- `dark:text-white`
  - I don't think this is a good way for large scale though. Adding this to all components is too hard in a large scale application
  - Consider using custom theming

## Performance

Tailwind will purge any unused stylings in production build to minimize bundle size.

# Tips

## Centering

- `flex justify-center`
- `grid justify-center content-center`

# Custom Theming

- Watch [YouTube: Theming Tailwind with CSS Variables](https://youtu.be/MAtaT8BZEAo)

# Readings

- [nuxt/tailwind](https://tailwindcss.nuxtjs.org/)

# Reference

- [YouTube Fireship: Tailwind in 100 Seconds](https://youtu.be/mr15Xzb1Ook?list=TLPQMjkwMzIwMjJ6Tp7Oh4AScg)
- [YouTube: Theming Tailwind with CSS Variables](https://youtu.be/MAtaT8BZEAo)

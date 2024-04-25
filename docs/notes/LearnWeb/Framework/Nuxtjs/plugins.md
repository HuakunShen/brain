# Nuxt Plugins

You can extend Nuxt's functionalities by installing and adding more plugins/libraries or even write your own.



## Tailwind

Original Tailwind doesn't work with nuxt3 so far.

Use the plugin [nuxt/tailwind](https://tailwindcss.nuxtjs.org/) defined for nuxt, if officially supports nuxt3.



## PrimeVue

[PrimeVue](https://www.primefaces.org/) is a component library for vue 3. 

See [primevue-quickstart-nuxt3](https://github.com/primefaces/primevue-quickstart-nuxt3) for a sample project.

1. Install the lastest primevue packages first
2. Update the `nuxt.config.js`
3. Add a `plugins/primvue.js` file to import any used components



## Pinia

As Vuex integration is not yet supported in Nuxt3, [Pinia](https://pinia.vuejs.org/) is an alternative recommended by the [offcial doc](https://v3.nuxtjs.org/migration/configuration#vuex).

See [Nuxt 3 and Pinia](https://dev.to/codybontecou/nuxt-3-and-pinia-473k) for a tutorial.

Note:

1. `buildModules` is deprecated in nuxt 3. `modules` should be used instead
2. In the tutorial, `filtersStore.filtersList` returns `undefined`, use `filtersStore.$state.filtersList` instead
   1. This is because getter and state are using the same variable name, if the getter's function name is `filtersListGetter`, then it's possible to be retrieved using `filtersStore.filtersListGetter`
3. `storeToRefs` is a convenient function which turns a store variable into a ref
   1. `const { filtersList } = storeToRefs(store);`
   2. `filtersList` can be used directly in `template`






---
date: 2022-5-16
---

# Build a Chrome Extension with Vue/Vite

At the time of writing this note, official Vue has switched to Vite, which is a much faster alternative of original Vue CLI.

See [Vite Note](../../Framework/vite/README.md) for more details.

See [Sample Code](#sample-code)

## Vite

Let's suppose you want to build 2 diffrent pages, one for popup and one for options.

### Procedures

1. `npm init vue@latest`
   1. Select the components you need
2. `npm install`
3. Copy `index.html` and name the new file `popup.html`, rename `./src/main.ts` to `popup.ts`.
   1. Within `popup.html`, replace the `src` of  `<script type="module" src="/src/main.ts"></script>` with `/src/popup.ts`
4. Make a copy of `popup.html` and `./src/popup.ts`, call them `options.html` and `./src/options.ts`
   1. Within `options.html`, replace the `src` with `./src/options.ts`
5. Rename `./src/App.vue` to `./src/Popup.vue`. Make a copy of it and name it `./src/Options.vue`
   1. `./src/options.ts` and `./src/popup.ts` will be the entrypoint when building the 2 pages
   2. `./src/Popup.vue` and `./src/Options.vue` will be the 2 pages themselves
6. In `vite.config.ts`, add the following to `defineConfig`

```js
import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import { resolve } from 'path'

const root = resolve(__dirname, 'src');
const outDir = resolve(__dirname, 'dist');
const publicDir = resolve(__dirname, 'public')
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  publicDir,
  root,
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    outDir,
    emptyOutDir: true,
    rollupOptions: {
      input: {
        popup: resolve(root, 'index.html'),
        options: resolve(root, 'pages/options/index.html')
      }
    }
  }
})
```

7. Now, if you run `npm run build`, the dist folder will contain `options.html` and `popup.html`
8. Note that the `index.html` is not deleted. It's used for development server.
   1. Toggle the `src` attribute between `/src/popup.ts` and `/src/options.ts` to decide which page you want to develop.
   2. Another option is to use a config file to specify which entrypoint html file to use.

## Sample Code

See [chrome-ext-vue3-ts](https://github.com/HuakunShen/chrome-ext-vue3-ts) for sample code.

Check different branches. Both original Vue and Vite examples are supplied.


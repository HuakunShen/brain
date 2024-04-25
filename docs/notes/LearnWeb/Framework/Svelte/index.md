---
title: Svelte
---

We will talk about Svelte and SvelteKit together.

- [Svelte: https://svelte.dev/](https://svelte.dev/)
- [SvelteKit: https://kit.svelte.dev/](https://kit.svelte.dev/)

SvelteKit is the meta framework for Svelte. It's like Nuxt.js to Vue, or Next.js to React.

I personally always use SvelteKit instead of Svelte in any circumstances I've seen as SvelteKit offers much more functionalities.

On [State of JS 2022](https://2022.stateofjs.com/en-US/libraries/), Svelte is rated as **S** tier.

Personally, I have a better experience with Svelte than React and Vue. If you tried Svelte, it's hard to go back.

It has many advantages over React and Vue, like speed and syntactic sugar. Since it doesn't use Virual DOM but a JS compiler, everything is pure JS, it can reach higher speed and flexible syntax.

It's actually a little similar to Vue wrt. coding experience. Vue is great and I love it, much better than React, but I just find Svelte more friendly to use. Svelte has less restrictions, simpler syntax, etc.

The only limitation I've experienced is the size of its ecosystem. As a very new framework, it has less libraries (UI libraries). For basic websites, Svelte is good enough. But there are many complex/professional libraries like a WYSIWYG editor library only supporting React & Vue, or even just React. Although I don't really like programming with React (especially after its double render `useEffect`), I have to admit that it has the biggest library ecosystem support. **So, do some research on the libraries/tools you need before choosing Svelte. **

## UI Library

There are already many UI libraries that support svelte

1. https://daisyui.com/
2. https://sveltematerialui.com/
3. https://flowbite-svelte.com/
4. https://skeleton.dev/
5. etc.

The non-framework-specific libraries like the tailwind libraries can support any framework.

My favorite library so far is https://daisyui.com/, it doesn't have the complex configurations in other libraries. Other libraries could have issues you have to fix when your project is in a monorepo like npm workspace. DaisyUI is more standalone. It also has many themes you can choose from, not limited to just dark and light.

DaisyUI's limitation is that it lacks JS functionality, it's just a CSS library. For example Skeleton's utility components like the toast component (https://www.skeleton.dev/utilities/toasts) is very useful in an application. While DaisyUI only provides an Alert component, without animation. Programmers have to manually implement a toast/snackbar/notification, which is annoying. This is probably because, this kind of functionality requires writing JS code for each framework, while pure tailwindcss only works with any framework out of the box. DaisyUI would be perfect if it can support the major frameworks.

Skeleton is relative new at this point. It doesn't have as much components as other libraries, but looks promising to me. I am using it in my app. Pretty sure it will be better in the future.

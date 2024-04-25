---
title: Parcel
---

# Parcel

https://parceljs.org/

> The zero configuration build tool for the
>
> - web
> - JavaScript
> - CSS
> - HTML
> - TypeScript
> - React
> - images
> - SASS
> - SVG
> - Vue
> - libraries
> - Less
> - CoffeeScript

> Parcel combines a great out-of-the-box development experience with a scalable architecture that can take your project from just getting started to massive production application.


Parcel is ideal for simple tasks like building a TypeScript library. Parcel can achieve some level of "Zero Configuration". 

For example, to build a CJS and a ESM format JS from a TypeScript project, you just need to specify "source", "module", "main" in `package.json` and run `parcel build`.
Parcel will recognize what you need and generate the files for you. 

Unlike webpack where you have to install all the loaders and set up configuration files, parcel is smarter.

However, based on my understanding in Parcel so far, although simple to use, may not be as powerful as webpack. For example, for some very cusomized tasks, webpack may still be the best choice. 

For regular usage such as building a TypeScript library, Parcel is perfect.
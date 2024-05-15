---
title: Reconciliation
---

## What is Reconciliation in React?

Reconciliation is the process of updating the DOM to match the React elements.

React uses a diffing algorithm to determine the changes in the DOM and updates the DOM accordingly.

[Ink](https://github.com/vadimdemedes/ink.git) is a project that can render React component to Terminal

Here is the `render` function https://github.com/vadimdemedes/ink/blob/eb18bdeb0ac4c91ae4a686774bbdedbb96bb7263/src/ink.tsx#L211

## Resource

- [awesome-react-renderer](https://github.com/chentsulin/awesome-react-renderer): A curated list of React Renderer to help you choose the right renderer for your React application.  
  - e.g. [react-blessed](https://github.com/Yomguithereal/react-blessed): Control terminal with React

## Reference

- [Legacy React Reconciliation Documentation](https://legacy.reactjs.org/docs/reconciliation.html)
- [react-reconciler](https://www.npmjs.com/package/react-reconciler)
- [Building a Custom React Renderer | Sophie Alpert](https://youtu.be/CGpMlWVcHok)

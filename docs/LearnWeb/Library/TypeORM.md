# TypeORM

https://typeorm.io/

> TypeORM is an ORM that can run in NodeJS, Browser, Cordova, PhoneGap, Ionic, React Native, NativeScript, Expo, and Electron platforms and can be used with TypeScript and JavaScript (ES5, ES6, ES7, ES8). Its goal is to always support the latest JavaScript features and provide additional features that help you to develop any kind of application that uses databases - from small applications with a few tables to large scale enterprise applications with multiple databases.

The default TypeORM template uses commonjs module. If you change **module** in tsconfig to **esxxxx**.

See [Initialize a new TypeORM project](https://typeorm.io/using-cli#initialize-a-new-typeorm-project).

Generate ESM based project

```bash
typeorm init --name my-project --module esm
```



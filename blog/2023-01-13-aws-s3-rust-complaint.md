---
title: S3 SDK with Rust (Manual Credential Configuration)
authors: [huakun]
tags: [AWS, S3, Rust, Python, JS, Nodejs, Docs]
---

> First of all, I have to say, I am very disappointed with AWS's documentation.
> They do have many documentation and sample code, but I am still unable to find what I was looking for (easily).

## Intro

I was working on a project that requires using Rust to upload files to AWS S3.
I wanted to use Rest API to do this, but could not find enough information from the documentation.
There is no sample code or something like a postman API doc that allows you to generate client code from a Rest API.

For example, in this API doc on PutObject, https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html.

`Authorization:authorization string` doesn't mean anything to me. I have access key and secret, but there must be a way to get this authorization string.
I am pretty sure it exists, and must be somewhere in the docs. I just couldn't find it. Put a link in the documentation isn't hard.
It saves people time from looking through your entire documentation.
The purpose of World Wide Web is to link things together, instead of look for things separately and try to assemble in clients' head.

Then I switched to Rust SDK. They have plenty of documentation and sample code; but I got stuck on one problem for a long time.
Again, authorization. The documentation and sample code always assume you have the same scenario as they do.
They assume you have a `~/.aws/credentials` file with your access key id and secret.
Sample code always loads credentials automatically from default locations or environment variables, which is fine for a server application.
For client-side software, this doesn't hold. I need to explicitly pass credentials to a function to generate a client.
This is possible and documented for both Python and Nodejs version of the doc, but not for Rust.

I had to go over so many documentation and sample code to figure out how to do this naive thing.
Function from another Rust crate (package) has to be used. [aws_types](https://docs.rs/aws-types/latest/aws_types/struct.Credentials.html#method.from_keys).

Basically, there are many different ways to produce credentials and client;
but for someone without prior knowledge about your nasty design, there is no way to know which package I should find what the method needed.
If you decide to put things in different packages, then at least provide an obvious link somewhere to indicate "You have the option to do blah blah, read the docs here".

Reading AWS docs (Rust) is like browse information everywhere and try to assemble in my head.
Without enough prior knowledge, it's not easy to get things done quickly.

## Details

- Find all docs example here https://github.com/awsdocs/aws-doc-sdk-examples
- [A list of S3 Examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rust_dev_preview/s3)
- S3 [Cargo.toml](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/rust_dev_preview/s3/Cargo.toml) tells you the dependency to install
- [This](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/rust_dev_preview/s3/src/bin/client.rs) is the default way to create client, credentials loaded from FS or Env
  - [Another One](https://docs.aws.amazon.com/sdk-for-rust/latest/dg/client.html)
  - [rust: aws_config: How to load credentials and config](https://docs.rs/aws-config/0.52.0/aws_config/fn.from_env.html)
  - These docs don't talk about loading credentials with function parameters (only loading from FS or Env Vars)
- [Rust Credentials Docs](https://github.com/awsdocs/aws-rust-developer-guide-v1/blob/main/doc_source/credentials.md) doesn't talk about dynamic credential loading (with parameters) at all
- [aws_types crate](https://docs.rs/aws-types/latest/aws_types/struct.Credentials.html#method.from_keys) has the way of loading credentials manually
  - Who the fk know where to find this? You can't expect me to know this crate beforehand, put a link somewhere.
  - `hardcoded-credentials` feature needs to be enabled means, enable it in `Cargo.toml`.
    - `aws-types = { version = "0.52.0", features = ["hardcoded-credentials"] }`
    - Just mention `Cargo.toml` please. Features can be enabled with anything, environment variables, parameters, configurations
    - Who knows you are talking about `Cargo.toml` feature
  - [Discussion on How to use hardcoded credentials](https://github.com/awslabs/aws-sdk-rust/discussions/444)

## Comparison

When I google "AWS s3 python client credential loading", the first link gives me what I need: [Passing credentials as parameters
](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#passing-credentials-as-parameters).
Took me 10 seconds to find the answer.

For Nodejs, it took me ~10 minutes. To find docs and examples everywhere. This is how I found the solution eventually.

1. Google "aws s3 create nodejs client with credentials"
2. Found [S3 Client - AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/index.html), the JS package API docs
3. [S3Client class API](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/classes/s3client.html)
4. [Constructor API](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/classes/s3client.html#constructor)
5. [S3ClientConfig Interface API](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/interfaces/s3clientconfig.html)
6. [Properties -> Credentials Type](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/interfaces/s3clientconfig.html#credentials)
7. [AwsCredentialIdentity (Type of credentials property)](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/interfaces/awscredentialidentity.html)
8. Finally found that this is where to pass in `accessKeyId, expiration, secretAccessKey, sessionToken`.

This is no different from browsing source code. It's important developers has the ability to read source code and API docs.
That doesn't mean the docs provider don't need to provide easy access to the most basic functionalities.

At least I could figure out Nodejs solution within 20 minutes. Took me a few hours to figure out the Rust solution.

## Final Words

- Also, why is documentation and examples everywhere? `aws.amazon.com`, `github.com`, and external websites like [S3 Client - AWS SDK for JavaScript v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/globals.html), (different for every language).
- It's OK to have external API docs as each language have their own platforms. Like rust docs for rust crates.
- But you should have a central place for links to everywhere and a easy-to-use search utility.
-  Could you put everything in one place and provide a search utility to search everything?
  - Like what you have in [JS API docs](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-s3/interfaces/s3clientconfig.html#credentials)
  - If your example is on GitHub, it's not that to search through the source code

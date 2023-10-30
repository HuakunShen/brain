---
title: Features Classification

---

## Overview

- Text Classification
- Feature Extraction from text
  - How to pick the right features?
  - Grammatical 'parts-of-speech'
- Classification overview

## Features

Feature is a measurable variable that is distinctive of something we want to model. We often choose features to identify something (i.e. classification).

### Sentiment Analysis

Detect

- Stress or frustration in a conversation
- Interest, confusion or preferences

Useful features for sentiment analyzers include

- Trigrams
- Frist-person pronouns

## Noise

- Artifact inreceived  `signal` that obfuscates the features.
- In tweets, it can be text that affects feature values (e.g. semi-colon that is used as emoji).

## Pre-processing

Preparing data to make feature extraction easier or more valid.

There is no perfect preprocessor. There are many edge cases to deal with, **Being Consistent** is important. **Noise-reduction** removes some information.



## Parts-of-Speech (PoS)

词性

- Noun
- Verb
- Adjective
- Adverb
- Preposition: over, under
- Pronoun: I, We, They
- Determiner: the, both, either
- Conjunction: and, or

### Contentful parts-of-speech

Some PoS convey more meaning, usually nouns, verbs, adj, ajv.

Contentful PoS usually contain more words, e.g. there are more nouns than prepositions

New contentful words are continually added

Archaic (古老的) contentful words go extinct.

### Functional parts-of-speech

Some PoS are "glue" that holds others together, e.g. prepositions, determiners, conjunctions

Funcitonal PoS usually cover a small and fixed number of word types

Their semantics depend on the contentful words with which they're used.

## Grammatical features

- case
- Person
- Number
- Gender

These features can restrict other words in a sentence.

## Tagging

### PoS Tagging

The process of assigning a **part-of-speech** to each word in a sequence.

i.e. Given a sentence, which are nouns, which are verbs, etc.



## Classification

### Types of Classifiers

- **Generative** classifiers model the world.
  - Parameters set to maximize likelihood of training data
  - We can **generate** new observations from these (e.g. HMM)
- **Discriminative** classifiers emphasize **class boundaries**
  - Parameters set to minimize error on training data (e.g. SVM, Decision trees)



## Kernel Trick

Sometimes it's not possible to draw a line to separrate and classify multiple classes.

We can sometimes linearize a non-linear case by moving the data into a higher dimension with a **kernel function**.

![image](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/4/19/94757f0d-9bce-423d-b3e0-43d2ab3e51e1.png)

![image](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/4/19/dcc8ebff-d09c-4ee7-9eda-a0017156c885.png)



## Random Forests

Random forests are **ensemble** classifiers that produce K decision trees and output the mode class of those trees.



## Agreement

Parts-of-speech should match in certain ways. Proper grammar.

e.g. "the dogs eats the gravy" has no number agreement





## Review Questions

1. Why K-fold cross-validation and what to watch out for?
2. Explain underfitting and overfitting with respect to the bias-variance tradeoff
3. What does SVM maximize and minimize?
   1. Maximize margin to separate 2 classes
   2. Minimize classification error
4. What are some tricks that SVM uses?
   1. Kernel tricks for high dimentional and non-linear-separable data
5. 












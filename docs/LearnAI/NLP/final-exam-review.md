---
title: Final Exam Review

---

No aids allowed.

## Hints

- Anything highlighted in yellow in lecture slides are important to know.

- Go through the lectures
  - Work out the examples
- The exam contains everything excepts bonus in assignments and "Aside" in slides.



## Topics

- Corpus-based linguistics
- N-gram, Linguistic features, classification
- Entropy and Information Theory
- NLM and word embedding
- Machine Translation (statistical and nerual)
- Recent breakthroughs - (SOTA) transformer varints
- HMMs
- Automatic speech recognition (ASR)
- Natural Language Understanding (NLU)
- Information Retrieval (IR)
- Interpretability and LLM



## Text Classification



## Bayes' Theorem

$$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$$

From Bayes rule, we can do MLE.

Goal: Maximize the likelihood of the training data using the model.

![image](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/4/19/146a30f8-f8b1-44b2-9d0b-9cb2437823b5.png)

To solve the 0 problem, use smoothing. 

Zipf's law: there are many words that appear only once.

Smoothing: steal frequency from the rich and give to the poor.

Add-$\delta$ smoothing: distribute the frequencies more evenly.



## Evaluation

### Extrinsic Evaluation

Which model gives better performance. Performance can be accuracy.. F1 score, recall precision. 

### Intrinsic Evaluation

Perplexity: a way of meausing language model.

Get perplexity of each model, the lower the better.

Bleu score is for translation.



## Entropy

Measure of randomness. 

e.g. if a language model says each word is equally likely, the entropy is high (1). Highly random.

**Know how to calculate entropy, conditional entropy, joint entropy**

Relations between entropies: $H(X, Y)=H(X)+H(Y)-I(X;Y)$

### Mutual Information

$I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)$



Information Theory: Learn how to do calculations, see tutorials.



## Procedure of a Statistical Test

1. State a hypothesis
   1. Null hypothesis and alternative hypothesis
2. Compute some test statistics (P-value)
3. Compare the statistics to a critical vlaue and report the test results



Null Hypothesis: Nothing has changed



## Types of t-tests

- one-sample t-test
- two-sample t-test
- paired t-test



## HMM

**There will be calculation in long answer.**

Train HMM: modify the parameters of model, to maximize training data.



## Backtrack Dynamic Programming



## Forward-Backward Algorithm

Baum-Welch re-estimation



## BLEU

Know how to calculate BLEU scores.

$$BLEU=BP\times(p_1p_2\cdots p_n)^{1/n}$$



## Beam Search: top-K greedy

Idea: track the K-top choices of partial translations (hypotheses) at each step of decoding



## Nerual Language Models

Old stuff in short long answer questions, new stuff in multiple choice.



## RNN

## LSTM

What's the difference, what are the equations?

## ELMo

ELMo considers the entire sentence before embeddeing each token.



## ASR

Long answer question on this.

### Levenshtein Distance

How to calculate, dynamic programming.



## NLU





## IR

### Similarity Score

Vectorization: tf.idf

tf.idf: traditional method to vectorize the documents

### Evaluating Retrieval Systems

- Precision
- Recall
- F-score
- Precision @ K

roc curve

### Term Frequency



## Interpretable NLP

### Shapley Value

Multiple Choice and Short Answer.




















































---
title: Introduction

---



- Tokens: **instances** of words or punctuation
- Types: **kinds** of words or punctuation

How we count things matters.

# Corpora

- Corpus: A body of language data of a particular sort (not only text)
  - Tweets, news, multilingual transcripts of the UN
  - More is better (10M - 1T words)
- Examples
  - Canadian Hansards
  - Project Gutenberg (e-books)
  - web crawls (Google N-Grams, Common Crawl)



## N-grams

N-grams: token sequences of length N.



## Language Models

Language Model: The statistical model of a language

Language models can score and sort sentences. i.e. given 2 sentences, which one is more likely.

## Frequency Statistics

- **Term Count** of term $w$  in corpus $C$ is the number of tokens of term $w$ in $C$. 

  $$Count(w, C)$$

- **Relative Frequency ($F_C$)** is defined relative to the total number of tokens in the corpus $||C||$

  $$F_C(w)=\frac{Count(w, C)}{||C||}$$

  In theory $\lim_{||C||\rightarrow\infty}F_C(w)=P(w)$ (the "frequentist view")

## Probabilities of Sentences

The probability of a sentence is defined as the product of the conditional probabilities of its N-grams

Trigram: $$P(s)=\prod^t_{i=2}P(w_i|w_{i-2}w_{i-1})$$

Bigram: $$P(s)=\prod^t_{i=2}P(w_i|w_{i-1})$$










































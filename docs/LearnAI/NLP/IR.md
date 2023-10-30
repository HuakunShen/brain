---
title: Information Retrieval

---

> Given a **query**, **search for** the most relevant document among a **knowledge base**.

Search Engines are IR systems.

3 Problems:

1. How to represent the query?
2. How to store a knowledge base?
3. How to search efficiently and accurately?

## Options

1. SQL
2. Max-similarity Search (find the doc that's the most similar to the query)
   - Represent query: text-based document
   - Store: **Vectorized** documents
   - Search: Compute similarity score beween query and each doc, return the one with highest score
     - Similartiy: Cosine Distance
3. Semantic Doc2Vec
   1. Also max-similarity search
   2. Goal: train a document encoder $E$
   3. Compare the similarity between 2 encoded doc

## Vectorization: tf.idf

tf.idf is a traditional method to **vectorize** the documents.

Weighing words in documents

1. Term Freq $tf_{ij}$: num of word $w_i$ in doc $d_j$
   1. Usually dampen by $tf_{dampen}=1+\log(tf)$ if $tf>0$
2. Document Freq $df_i$: num docs word $w_i$ appears
   1. Inverse document frequency: maximize specificity $idf_i=\log(\frac{D}{df_i})$, where $D$ is the total number of docs
      1. This gives full weight to words that occur in 1 doc, zero to words in all docs
3. Collection Freq $cf_i$: total num of $w_i$



## Eval Retrieval Systems

<img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/4/20/154c1511-7034-4942-9d5f-dfbcb62e6ab5.png" width="30%" />

- Precision
  - $\frac{TP}{TP+FP}=\frac{TP}{P}$
  - Among the positives (chosen), how many are relevant/correct/true
  - [Precision and recall - Wikipedia](https://en.wikipedia.org/wiki/Precision_and_recall)
- Recall
  - $\frac{TP}{TP+FN}=\frac{TP}{T}$
  - fraction of the relevant documents that are successfully retrieved
  - Among the True documents in ground truth, what fraction is selected
- F-score
  - Measure of test accracy, calculated from precision and recall
  - $F_1=2\cdot\frac{precision\cdot recall}{precision+recall}$
- Precision @ k
  - performance metric used to evaluate the effectiveness of a recommendation system, search engine or information retrieval system
  - measures the proportion of relevant items among the top k recommended items to a user
  - number of relevant items (good predictions) in top k predictions

There are tradeoffs between these metrics.

## Tradeoffs

TODO
















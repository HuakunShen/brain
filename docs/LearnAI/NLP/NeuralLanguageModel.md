---
title: Neural Language Models
---

### Pros

- can generalize better than MLE LMs to unseen n-grams
- Can use semantic information as in word2vec

### Cons

- Can take relatively long to train
- Number of parameters scale poorly with increasing context



## Solution to Expensive Training

- Replace rare words with `<out-of-vocabulary>` token
- Subsample frequent words

- Hierarchical softmax
- Noise-contrastive estimation
- Negative Sampling

### Hierarchical softmax

Group words into distinct classes e.g. by frequency, $c_1$ is top 5%, $c_2$ is the next 5%



## RNN

RNNs have feedback connections so that it remembers previous states. 

- Challenge: Gradient decays quickly



## LSTM

> Long Short-term Memory

Idea: There is a separate "thread"/cell state/special vector stream that runs through the entire chain and stores the long-term information.

<img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/4/21/59625cf4-340f-49e5-b626-32fcabc0b4d0.png" width="100%" />

In a LSTM cell, there are several gates

- Forget gate layer: compare $h_{t-1}$ and the current input $x_t$ to decide which elements in cell state $C_{t-1}$ to keep and which to turn off.
- Input gate layer: 2 steps
  - one sigmoid layer decides which cell units to update
  - one `tanh` layer creates new candidate values $\tilde{C_t}$
- Update Cell State
- Output and feedback



## Contextual Word Embedding

### ELMo

> Embeddings from Language Models






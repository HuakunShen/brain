---
title: NMT (Neural Machine Translation)
---

> Neural Machine Translation (NMT) is a way to do Machine Translation with a single end-to-end neural network.

- Drop noisy channel
- No (explicit) alignments - end-to-end training
- Outperforms "SMT" by a large margin

## Teacher Forcing

- Remove feed-forward recurrence from the previous output to the hidden units, and replace with ground truth for faster training.
- Only used in training

## Attention

Decoder consider input (encoder hidden states) when making decisions. Attention scores determines which area to focus/attend.

- One decoder hidden state and all encoder hidden states are passed into the attention score funciton

Think of decoder hidden state at time t, $\tilde{h_t}$ as **query**.All encoder hidden states, $h_{1:S}$ as values.

### Advantage

- Performance
- Solves bottleneck
  - Sllows decoder to look at the source sentence directly
- Helps with the long-horizon (vanishing gradient) problem by providing shortcut to distant states

## Transformer

- Replace RNN with attention
- Allow parallel computation

### Q,K,V

Decoder has values, the encoder has keys and queries (memory).

$QK^T$ is a similarity measure between Query and Key.

### Positional Encoding

Add positional info of an input token in the sequence into the input embedding vectors.



## Advantages compared to SMT

- Better **performance**
  - More **fluent**
  - Better use of **context**
  - Better use of **phrase similarities**
- Single neural network to be optimized end-to-end
  - Rather than optimizing multiple components individually
- Less human engineering effort
  - No feature engineering
  - Same method for all language pairs

## Disadantages compared to SMT

Mainly due to the **blackbox**-like nature of neural networks.

- NMT is less interpretable
  - hard to debug
- Difficult to control
  - Can't easily specify rules or guidelines for translation
  - Safety concerns

## Sequence-to-Sequence Model (seq2seq)

![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/f2cfef3e-c8b7-4784-920d-aa3598372cef.png)

Many NLP tasks can be phrased as seq2seq:

- Summarization (long -> short text)
- Dialogue (previous -> next utterance)
- Parsing (input text -> output parse as sequence)
- Code Generation (natural language -> code)

NMT directly calculates $P(y|x)$, the translation model.
$P(y|x)=P(y_1|x)P(y_2|y_1,x)\cdots P(y_T|y_1,\cdots,t_{T-1},x)$
$P(y_T|y_1,\cdots,t_{T-1},x)$ is the probability of next target word, given target words so far and source sentence $x$. It's like a recursion, the next word depends on source and all previously generated words.

### How to Train NMT?

> Get a big parallel corpus (equivalent text in e.g. different languages).

![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/e6284892-d63a-47c0-b90d-0033e9866b58.png)

## Multi-layer RNNs (Stacked RNNs)

- RNNs are already "deep" on one dimension (time, they unroll over many timesteps, takes history into account)
- We can make them "deep" in another dimenssion by **applying multiple RNNs** (multi-layer RNN)
- 2-4 layers is best foir encoder RNN, 4 layers is best for decoder RNN
  - skip connections/dense connections are needed to train deeper RNNs (e.g. 8 layers)
  - Transformer-based models are usually deeper (12-24 layers).
- More complex representations - Lower RNNs compute lower-level features, higher RNNs compute higher-level features. - higher-level feaures could be, overall structure and sementics of sentence - lower-level features could be, basics of words (is it a name? adjective etc.)
  ![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/f8a8846a-e73e-4733-a242-40e255777911.png)

## Greedy Decoding

Greedy Decoding: generate target sentence by taking argmax on each step of the decoder (find the most probable word on each step).
<img src="https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/261c633d-d96b-4317-9ba2-288688ce2100.png" width="50%" />
Greedy decoding has no way to undo decisions. If later word can affect previous word, there is no way to undo.

### Exhaustive Search Decoding

Ideally we want to find a (length T) translation $y$ that maximizes $$P(y|x)=P(y_1|x)P(y_2|y_1,x)\cdots P(y_T|y_1,\cdots,t_{T-1},x)=\prod^T_{t=1}P(y_t||y_1,\cdots,y_{t-1},x)$$

## Beam Search Decoding

> On each step of decoder, keep track of k most probable partial translations (hypotheses)

- $k$ is the beam size (in practice 5-10)
- Not guaranteed to find the optimal solution
- Much more efficient than exhaustive search
  A hypothesis $y_1,\cdots, y_t$ has a score which is its log probability:
  $$score(y_1,\cdots, y_t)=\log P_{LM}(y_1,\cdots,y_t|x)=\sum^t_{i=1}P_{LM}(y_i|y_1,\cdots,y_{i-1}, x)$$
- Scores are all negative because log of probability is always negative, higher score is better (higher probability) due to log's property.
- Search for high-scoring hypotheses, tracking top $k$ on each step

### Decoding Example

In the following example beam size $k=2$.
In each round, only choose the 2 with highest scores to continue. Each of the 2 selected words will expand another 2 words, and keep going. This prevents the tree from growing exponentially.
Each expansion is a partial hypothesis. In the end, trace back to obtain full hypothesis.
![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/7f7b9c6e-b48f-4f79-9597-cbd786c4342d.png)

### Problem

Longer hypotheses have lower scores because it's a product of probabilities.
Solution: Normalize by length. So we have a per-word log probability.
$$\frac{1}{t}\sum^t_{i=1}\log P_{LM}(y_i|y_1,\cdots,y_{i-1},x)$$

## Evaluation (BLEU)

BLEU: Bilingual Evaluation Understudy.
BLEU compares machine-written translation to one or several human-written translation(s), and computes a similarity score based on:

- n-gram precision (usually for 1,2,3,4-grams)
  - Overlap words
- Penalty for too-short system translations
  BLEU is imperfect
- Many valid ways to translate a sentence
- good translation can get poor BLEU score

## Attention

### Seq-to-Seq Bottleneck

All information in a single layer.
![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/af8ba98f-544d-4a02-9bd8-ce6be1541920.png)

> On each step of the decoder, **use direction connection to the encoder** to **focus on a particular part** of the source sequence.

![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/b84d40f9-2d03-4cbf-b829-c2b665df18ba.png)

Use the attention distribution to take a weighted sum of the encoder hidden states.
The attention output mostly contains information from the hidden states that received high attention.

![](https://hacker-storage.s3.us-east-2.amazonaws.com/2023/3/11/6121a90c-f0fe-4b5f-a467-3e6407ec577e.png)

Attention always involves

1. Computing the attention scores $e\in\mathbb{R}^N$
2. Taking the softmax to get attention distribution $\alpha$
   $$\alpha=softmax(e)\in\mathbb{R}^N$$
3. Use attention distribution to take weighted sum of values, to obtain attention output $a$
   $$a=\sum^N_{i=1}\alpha_ih_h\in\mathbb{R}^{d_1}$$

### Attention Variants

> There ar eseveral ways to obtain attention scores $e\in\mathbb{R}^N$ from $h_1,\cdots,h_N\in\mathbb{R}^{d_1}$ and $s\in\mathbb{R}^{d_2}$

Basic dot-product attention: $e_i=s^T h_i \in\mathbb{R}$
Multiplicative attention: $e_i=s^T W h_i\in\mathbb{R}$

- $W\in\mathbb{d_2\times d_1}$ is a weight matrix
- Problem: too many parameters in $W$
  Reduced rank multiplicative attention: $e_i=s^T(U^T V)h_i=(U_s)^T(Vh_i)$
- For low rank matrices $U\in\mathbb{R}^{k\times d_2}, V\in\mathbb{R}^{k\times d_1}, k<<d_1, d_2$
- Additive Attention

## Reference

- [Stanford CS224N - Lecture 7 - Translation, Seq2Seq, Attention](https://youtu.be/wzfWHP6SXxY)

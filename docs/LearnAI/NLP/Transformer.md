## Basics
### Attention

### Self Attention

### Masking
Masking is to prevent models from looking at future words, otherwise it's like cheating and models are not penalized/trained.

## Multi-Headed Attention
**Multi-Headed** means, pay attention to multiple place in the source sentence.
Define multiple attention heads through multiple $Q, K, V$ matrices.

## Tricks

### Layer Normalization
> Layer Normalization is a trick to help models train faster.

Cut down on **uninformative variation in hidden vector** values by normalizing to unit mean and standard deviation **within each layer**

### Scaled Dot Product

### Cross-Attention


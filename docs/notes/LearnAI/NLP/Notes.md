## Sparseness

Problems with N-gram models:

- New words appear
- New bigrams occur more often
- New trigrams occur even more often

## Smoothing

Some N-grams are really rare.

If we have no way to determine the distribution of unseen N-grams, how can we estimate them? (Smoothing)

### Add-1 Smoothing (Laplace discounting)

Add 1 to count of every word

Given vocab size $||V||$ and corpus size $N=||C||$.

MLE: $P(w)=Count(w)/N$

Laplace Estimate: $P_{Lap}(w)=\frac{Count(w)+1}{N+||V||}$

It gives a proper probability distribution, $\sum_w P_{Lap}(w)=1$.

For bigrams, $P_{Lap}(w_t|w_{t-1})=\frac{Count(w_{t-1}w_t)+1}{Count(w_{t-1})+||V||}$

#### Problem

Sometimes ~90% of the probability mass is spread across unseen events.

It only works if we know $\mathcal{V}$ beforehand.

### Add-$\delta$ Smoothing

Add $\delta<1$. 

### Good-Turing












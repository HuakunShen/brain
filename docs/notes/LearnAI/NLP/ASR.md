---
title: Automatic Speech Recognition

---

ASR systems converts speech into text.



Raw speech data are 1-d arrays of shape $T_1=f\times t$

- $f$ is sample rate
- $t$ is time length (in seconds)



Speech features are 2D arrays of shape $(T_2, D)$

- $T_2<<T_1$
- $D$: number of features



## Acoustic Model

Each word w migh have different sounds $X$, $P(X|w)$

ASR system becomes $W=\max_w P(w|X)$, given a speech sample, predict a word.

## Bayes Theorem

$$P(w|X)=\frac{P(X|w)P(w)}{P(X)}$$

- $P(w)$ : prior probability (language model)
- $P(X|w)$ : likelihood (acoustic model)



$$W=\max_w P(w|X)=\max_w\frac{P(X|w)P(w)}{P(X)}=\max_w P(X|w)P(w)$$

The last equation is because $P(X)$ is constant wrt $w$



## WER

WER: Word-Error Rate counts different kinds of errors that can be made by ASR at the word-level:

1. Substitution Error: wrong word
2. Deletion Error: skipped word
3. Insertion Error: extra word

$$WER=100\times\frac{N_{sub}+N_{ins}+N_{del}}{N_{wordsinreference}}$$

$WER$, or $N=N_{sub}+N_{ins}+N_{del}$ can be computed with dynamic programming ($N$ is edit distance or Levenshtein Distance). N is the minimum number of error to edit the hypothesis H into the reference R.





## Review Questions

1. What is listen, attend, spell ASR model
2. How to evaluate ASR system
   1. WER
   2. What are the 3 errors (sub, insrt, delete)
   3. What are the init and induction steps to compute WER using dynamic programming
3. Optional: Do LeetCode Q72 (Edit Distance)






---
title: AdaBoost
---

# Boosting

Train classifiers sequentially, each trying to correct its predecessor by assgining higher weights to training data points that were **previously misclassified**.

AdaBoost uses weak learners (e.g. decision stumps, binary tree with a hight of 2) to build a strong learner. 
Weak learners are weak and can't classify well. But we focus on misclassified data points and assign higher weights to them. This way, the weak learner can learn from the misclassified data points and improve its performance.

# Key Steps

1. At each iteration we re-weight the training data points based on the previous classifier's performance, by assigning larger weights to samples (data points) that were misclassified by the previous classifier.
2. We train a new weak classifier based on the re-weighted training data.
3. Add this weak classifier to the ensemble of weak classifiers. This ensemble is our new classifer.
4. Repeat steps 1-3 until the desired number of weak classifiers is reached.

The weak learner needs to minimize weighted error.

AdaBoost reduces bias by making each classifer focus on previous mistakes.


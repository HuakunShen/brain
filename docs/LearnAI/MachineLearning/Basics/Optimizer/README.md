# Optimizer

An optimizer is used to optimize model parameters. 

## [Algorithems Provided by PyTorch](https://pytorch.org/docs/stable/optim.html#algorithms)

| [`Adadelta`](https://pytorch.org/docs/stable/generated/torch.optim.Adadelta.html#torch.optim.Adadelta) | Implements Adadelta algorithm.                               | Notes             |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ----------------- |
| [`Adagrad`](https://pytorch.org/docs/stable/generated/torch.optim.Adagrad.html#torch.optim.Adagrad) | Implements Adagrad algorithm.                                |                   |
| [`Adam`](https://pytorch.org/docs/stable/generated/torch.optim.Adam.html#torch.optim.Adam) | Implements Adam algorithm.                                   | [Adam](./Adam.md) |
| [`AdamW`](https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html#torch.optim.AdamW) | Implements AdamW algorithm.                                  |                   |
| [`SparseAdam`](https://pytorch.org/docs/stable/generated/torch.optim.SparseAdam.html#torch.optim.SparseAdam) | Implements lazy version of Adam algorithm suitable for sparse tensors. |                   |
| [`Adamax`](https://pytorch.org/docs/stable/generated/torch.optim.Adamax.html#torch.optim.Adamax) | Implements Adamax algorithm (a variant of Adam based on infinity norm). |                   |
| [`ASGD`](https://pytorch.org/docs/stable/generated/torch.optim.ASGD.html#torch.optim.ASGD) | Implements Averaged Stochastic Gradient Descent.             |                   |
| [`LBFGS`](https://pytorch.org/docs/stable/generated/torch.optim.LBFGS.html#torch.optim.LBFGS) | Implements L-BFGS algorithm, heavily inspired by [minFunc](https://www.cs.ubc.ca/~schmidtm/Software/minFunc.html). |                   |
| [`NAdam`](https://pytorch.org/docs/stable/generated/torch.optim.NAdam.html#torch.optim.NAdam) | Implements NAdam algorithm.                                  |                   |
| [`RAdam`](https://pytorch.org/docs/stable/generated/torch.optim.RAdam.html#torch.optim.RAdam) | Implements RAdam algorithm.                                  |                   |
| [`RMSprop`](https://pytorch.org/docs/stable/generated/torch.optim.RMSprop.html#torch.optim.RMSprop) | Implements RMSprop algorithm.                                |                   |
| [`Rprop`](https://pytorch.org/docs/stable/generated/torch.optim.Rprop.html#torch.optim.Rprop) | Implements the resilient backpropagation algorithm.          |                   |
| [`SGD`](https://pytorch.org/docs/stable/generated/torch.optim.SGD.html#torch.optim.SGD) | Implements stochastic gradient descent (optionally with momentum). | [SGD](./SGD.md)   |

[`torch.optim` Base Class](https://pytorch.org/docs/stable/optim.html#base-class) implements an abstract method `step` that updates the parameters. 

## Scheduler

[Docs](https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate)

> `torch.optim.lr_scheduler` provides several methods to adjust the learning rate based on the number of epochs.





# Reference

- [`torch.optim`](https://pytorch.org/docs/stable/optim.html#module-torch.optim)


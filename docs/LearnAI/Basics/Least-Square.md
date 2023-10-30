# Least Square

## Linear Least Squares

$$
prediction=y(x,w)=w_0+w_1x_1+\cdots+w_dx_d=w_0+\Sigma^d_{j=1}w_jx_j
$$


$$
\begin{align*}
E(w)&=\frac{1}{2}\Sigma^N_{n=1}(x^\intercal_nw-t_n)^2\\
&=\frac{1}{2}(Xw-t)^\intercal(Xw-t)
\end{align*}
$$

$E$ is the loss function.

Solve $min_wE(w)$

$W^*=(X^\intercal X)^{-1}X^\intercal t$

where 

- $W^*$ is the optimal weights
- $X$ is the design matrix (data) (one input vector per row)
- $t$ is the vector of target values

## Polynomial Curve Fitting

$$
y(x,w)=w_0+w1x+w_2x^2+\cdots+w_Mx^M=\Sigma^M_{j=0}w_jx^j
$$

Polynomial function is a nonlinear function of $x$, but it's a linear function of the coefficients $w$, thus it's still a **linear model**.
$$
E(w)=\frac{1}{2}\Sigma^N_{i=1}(y(x_n,w)-t_n)^2
$$



























---
title: PID Control
---

# Things to know

- How to implement and tune a PID controller
- When is PID insufficient
- How to formulate a potential field for goal-based navigation
- Disadvantages of potential fields
- Vector Field Histogram



# Intro

## Goal

Figure out how to generate the **Control Inputs (Actuating Signal)** so we get the desired **Controlled Variable (output/state)**.

There is always error between **Commanded Variable (what we want the system to do)** and the output (Controled Variable), otherwise, it's called Zero Error. <u>*We want to drive error to zero over time.*</u> 

**Solution: Controller**

Controller's job is to reduce error. 

## PID

Suppose we have a current state $curr$ and a goal state $goal$. The error is defined to be $e = goal - curr$. $e$ can be either positive or negative.

### P: Proportional (present)

Distance between $goal$ and $curr$ is the error and contributes to the controller system. The larger the distance, the larger the error.

$$\omega=K_pe(t)$$

### I: Integral (Past)

This takes the past error into account. It integrates error over time, and the goal is to reach a integral error of zero. 

For example, we are -5m from the $goal$, then +3m, then -1m, etc. As the integral of error goes to zero, we also gets closer to the $goal$.

i.e. We oscillate around the $goal$.

Integral of error from the beginning of the time: $\int^{\tau=t}_{\tau=0}e(\tau)d\tau$

$$\omega=K_pe(t)+K_i\int^{\tau=t}_{\tau=0}e(\tau)d\tau$$



### D: Derivative (Future)

Sometimes we don't want to go over the $goal$. e.g. the target height of a drone is 50m, it might be too dangerous to reach 51m, or it's beyond the actuator's limit.

In this case, we add one more term: future/**derivative**. Derivative is the rate of change, and tells the future of a system. A positive derivative of speed means a drone will fly higher in the future. If we take this term into account, it avoids going (too much) over the 50m line.



$$\omega=K_pe(t)+K_i\int^{\tau=t}_{\tau=0}e(\tau)d\tau+K_d \dot{e}(t)$$



Each term has a **weighting factor** that engineer needs to turn. 

PID is the simplest controller that uses the past, present and future error to achieve a steady state (Zero Error).



# How to Implement PID

- Assume time is discrete

- Identify error function, e.g. $e(t) = current\_state(t) - target\_state(t)$

- Is the measurement reliable

  - If measurement is noisy, choices are smoothing/filtering using

    1. Moving Average Filter with uniform weights

       Take a window of past info into account by averaging the window

       $\hat{t}=\frac{x_t+x_{t-1}+\cdots+x_{t-k+1}}{k}=\hat{x}_{t-1}+\frac{x_t-x_{t-k}}{k}$

       Potential Problem: the **larger the window** of the filter the slower it is going to register changes

    2. Exponential Filter

       $\hat{x}_t=\alpha\hat{x}_{t-1}+(1-\alpha)x_t$, $\alpha\in[0,1]$

       Take past information into account.

       Potential Problem: the closer $\alpha$ is to 1(less current info considered), the slower it is going to register changes.

- Approximate the integral of error by a sum

- Approximate the derivative of error by:

  - Finte Differences

    $\dot{e}(t_k)\approx\frac{e(t_k)-e(t_{t-1})}{\delta t}$

  - Filtered Finite Differences

    e.g. $\dot{e}(t_k)\approx\alpha\dot{e}(t_{k-1})+(1-\alpha)\frac{e(t_k)-e(t_{k-1})}{\delta t}$

- Limit the computed controls

- Limit or stop the integral term when detecting large errors and windup



# How to Tune the PID

## Manually

1. Use only the proportional term (set other gains/terms to zero)

2. When you see oscillations $\Rightarrow$ slowly add derivative term

   Increasing $K_d$ increases the duration in which linear error prediction is assumed to be valid (i.e. take future more into account, makes future more important)

3. Add a small integral gain

   

   

## [Ziegler-Nichols heuristic]([Ziegler–Nichols method - Wikipedia](https://en.wikipedia.org/wiki/Ziegler–Nichols_method))

1. Use only the proportional term (set other gains/terms to zero)
2. When you see **consistent** oscillations, record the proportional gain $K_u$ (aka ultimate gain) and the oscillation period $T_u$.

| Control Type  | $K_p$     | $T_i$     | $T_d$   |
| ------------- | --------- | --------- | ------- |
| $P$           | 0.5$K_u$  | -         | -       |
| $PI$          | 0.45$K_u$ | $T_u/1.2$ | -       |
| $PD$          | 0.8$K_u$  | -         | $T_u/8$ |
| classic $PID$ | 0.6$K_u$  | $T_u/2$   | $T_u/8$ |



## Automatic

**Slef-tuning PID Controllers**

After manual or Z-N tweaking, you can use coordinate ascent to search for a better set of parameters automatically.

TODO: fill in the code from lecture slide



# When is PID Insufficient

- Systems with large time delays
- Controllers that require completion time guarantees
  - E.g. the system must reach target state within 2 secs
- Systems with high-frequency oscillations
- High-frequency variations on the target state



# Cascading PID

- Sometimes we have multiple error sources (e.g. multiple sensors) and one actuator to control.
- We can use a master PID loop that sets the setpoint for the slave PID loop. 
  - Master (outer loop) runs at low rate, while slave (inner loop) runs at higher rate.



# Drawbacks of Potential Fields

- Local Minima

  - Attractive and repulsive forces can balance (cancel out each other), so robot makes no progress.

  - Closely spaced obstacles, or dead end.

  - Solution: Navigation Functions

    **Single Global Minimum** , and no local minima.

- Unstable Oscillation

  - The dynamics of the robot/environment system can become unstable.
  -  High speeds, narrow corridors, sudden changes





# Vector Field Histogram

TODO: listen to lecture and fill in the notes here





# Dynamic Window Approach (DWA)

Similar to back-tracking algorithm. Use simulation to simulate different scenarios. 

Local, reactive controller

1. Sample a set of controls for x,y,theta
2. Simulate where each control is going to take the robot
3. Eliminate those that lead to collisions.
4. Reward those that agree with a navigation plan.
5. Reward high-speeds
6. Reward proximity to goal.
7. Pick control with highest score that doesn’t lead to collision.







# Reference

- [MATLAB YouTube Playlist: Understanding PID Control]([Understanding PID Control, Part 1: What Is PID Control? - YouTube](https://www.youtube.com/watch?v=wkfEZmsQqiA&list=PLn8PRpmsu08pQBgjxYFXSsODEF3Jqmm-y))
- 
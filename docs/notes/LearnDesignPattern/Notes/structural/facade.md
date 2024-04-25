---
title: Facade (正面)
---

# What

> A structural design pattern that hides complex logic behind a simplified interface.
>
> A structural design pattern that provides a simplified interface to a library, framework, etc.

Idea: hide the complex logic and only expose the necessary API.

# Why

If a library is complex and expose lots of details, your code may be deeply coupled with the library. It will be hard to comprehend and maintain. So encapsulate complex logic into simple interface will be helpful to reduce the connections between your code and a third party library.

# Where

- Helpful when you need to integrate your code with a library that has dozens of features, while you only need a tiny bit of its functionality.



# Analogy

When you call a customer service, you can ask the agent any question and they will complete the task in the background and give you a simple response (yes or no). 

The agent is like the simple interface, they will do the complicated work for you and you just need to give a call and explain your problem. This hides you from the services. If you were to do it yourself online by clicking here and there, it will take longer. 




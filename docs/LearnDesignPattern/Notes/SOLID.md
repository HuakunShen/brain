# SOLID Principle

- [SOLID Principle](#solid-principle)
  - [Single-responsiblity Principle](#single-responsiblity-principle)
  - [Open-closed Principle](#open-closed-principle)
  - [Liskov Substitution Principle](#liskov-substitution-principle)
    - [Example](#example)
  - [Interface Segregation Principle](#interface-segregation-principle)
  - [Dependency Inversion Principle](#dependency-inversion-principle)
- [References](#references)

## Single-responsiblity Principle

## Open-closed Principle

## Liskov Substitution Principle

> Subclasses should be substitutable for their base classes.

Given that class B is a subclass of class A, we should be able to pass an instance of class B to any method that expects an instance of class A and the method should not give any weird output in that case.

So in terms of functionality, subclass `B` should be a superset of superclass `A`.

### Example

Although in math, Square is a special case of Rectangle, letting `Square` class inherit `Rectangle` class violates Liskov Substitution Principle.

`Square` cannot replace `Rectangle` as its width and height are set together.

## Interface Segregation Principle

## Dependency Inversion Principle

# References

- https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/

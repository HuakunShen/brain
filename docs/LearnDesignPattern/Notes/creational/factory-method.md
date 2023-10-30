# Factory Method

> A factory object can be used to create different types of objects under a specific superclass.
> More flexible and less work will need to be done when new classes of objects are added.

## Problem

Problematic when adding new classes. May need to modify the entire codebase.

## Solution

Instead of crating the objects directly, use a "factory" to create objects in one place, 
so that when a new class of object is added, you just need to modify one place.

## Sample Code

<!-- [Sample Code](../../src/creational_patterns/factory_method) -->

## Limitation


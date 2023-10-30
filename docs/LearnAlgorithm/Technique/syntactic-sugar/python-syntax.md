# Python Syntactic Sugar

## zip

- [Programiz](https://www.programiz.com/python-programming/methods/built-in/zip)

```python
l = [1, 2, 3, 4]
list(zip(l, l))		# [(1, 1), (2, 2), (3, 3), (4, 4)]

A = [[1,2,3], [3,2,1]]
list(zip(A))		# [([1, 2, 3],), ([3, 2, 1],)]
list(zip(*A))		# [(1, 3), (2, 2), (3, 1)]
```

## list

```python
l = [1, 2, 3, 4]
l[::-1]				# reverse
l[::1]				# stay the same
l[::2]				# select 1 every 2 element, ret=[1, 3]
```
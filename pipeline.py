from toolz import pipe
from functools import partial
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average = pipe(numbers, 
    partial(map, lambda x: x * 2),
    partial(filter, lambda x: x < 10),
    )
print(list(average))
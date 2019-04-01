from itertools import cycle

list1 = [1,2,3]
cy = cycle(list1)
for index in range(5):
    print(next(cy))
    
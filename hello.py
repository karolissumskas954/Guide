# Printinam stringa i terminala
print("hello")

# Is GitHub

# kaip sukuriamas exeption
raise Exception("Kazkas ivyko (error)")
# Kita variacija
raise SyntaxError("Sintakses klaida")

# Listo kurimas
my_list = ["one"]
# Listo elemento pasiekimas
print(my_list[0])


# Funkcijos kurimas
def name():
    print("")


# Funkcijos paleidimas
name()

# Importuojame tai ko reikes
import random

# Sudarome lista
random_exp = [1, 2, 3]
# Gauname random varianta
print(random.choice(random_exp))

import logging

# loggeris
l = logging.getLogger("toll_booth")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(levelname)s!!! %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.WARNING)

# Merge sort

def merge_sort(l):
    if len(l) < 2:
        return l
    middle = len(l) // 2
    sorted_left = merge_sort(l[:middle])
    sorted_right = merge_sort(l[middle:])
    return merge(sorted_left, sorted_right)


def merge(left, right):
    left_i = 0
    right_i = 0
    result = []
    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    result.extend(left[left_i:])
    result.extend(right[right_i:])
    return result


l = [5, 3, 7, 1, 4, 4, 2, 10]
l = merge_sort(l)
print(f"Sorted list: {l}")

# Stack

class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, v):
        self.__stack.append(v)

    def pop(self):
        return self.__stack.pop()

    def __len__(self):
        return len(self.__stack)

    def is_empty(self):
        return self.__stack == []

# Queue

class Queue:
    def __init__(self):
        self.__queue = []

    def push(self, v):
        self.__queue.append(v)

    def pop(self):
        return self.__queue.pop(0)

    def __len__(self):
        return len(self.__queue)

    def is_empty(self):
        return self.__queue == []



#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

if __name__ == "__main__":
  
def sum_numbers_decorator(start):
    def sum_numbers(func):
        def wrapper(string):
            numbers = list(map(int, string.split()))
            return start + func(numbers)
        return wrapper
    return sum_numbers


@sum_numbers_decorator(start=5)
def sum_numbers(numbers):
    return sum(numbers)


input_string = input("Введите строку целых чисел через пробел: ")
result = sum_numbers(input_string)
print("Сумма чисел:", result)

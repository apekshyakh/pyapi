#!/usr/bin/python3

""" This is a commonly used challenge to see if applicants actually know how to code!
Write a short program that prints each number from 1 to 100 on a new line
For each multiple of 3, print "Fizz" instead of the number
For each multiple of 5, print "Buzz" instead of the number. 
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the numbers
"""
for x in range(1,101,):
    
    if x%3 == 0 and x%5 ==0:
        print("FizzBuzz")
    elif x%3 == 0:
        print("Fizz")
    elif x%5 == 0:
        print("Buzz")
    else:
        print(x)

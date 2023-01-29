'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def day1(numbers, k):
    for i in range(len(numbers)):

        if (k-numbers[i] in numbers):
            return True

print(day1([10,15,3,7],10) == True)
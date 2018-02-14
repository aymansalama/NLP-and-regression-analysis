# Owner: Ayman Salama
# Email: ayman3salama@gmail.com
# Q1. Write a function in python to sum up a given set of numbers other than itself Input:
# An array of n integers nums, Output: An array output such that output[i] is equal to
# the sum of all the elements of nums except nums[i]. For example, given [1,2,3,4], return [9,8,7,6].

# The function sum_list, takes a list as an input and calculate the sum of all its elements and return the sum
def sum_list(original_list):
    sum_numbers = 0
    for x in original_list:
        sum_numbers += x
    return sum_numbers

# The function create_new_list take a list as input, call sum_list function to calcuate the sum and create the new list
# where each element is the sum of all list elements minus the element itself
def create_new_list(original_list):
    sum_numbers=sum_list(original_list)
    newlist= []
    for x in original_list:
        newlist.append(sum_numbers-x)
    return newlist

testlist=[1,2,3,4]
print (create_new_list(testlist))

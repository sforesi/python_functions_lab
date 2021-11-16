# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum 


# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list


# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

# def occurances(a, b): # function that takes two strings arguments as a parameter 
#   count = 0 # set count to zero 
  


# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*nums):
  product = 1
  for n in nums:
    product *= n
  return product 

# function calls 
print(sum_to(6))
# print(largest([1, 2, 3, 4, 0]))
# print(occurances('fleep floop', 'e')   # returns 2)
print(product(-1, 4)) # returns -4
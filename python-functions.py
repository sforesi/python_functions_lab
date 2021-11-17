# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to(num): # function that takes a single parameter named 'num' to represent an integer
  sum = 0 # set the sum to zero, starting point 
  for n in range(1, num + 1): # for each item that is in the range of 1- 'num' + 1 
    sum += n # as we iterate through the range add the current number to the sum, sum will always be stored as whatever the previous number was added
  return sum # ending the function and determining output 
print(sum_to(6))


# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list

def largest(numbers): # function named largest that takes a single parameter 'numbers' to represent a list
  largest = 0 # at the beginning of the function set the largest number in the list to 0 
  for n in numbers: # for each element in the list 
    if n > largest: # if current is greater than the largest number in the list
      largest = n  # that number should become the new largest number ** wtf can't i flip these around? if n = largest it outputs 0 
  return largest 
print(largest([1, 2, 3, 4, 0, 10]))


# 3. Write a function named occurances that takes two string arguments as input and counts the number of occurances of the second string inside the first string.

  # returns 2
# occurances('fleep floop', 'p')   # returns 2
# occurances('fleep floop', 'ee')  # returns 1
# occurances('fleep floop', 'fe')  # returns 0

def occurances(str1, str2): # function that takes two strings arguments as a parameter 
  print(str1.count(str2)) # count how many occurances of str2 are inside of str1 
occurances('fleep floop', 'e') 


# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*nums): # declare a function named product that accepts an arbitrary number '*' 
  product = 1 # set product equal to 1, not zero because it will always return zero 
  for n in nums: # for each element in the list of numbers 
    product *= n # multiply that current element by product 
  return product 

print(product(-1, 4)) # returns -4
#!/usr/bin/env python
# coding: utf-8

# # PJP Core - Python
# ## Python Fundamentals

# ## Exercises

#  Write a program to check if a given number is Positive, Negative, or Zero.

# In[1]:


a = 0

if(a == 0):
    print('number is zero')
elif(a >= 0):
    print('number is positive')
elif(a <= 0):
    print('number is negative')


#  Write a program to check if a given number is odd or even.

# In[2]:


a = 231

if (a%2 == 0):
    print('a is even')
else:
    print('number is odd')


# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
#  
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# 
# lastDigit(3, 113) → true

# In[3]:


a = 17
b = 27

if( a%10 == b%10):
    print('numbers have the same last digit')
else:
    print('numbers have different last digit')


# 	
#  Write a program to print numbers from 1 to 10 in a single row with one tab space.

# In[13]:


for i in range(1,11):
    print(i, end="    ")


#  Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.

# In[5]:


for i in range(23,58):
    if(i%2 == 0):
        print(i)


# 	
#  Write a program to check if a given number is prime or not.

# In[6]:


a = 123

if(a>=1): #condition for 1 to not include in the loop    
    for i in range(2,a):
        if (a%i == 0): # checking for divisibilty with the numbers from 2 to itself
            print(a,end=" is not a prime number")
            break
    else:
        print(a,end=" is a prime number")

else:
    print(a,end=" is a prime number")


#  Write a program to print prime numbers between 10 and 99.

# In[7]:


for i in range(10,100): # range for the input numbers
    for j in range(2,i): # checking if the individual number are prime
        if (i%j == 0): # checking for divisibilty with the numbers from 2 to itself
            break
    else:
        print(i)


#  Write a program to print the sum of all the digits of a given number.
# Example:
# 
# I/P:1234
# 
# O/P:10

# In[8]:


a = 123434
sum = 0
while(a>0):
    last_digit = a%10
    a = a//10
    sum = sum + last_digit
print(sum)


# 	
#  Write a program to reverse a given number and print.
# 
# Example:1
# 
# I/P: 1234
# 
# O/P:4321
# 
# Example:2
# 
# I/P:1004
# 
# O/P:4001

# In[9]:


a = 14162
reverse = 0

while (a>0):
    last_digit = a%10 #gives the last digit of the original number
    reverse = reverse*10 + last_digit #gives the reverse number
    a = a//10 #eliminates the last digit
print(reverse)


#  Write a program to find if the given number is palindrome or not
# 
# Example:1
# 
# I/P:110011
# 
# O/P: 110011 is a palindrome.
# 
# Example:2
# 
# I/P:1234
# 
# O/P: 1234 is not a palindrome.

# In[2]:


a = 11011
b = a # stored value of a in b as a's value will change due to while loop
rev = 0

while (a>0):
    last_digit = a%10 #gives the last digit of the original number
    rev = rev*10 + last_digit #gives the reverse number
    a = a//10 #eliminates the last digit

if( b == rev):
    print(b, end = " is a palindrome")
else: 
    print(b, end = ' is not a palindrome')
    


# In[ ]:





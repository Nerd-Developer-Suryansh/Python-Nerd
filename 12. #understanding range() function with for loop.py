#understanding range() function with for loop 

#range() function returns allows the user to generate a series of numbers within a given range.
#SYNTAX :           range(start,   stop,    step)
#by default values:        0    till last     1

# for loop is used to iterate over a sequence such as a list, tuple, dictionary, set, or string.
# It is used to execute a block of code repeatedly for each item in the sequence.
# SYNTAX : for  <variable> in <sequence>:
#                       print(variable)                


a=int(input("enter a last no: "))
for i in range(a): # i is variable where range values are stored and  range(a) is a sequence
    print(i)
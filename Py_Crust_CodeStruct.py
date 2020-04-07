import math
#4.1 Assign the value 7 to the variable guess_me. 
#Then, write the conditional tests (if, else, and elif) 
#to print the string 'too low' if guess_me is less than 7, 
#'too high' if greater than 7, and 'just right' if equal to 7. 


guess_me = int(input('Enter a digit: '))
print(guess_me)
if (guess_me == 7):
    print("just right")
elif (guess_me < 7 ):
    print("too low")
else:
    print("too high")

#4.2 Assign the value 7 to the variable guess_me and the value 1 to the variable start.
# Write a while loop that compares start with guess_me. Print too low if start is less than guess me.
#  If start equals guess_me, print 'found it!' and exit the loop.
#   If start is greater than guess_me, 
#  print 'oops' and exit the loop.
#   Increment start at the end of the loop.

guess = 7
start = 1
while (start <= guess):
    print("too low")
    
    if (start == guess):
        print("found it")
       
    if (start > guess):
        print('oops')
        

    start += 1

#4.3 Use a for loop to print the values of the list [3, 2,1, 0]. 
list = [3,2,1,0]
for v in list:
    print(v)

#4.4 Use a list comprehension to make a list of the even numbers in range(10). 

even_numbers = [number for number in range(0,10) if number % 2 == 0]
print(even_numbers)


#4.5 Use a dictionary comprehension to create the dictionary squares. 
#Use range(10) to return the keys, and use the square of each key as its value. 
dict_square = {1,2,3,4,5,6,7,8,9,10}
sq = {key: key**2 for key in dict_square}
print(sq)


#4.6 Use a set comprehension to create the set odd from the odd numbers in range(10). 
odd_set = {number for number in range(0,10) if number % 2 == 1}
print(odd_set)

#4.7 Use a generator comprehension to return the string 'Got '
#  and a number for the numbers in range(10).
#   Iterate through this by using a for loop. 
str = 'Got '
num = {word:str.count(word) for word in str}
print (num)



#4.8 Define a function called good that returns the list ['Harry', 'Ron', 'Hermione'].
def good():
    name = {'Harry', 'Ron', 'Harmonize'}
    print(name)
    return name


good() # to call the function

# 4.9 Define a generator function called get_odds that returns the odd numbers from range(10). 
# Use a for loop to find and print the third value returned.
def get_odds():
    x = {number for number in range(0,10) if number % 2 == 1}
    print(x)
    return x
    for value in x.copy():
        print('the third value is: ' +  value[2])
        return value[2]
    
    

get_odds() # to call the Function



#  4.10 Define a decorator called test that prints 'start'
#  when a function is called and 'end' when it finishes.
def test(prefix, postfix):
    def start():
        print(prefix, 'start')
        return(prefix,'start')
    def end():
        print(postfix,'end')
        returun(postfix,'end')




#4.11 Define an exception called OopsException. Raise this exception to see what happens.
# Then write the code to catch this exception and print 'Caught an oops'.

class OopsException(Exception):
    pass

try:
    raise OopsException('panic')
except OopsException as exe:
    print('Caught an oops')

    






#  4.12 Use zip() to make a dictionary called movies that pairs these
#   lists: titles = ['Creature of Habit', 'Crewel Fate'] and
#    plots = ['A nun turns into a monster', 'A haunted yarn shop'].

tiles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
for title,plot in zip(tiles,plots):
    print('titles: ', title, ' plots: ', plot)
#Question 1 to 3
#3.1. Create a list called years_list, starting with the year of your birth, 
#and each year thereafter until the year of your fifth birthday. 
#For example, if you were born in 1980. 
#the list would be years_list = 
#[1980, 1981, 1982, 1983, 1984, 1985].
# If you’re less than five years old and reading this
#book, I don’t know what to tell you. 
#3.2. In which year in years_list was your third birthday?
# Remember, you were 0 years of age for your first year. 
#3.3 In which year in years_list were you the oldest? 


year_list = [1993,1994,1995,1996,1996, 1997]
print("My third birthday was " , year_list[3])
print("I was oldest in ", year_list[-1])

#Question 4 to 5

#3.4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella". 
#3.5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list? 

things = ["mozarella", "cinderalla", "salmonella"]


print(things[0].capitalize(), things[1].capitalize(), things[2].capitalize())
"""
No it did not channge the element in the list


"""
#Question 6 to 7
#3.6. Make the cheesy element of things all uppercase and then print the list.
#3.7. Delete the disease element from things, collect your Nobel Prize, and print the list. 




pythons = { 'Chapman': 'Graham', 
        'Cleese': 'John',   
       'Gilliam': 'Terry', 
    'Idle': 'Eric',   
   'Jones': 'Terry',   
 'Palin': 'Michael',   } 
# to change the value of dictionary value 

print(pythons['Cleese'].upper())

del year_list[0]
print(year_list)
name4 = "Collect your noble prize"
year_list.append(name4)
print(year_list)

#Question 8 and 9

#3.8. Create a list called surprise with the elements "Groucho", "Chico", and "Harpo". 
#3.9 Lowercase the last element of the surprise list,

suprise = ["Groucho", "Chico", "Harpo"]
print(suprise[0].lower(), suprise[1].lower(), suprise[2].lower())
suprise.reverse()
print(suprise)

os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)

#Capitalize the suprise list
print(suprise[0].capitalize(), suprise[1].capitalize(), suprise[2].capitalize())


# Question 10 to 11
#3.10. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse. 
#3.11. Using your three-word dictionary e2f, print the French word for walrus. 

etof = {"dog" : "chien","cat" : "chat" , "walrus": "morse"}
print("The French word for walrus is: ", etof["walrus"])
ftoe = { "chien" : "dog", "chat" : "cat"  , "morse" : "walrus"}

# Question 12
#Make a French-to-English dictionary called f2e from e2f. Use the items method.
#to get all the key value pair use item method

print(etof.keys())
print(list(etof.items()))
print(list(etof.values()))

#Question 13
# Using f2e, print the English equivalent of the French word chien.  
#Print the English equivalent of French word chien
for value in ftoe.items():
  print ("The English word for Chien is: "  + "and its value is" + ftoe["chien"])


#Question 14
#3.14. Make and print a set of English words from the keys in e2f. 
#for key in etof:
print(etof.keys())

#Question 15
#3.15. Make a multilevel dictionary called life. Use these strings for the topmost keys:
# 'animals', 'plants', and 'other'. Make the 'animals' key 
# refer to another dictionary with the keys 'cats', 'octopi', and 
# 'emus'. Make the 'cats' key refer to a list of strings with the values 
# 'Henri', 'Grumpy', and 'Lucy'.
#  Make all the other keys refer to empty dictionaries.

cake = ['Henri', 'Grumpy', 'Lucy']
ox = {''}
em = {''}

life = {'animals': {'cats': cake, 'octopi': ox, 'emus': em},
        'plants' : {''},
        'other' : {''},
        }


#Question 16
#3.16. Print the top-level keys of life.
for keys in life:
    print("Top-most keys: ", keys)



#Question 17
#3.17. Print the keys for life['animals'].

for k, v in life.items():
    print("the keys of life are: ", k)



#Question 18
#3.18. Print the values for life['animals']['cats'].
values = 'animals'
for k, v in life.items():
    if (k == values):
      print(cake)

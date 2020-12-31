#Build a Dictionary

programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
"Loop":"The action of doing something over and over again"
}


#to have access to the dictionary
print(programming_dictionary["Bug"])
print("===========================")

print(programming_dictionary["Loop"])
print("===========================")


#Adding new items to dictionary
programming_dictionary["class"] = "A class is a blueprint that defines the variables and the methods common to all objects of a certain kind."

print(programming_dictionary)
print("===========================")


"""
#to define a new dictionary
empty_dictionary = {}   
"""

#to Edit an item in a dictionary
programming_dictionary["Bug"] = "A software bug is an error, flaw or fault in a computer program or system that causes it to produce an incorrect or unexpected result, or to behave in unintended ways."

print(programming_dictionary["Bug"])
print("===========================")

#to Loop through dictionary
for key in programming_dictionary:
    print(key)                          #Will print only the key
    print(programming_dictionary[key])  #Will print only the value
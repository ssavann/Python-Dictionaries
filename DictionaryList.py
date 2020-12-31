"""
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log. 
"""

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#create a function to add new value to the list
def add_new_country(country_visited, times_visited, cities_visited):
    
    #create an empty dictinary to pass the values
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited

    #to add into a list
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
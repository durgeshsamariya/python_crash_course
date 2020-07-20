# 3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

#list of countries
countries = ['US', 'UK', 'India', 'Australia', 'China', 'Japan']

#print list
print("\n Original list:")
print(countries)

#Modifying List
countries[5] = 'Korea'

print("\n Modified list:")
print(countries)

#append
countries.append('Japan')

#insert
countries.insert(0, 'Singapore')

print("\n After adding elements in list:")
print(countries)

#removing element
del countries[1]
countries.pop()
countries.remove('China')


print("\n After deleting elements from list:")
print(countries)

print("\n Sorted list :")
countries.sort()
print(countries)

print("\n Reverse sorted list :")
countries.sort(reverse=True)
print(countries)

print("\n Total countries in the list is " + str(len(countries)))

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests. • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner. • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner. • Print a message to each of the two people still on your list, letting them know they’re still invited. • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ['Jessica','Peter', 'John', 'Luke', 'Sarah', 'James', 'Jonathan']

print('Due to table issue I am only inviting 2 people.')

uninvited_guest = guest_list.pop()
print("Sorry " + uninvited_guest.title() + " for not inviting you for dinner.")

uninvited_guest = guest_list.pop()
print("Sorry " + uninvited_guest.title() + " for not inviting you for dinner.")

uninvited_guest = guest_list.pop()
print("Sorry " + uninvited_guest.title() + " for not inviting you for dinner.")

uninvited_guest = guest_list.pop()
print("Sorry " + uninvited_guest.title() + " for not inviting you for dinner.")

uninvited_guest = guest_list.pop()
print("Sorry " + uninvited_guest.title() + " for not inviting you for dinner.")

print(guest_list[0] + ", you are still invited for dinner.")
print(guest_list[1] + ", you are still invited for dinner.")

del guest_list[0] # removing first name from the list
del guest_list[0] # after removing first name from the list, second name become first name so removing from 0 index.

print(guest_list)

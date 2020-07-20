# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement to the end of your program informing people that you found a bigger dinner table. • Use insert() to add one new guest to the beginning of your list. • Use insert() to add one new guest to the middle of your list. • Use append() to add one new guest to the end of your list. • Print a new set of invitation messages, one for each person in your list.


guest_list = ['Peter', 'John', 'Sarah', 'James']

print("I found bigger table for dinner party.")

guest_list.insert(0, 'Jessica')
guest_list.insert(3, 'Luke')
guest_list.append('Jonathan')

print(guest_list[0] + " is invited for dinner.")
print(guest_list[1] + " is invited for dinner.")
print(guest_list[2] + " is invited for dinner.")
print(guest_list[3] + " is invited for dinner.")
print(guest_list[4] + " is invited for dinner.")
print(guest_list[5] + " is invited for dinner.")
print(guest_list[6] + " is invited for dinner.")

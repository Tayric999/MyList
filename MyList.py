my_list = []
print("1. empty list:", my_list)

#apend elements 10,20,30,40, to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("2. List after appendng elements:",my_list)

#insert the value 15 at the second position in my_list (index 1)
my_list.insert(1,15)
print("3. List after inserting at the second position in my_list:",my_list)

#extend my_list with another list [50,60,70]
my_list.extend([50,60,70])
print("4. List after extending: ",my_list)

#remove the last element from my_list
my_list.pop()
print("5. Lt after removing the last element:",my_list)

# sort my list in ascending order
my_list.sort()
print("6. List sorted in ascending order:",my_list)

#find and print the index of thevalue in my list
index_of_30= my_list.index(30)
print(" 7. The index of value 30 is:",index_of_30)
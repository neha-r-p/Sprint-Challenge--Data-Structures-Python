import time
from binary_search_tree import BinarySearchTree
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# print("name 1 first name", names_1[0])


duplicates = []
# create a tree with one list
    # create root with first name on list
root = names_1[0]
names_1_bst = BinarySearchTree(root)
# print("root bst", names_1_bst.value)
    #insert all other names
for name in names_1[1:]: #runtime O(n)
    names_1_bst.insert(name)
    # print("name", name)
#compare each name on second list to first
for name in names_2: #runtime O(n)
    if names_1_bst.contains(name): #runtime for bst is O(logn)?
#add name to duplicate if name is contained in both
        duplicates.append(name)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#Starter code runtime is O(n^2)?

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

fruits= {"mango","banana","grapes","mango","cherry"}
print(type(fruits))  #<class 'set'>
print(fruits) #{'mango', 'banana', 'grapes', 'cherry'}

# l1 = list(fruits)
# print(l1)

# for x in fruits:
#     print(x, end=",")


fruits.add("apple")
print("updated",fruits)#updated {'grapes', 'mango', 'cherry', 'banana', 'apple'}
fruits.add(("woodppple","orange"))
print(fruits) #{'grapes', 'mango', 'cherry', ('woodppple', 'orange'), 'banana', 'apple'}


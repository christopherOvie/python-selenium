fruits= ("banana","grapes","mango","cherry","mango")
print(fruits)
print(fruits.count('banana'))#1
print(fruits.index('banana'))#0

print("fruit tuple",fruits)#fruit tuple ('banana', 'grapes', 'mango', 'cherry', 'mango')
l1=list(fruits)
print(type(l1)) #<class 'list'>
print(l1) #['banana', 'grapes', 'mango', 'cherry', 'mango']
print('fruit list',l1) #fruit list ['banana', 'grapes', 'mango', 'cherry', 'mango']

t1=tuple(l1)
print(t1)  #('banana', 'grapes', 'mango', 'cherry', 'mango')



fruits= ("banana","grapes","mango","cherry")
print(type(fruits)) #<class 'tuple'>
print(len(fruits))  #4
print(fruits[0])

i=0
while(i<=3):
    print(fruits[i])
    i=i+1

print('iterating using for loop')

for x in fruits:
    print(x)

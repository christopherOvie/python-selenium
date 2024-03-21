fruits= ["banana","grapes","mango","cherry"]

print("original list",fruits)
#fruits[2]='orange' #replace
fruits.insert(2,"orange")  #shifted
print("modified list is ",fruits)

#
# original list ['banana', 'grapes', 'mango', 'cherry']
# modified list is  ['banana', 'grapes', 'orange', 'mango', 'cherry']
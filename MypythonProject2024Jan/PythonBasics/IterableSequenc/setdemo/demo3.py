fruits= {"mango","banana","grapes","mango","cherry"}
print('before remove',fruits) #before remove {'mango', 'banana', 'grapes', 'cherry'}
#diff betweeen remove and disccard
fruits.discard('banana')
print('after remove',fruits)  #after remove {'mango', 'grapes', 'cherry'}
print('program ended')
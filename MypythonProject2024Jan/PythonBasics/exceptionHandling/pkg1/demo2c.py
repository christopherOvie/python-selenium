print('program started')

l1=[10,20,30,40]

try:
     l1[4]

except IndexError:
   print('At given number does not exist')
except ZeroDivisionError:
   print('python cannot be divisible by zero')
finally:
    print('will be executed even exception is thrown or not')
print('program ended')
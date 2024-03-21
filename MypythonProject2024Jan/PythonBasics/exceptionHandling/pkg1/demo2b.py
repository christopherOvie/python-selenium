print('program started')

l1=[10,20,30,40]

try:
     l1[1]/0

except IndexError:
    print('At given number does not exist')
except ZeroDivisionError:
    print('python cannot be divisible by zero')
print('program ended')
print('program started')

l1=[10,20,30,40]

try:
     l1[3]/0

except IndexError:
    print('At given number does not exist')

except ZeroDivisionError:
    print('At given number of zero does not exist')

except Exception:
    print('general exception')

print('program ended')
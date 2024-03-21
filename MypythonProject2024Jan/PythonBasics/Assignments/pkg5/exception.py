

l1 = [10, 20, 30, 40, 50]


try:

    print(l1[8]/0)
except IndexError:
    print('index error and was handled')
except ZeroDivisionError:
    print('zero error and was handled')

finally:
    print('will be printed even if exception throwen or not')

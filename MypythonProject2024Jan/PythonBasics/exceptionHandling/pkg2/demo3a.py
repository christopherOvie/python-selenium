print('program started')
balance =100000
witdrawalamount=80000

if witdrawalamount> balance:
    print('insufficient money')
# elif(witdrawalamount>balance):
#     print('insufficient balance')

else:
    balance=balance-witdrawalamount
    print('money laft is' ,balance)

print('program ended')
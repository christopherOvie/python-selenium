balance =10000
witdrawalamount=12000

if witdrawalamount>balance:
    raise TypeError('insufficient balance')
else:    #withdrawal  less than balanc
    balance=balance-witdrawalamount
    print('remaining balance is',balance)


  #raise TypeError('insufficient balance')
#TypeError: insufficient balance
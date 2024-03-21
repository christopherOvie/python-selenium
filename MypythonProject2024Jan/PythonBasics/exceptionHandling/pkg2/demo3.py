balance =10000
witdrawalamount=12000

if balance>witdrawalamount:
  try:
      raise TypeError('insufficient balance')
  except  TypeError:
      print('my own handling message: insufficient balance! pls enter correct amount')

else:
    balance=balance-witdrawalamount
    print('remaining balance',balance)  #remaining balance -2000

print('program ended')
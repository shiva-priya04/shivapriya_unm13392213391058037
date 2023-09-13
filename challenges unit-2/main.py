class bankacc:
  def __init__(self,accno,acchname,initialbal):
    self.__accno=accno
    self.__acchname=acchname
    self.__accbal=initialbal
  def deposit(self,amt):
    if amt>0:
      self.__accbal=self.__accbal+amt
      print("Deposited: ${}.New balance:${}".format(amt,self.__accbal))
    else:
      print("Invalid deposit amount. Please deposite a positive amount")
  def withdraw(self,amt):
    if amt>0 and amt<=self.__accbal:
      self.__accbal=self.__accbal-amt
      print("withdrew: ${}.New balance: ${}".format(amt,self.__accbal))
    else:
      print("Invalid withdrawls amount or Insufficient balance")
  def display(self):
    print("Account Balance for {} (Account #{}): ${}".format(self.__acchname,self.__accno,self.__accbal))
account=bankacc(accno="66557788",acchname="Bro",initialbal=3500.0)
account.display()
account.deposit(550)
account.withdraw(250)
account.display()
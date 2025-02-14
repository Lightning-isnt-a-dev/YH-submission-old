from abc import abstractmethod, ABC

class Person():

  def __init__(self, NAME, TYÖ, BankAccount=150, MoneyMultiplier=1.0):
    self.NAME = NAME
    self.TYÖ = TYÖ
    self.BankAccount = BankAccount
    self.MoneyMultiplier = MoneyMultiplier

  def IncreaseMultiplier(self):
    self.MoneyMultiplier += 0.2
    return
  
  def Deposit(self, money):
    self.BankAccount = money
    return self.BankAccount

  def Withdraw(self, money):
    if self.BankAccount < money:
      return f"Sinulla ei ole tarpeeksi rahaa. Sinulla on {self.BankAccount}€.", False

    self.BankAccount -= money
    return f"Sinulla on {self.BankAccount}€ jäljellä.", True

  def Job(self, job):
    self.TYÖ = job

  
  def GetMultiplier(self):
    return self.MoneyMultiplier
  
  def GetMoney(self):
    return self.BankAccount
  
  def GetName(self):
    return self.NAME
  
  def GetJob(self):
    return self.TYÖ

  
  def SavePlayer(self):
    return self.NAME, self.BankAccount, self.MoneyMultiplier

  def ClearSave(self):
    self.BankAccount = 150
    self.MoneyMultiplier = 1.0
    return 
    
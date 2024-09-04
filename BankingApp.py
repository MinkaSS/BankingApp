import  BaseModel 


class BankingApp:
  def start(self):
    # create an Object bank_account 
    bank_account = BaseModel.BankAccount () 
    bank_account.set_account_number("12345")
    bank_account.set_account_owner("Filan Fisteki")
    bank_account.set_account_balance("500.0")


   #creat an Object BankAccountOwner
        
    bank_account_owner=BaseModel.BankAccountOwner()
    bank_account_owner.set_first_name ( "Filan")
    bank_account_owner.set_last_name ("Fisteki")

    #Print the Outpt

    print( "Account Number  :" + str(bank_account.get_account_number()) )
    print( "Account Owner   :" + str(bank_account_owner.get_first_name()) +" " + str(bank_account_owner.get_last_name())) 
    print( "Account Balance :" + str(bank_account.get_account_balance()) )

bank_app=BankingApp()
bank_app.start()

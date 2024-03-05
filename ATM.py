print("State bank of india")

name=input("Enter your name: ")
print("Hello", name)
a=int(input("Enter your account number:"))
b=int(input("Enter your pin:"))
print("Welcome to the State bank of india")
print("Press 1. Deposit")
print("Press 2. cashwithdrawl")
print("Press 3. check balance")
print("Press 4. Fund transfer")
print("Press 5. change your pin")
x=int(input("Enter your choice:"))

match x:
  case 1:
   print("you account number is",a)
   print(name,"How much money do you want to deposit?")
   y=int(input("Enter the amount:"))
   print("Your money is deposited successfully",y) 
  case 2:
     print("you account number is",a) 
     z=int(input("Enter the amount:"))
     print("Your money is withdrawl successfully",z)
  case 3:
    print("you account number is",a)
    print("your current balance is:10000000")
  case 4:
    print("you account number is",a)
    n=int(input("Enter the account number you want to transfer money:"))
    m=int(input("Enter the amount you want to transfer:"))
    print("sucessfully transfer",n)
  case 5:
    print("you account number is",a)
    h=int(input("Enter your old pin:"))
    s=int(input("Enter your new pin:"))
  case _:
    print("Wrong choice")

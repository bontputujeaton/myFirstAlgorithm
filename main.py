# The main.py file was edited n made in local file in another machine in another Github account
print("Welcome to the school cantteen!")


sandwich = 4.50
chips = 2.50
wrap = 5.00


totalprice = 0


name = input("Please put in enter your name here: ")


print("Heres the menu")
print("Sandiwch", "$ ", sandwich)
print("chips", "$ ", chips)
print("Wrap", "$ ", wrap)
print("When you are finished type 'done'")


while True:
    order = input("Cchoose your item:  ")
    if order == "done":
       break
    if order == "sandwich":
        totalprice += sandwich
    elif order == "chips":
        totalprice += chips
    elif order == "wrap":
        totalprice += wrap
    else:
        print("Thats not an option choose from the menu above")


if totalprice > 10:
    totalprice = totalprice - 0.1


print("heres the reciept")
print("name:", name)
print("Total: $", totalprice)


#call apply disscount
#displayReciept

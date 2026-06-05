print("Welcome to the Kwek Kwek Calculator!")
amount = int(input("How much do you have right now? "))
price = int(input("How much is one piece of kwek kwek? "))

total_kwek_kwek = amount // price
print("You can buy " + str(total_kwek_kwek) + " pieces of kwek kwek with your money.")

leftover_money = amount % price
print("And you will have " + str(leftover_money) + " left.")

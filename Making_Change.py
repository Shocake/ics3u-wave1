cents = int(input("How many cents are owed?"))
quarters = cents//25
dimes = (cents - (quarters * 25))//10
nickels = (cents - (quarters * 25) - (dimes * 10))//5
pennies = (cents - (quarters * 25) - (dimes * 10) - (nickels * 5))
print(str(quarters) + " quarters")
print(str(dimes) + " dimes")
print(str(nickels) + " nickels")
print(str(pennies) + " pennies")
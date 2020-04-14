money = float(input("How much money would you like to deposit in dollars?"))
oneyears = money * 1.04
twoyears = oneyears * 1.04
threeyears = twoyears * 1.04

oneyear = str(round(oneyears, 2))
twoyear = str(round(twoyears, 2))
threeyear = str(round(threeyears, 2))

print("After 1 year, you will have " + oneyear + " dollars.")
print("After 2 years, you will have " + twoyear + " dollars.")
print("After 3 years, you will have " + threeyear + " dollars.")
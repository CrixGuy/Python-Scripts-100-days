print("Welcome to the Python Pizza Deliveries")
size = input("What size pizza do you want S, M or L: ")
add_pepperoni = input("Do you want pepperoni: Y or N: ")
extra_cheese = input("Do you want extra cheese: Y or N: ")


if size == 'S':
    cost = 15
elif size == 'M':
    cost = 20
elif size == 'L':
    cost = 25
else:
    print("Invalid selection")    



if add_pepperoni == 'Y':
    if size == 'M' or size == 'L':
        cost += 3
    else:
        cost += 2
        
if extra_cheese == 'Y':
    cost += 1

print(f"Your final bill is: {cost}")
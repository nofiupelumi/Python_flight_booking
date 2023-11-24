 import time
# List of products with their details
products = [
    {"name": "Tea", "price": 2200, "stock": 5},
    {"name": "Milk", "price": 1800, "stock": 8},
    {"name": "Sugar", "price": 550, "stock": 5},
    {"name": "Bread", "price": 750, "stock": 8},
    {"name": "Detergent", "price": 850, "stock": 5},
    {"name": "Bathing Soap", "price": 750, "stock": 8},
    {"name": "Coca Cola", "price": 250, "stock": 5},
    {"name": "Body Spray", "price": 2250, "stock": 8},
    {"name": "Tooth Brush", "price": 250, "stock": 5},
    {"name": "Tooth Paste", "price": 750, "stock": 8},
]
# List of users with their account balances
usernames = [
    {"name": "Ahmed", "amount": 5000},
    {"name": "Blessing", "amount": 10000},
    {"name": "Pelumi", "amount": 15000},
    {"name": "Yemi", "amount": 20000},
]
#ask user to login with their name
username = input("Please login with your username: ")
usernames = [user for user in usernames if user["name"] == username]
#check if the data is in the database
#print name and balance attached to the name
if usernames:
    user = usernames[0]
    print(f"Welcome {user['name']}!")
    print(f"Your account balance is {user['amount']}.")
    #ask user what action they will like to perform
    selection = input("What tasks will you like to perform? \n1. See Available Products. \n2. Buy Products.\n3. Quit\n")
     
    if selection == "1":
        # Display available products
        print("Available Products:")
        for idx, product in enumerate(products, start=1):
            print(f"{idx}. {product['name']} - N{product['price']} (Stock: {product['stock']})")
        proceed1= input("What would you like to do next?: \n1. Buy Products.\n2.Quit.\n")
        if proceed1 == "1":
            # Shopping cart and total cost initialization
            shopping_cart = []
            total_cost = 0
            # User adds products to the cart
            num_products = int(input("How many products would you like to add to your cart? "))
            for _ in range(num_products):
                choice = input("Enter the product number: ")
                if choice.isdigit():
                    choice = int(choice)
                    if 1 <= choice <= len(products):
                        product = products[choice - 1]
                        if product["stock"] > 0:
                            shopping_cart.append(product)
                            total_cost += product["price"]
                            product["stock"] -= 1
                        else:
                            print("Sorry, this product is out of stock.")
                    else:
                        print("Invalid product number.")
                else:
                    print(f'Please enter the corresponding number for {choice}')
            for item in shopping_cart:
                # Display items in the cart and calculate total cost
                print(f"{item['name']} - N{item['price']}")
            print("\n...Calculating total cost...\n")
            time.sleep(2)
            print(f"Total Cost: N{total_cost}")
            # User decides whether to proceed with the purchase
            checkout = input("Will you like to proceed? \n1. Yes\n2. No\n")
            if checkout == "1":
                # Check if the user has sufficient balance
                if total_cost > user['amount']:
                    balance = total_cost - user['amount']
                    print(f"Insufficient account balance.\nOutstanding N{balance} can be added to your tab")
                    proceed = input('\nWould you like to proceed?\n1. Yes\n2. No\nYour Response: ').lower()
                    if proceed == '1' or proceed == 'yes':
                        print(f'A negative balance of N{balance} has been added to your customer card\nThanks for shopping with us.')
                    elif proceed == '2' or proceed == 'no':
                        print('Purchase failed due to insufficient balance')
                    else:
                        print('Invalid response. Action denied.')
                else:
                    print(f"Bye for now, {user['name']}\nRemaining Account Balance: N{user['amount'] - total_cost}\nThank you for shoping with us..")
            elif checkout == "2":
                print('\nQuiting app...\n')
                time.sleep(2)
                print(f"Bye for now, {user['name']}. Come back soon.\n")
        elif proceed1 == "2":
            print('\nQuiting app...\n')
            time.sleep(2)
            print(f"Bye for now, {user['name']}. Come back soon.\n")
        else:
            print(f"Invalid input {user['name']}\nPlease start over.")
        

    elif selection == "2":
        shopping_cart = []
        total_cost = 0

        num_products = int(input("How many products would you like to add to your cart? "))
        for _ in range(num_products):
            choice = input("Enter the product number: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(products):
                    product = products[choice - 1]
                    if product["stock"] > 0:
                        shopping_cart.append(product)
                        total_cost += product["price"]
                        product["stock"] -= 1
                    else:
                        print("Sorry, this product is out of stock.")
                else:
                    print("Invalid product number.")
            else:
                print(f'Please enter the corresponding number for {choice}')
        for item in shopping_cart:
            print(f"{item['name']} - N{item['price']}")
        print("\n...Calculating total cost...\n")
        time.sleep(2)    
        print(f"Total Cost: N{total_cost}")
        checkout1 = input("Will you like to proceed? \n1. Yes\n2. No\n")
        if checkout1 == "1":
            if total_cost > user['amount']:
                balance = total_cost - user['amount']
                print(f"Insufficient account balance.\nOutstanding N{balance} can be added to your tab")
                proceed = input('\nWould you like to proceed?\n1. Yes\n2. No\nYour Response: ').lower()
                if proceed == '1' or proceed == 'yes':
                    print(f'A negative balance of N{balance} has been added to your customer card\nThank you for shopping with us.')
                elif proceed == '2' or proceed == 'no':
                    print('Purchase failed due to insufficient balance')
                else:
                     print('Invalid response. Action denied.')
            else:
                print(f"\nBye for now, {user['name']}\nRemaining Account Balance: N{user['amount'] - total_cost}\nThank you for shopping with us")
        elif checkout1 == "2":
            print('\nQuiting app...\n')
            time.sleep(2)
            print(f"Bye for now, {user['name']}. Come back soon.\n")
            
    elif selection == "3":
        print('\nQuiting app...\n')
        time.sleep(2)
        print(f"Bye for now, {user['name']}. Come back soon.\n")
else:
    print("Wrong input, please enter the correct username")
    
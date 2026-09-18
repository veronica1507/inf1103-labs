def get_valid_input(stock):
    stock = input("Enter stock quantity: ")
    if stock!= "quit":
        if stock.isdigit():
           stock = int(stock)
           return int(stock)
        elif stock.indigit()<0:
            print("No negative numbers")
        else:
           print("The stock quantity entered is not a valid integer")      
    else:
        return stock

def process_delivery(current_total,new_value):
    return current_total + new_value

# 10% of the stock quantity
def calculate_tax(amount):
    tax = 0.10 * amount
    return tax


inventory = 0
reject = 0
stock = ""

while stock!= "quit":
    stock = input("Enter stock quantity: ")
    if stock.isdigit():
        stock = int(stock)
        if stock < 0:
            print("negative number not allowed")
            reject = reject + 1
            continue
        inventory = inventory + stock
        print("Stock added")
        if inventory >= 500:
            print("Inventory is already 500 or more")
            break
    else:
        print("Integers or quit only")
        reject = reject + 1

print("Total Units Processed: ", inventory)
print("Number of Failed Entries: ", reject )





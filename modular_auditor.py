def get_valid_input():
    stock = input("Enter stock quantity: ")
    if stock!= "quit":
        if stock.isdigit():
           stock = int(stock)
           return int(stock)
        elif stock.indigit()<0:
            print("No negative numbers")
            return None
        else:
            print("The stock quantity entered is not a valid integer")      
            return None
    else:
        return stock

def process_delivery(current_total,new_value):
    return current_total + new_value

# 10% of the stock quantity
def calculate_tax(amount):
    tax = 0.10 * amount
    return tax

def generate_report(total_units, failed_attempts):
    print ("Total Deliveries Processed:", total_units)
    print("Failed_attempts", failed_attempts )

inventory = 0
reject = 0
stock = ""

while True:
    stock = get_valid_input()
    if stock == "quit":
        break
    if stock == None:
        reject = reject + 1
        continue
    inventory = process_delivery(inventory, stock)
    print("Stock added", stock)
    tax_amount = calculate_tax(stock)
    print("Tax amount(10%): ", tax_amount)
    if inventory > 500:
        print("Overstock alert: the inventory has exceeded 500 units" , inventory)
        break
    
generate_report(inventory,reject)






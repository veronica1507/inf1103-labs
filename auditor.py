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
        if inventory >= 500:
            print("Inventory is already 500 or more")
            break
    else:
        print("Integers or quit only")
        reject = reject + 1

print("Total Units Processed: ", inventory)
print("Number of Failed Entries: ", reject )


        
    


        
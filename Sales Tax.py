sale_amount = 1
total_sale = 0

print("Enter sale amounts. When finished entering amounts, enter '0' to continue: \n")

while sale_amount != 0:
    sale = raw_input("Enter the amount: \n $")
    sale_amount = float(sale)
    total_sale += sale_amount

else:
    print("The subtotal is $" + str(total_sale))
    sales_tax = round(total_sale * .06, 2)
    print("Sales tax equals $" + str(sales_tax))
    total_due = round(total_sale + sales_tax, 2)
    print("Total amount due equals $" + str(total_due))

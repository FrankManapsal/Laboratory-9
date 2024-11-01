product1=int(input("Amount of First Product: "))
product2=int(input("Amount of third Product: "))
product3=int(input("Amount of third Product: "))
total=float(product1+product2+product3)
print("Total Amount:",total)
payment=int(input("Payment Amount: "))
if payment>=total:
    print("Payment Accepted!")
    change=int(payment-total)
    print("Change:",change)
else:
    print("Payment Denied!(Insufficient Amount)")
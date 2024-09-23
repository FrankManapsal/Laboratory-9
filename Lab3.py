salary=int(input("What is your Monthly Salary?: "))
if salary>=30000:
    loan=int(input("What is your Desired Loan: "))
    if loan<=salary*10:
        print("You are Eligible for a Loan!")
        monthsforpayment=int(input("How many Months you want to Pay the Loan?:"))
        interest=loan*0.10
        totalpayment=float(loan+interest)
        print("Amount to Pay:",totalpayment)
    else:
        print("Uneligible for Loan.(Loan too High.)")
else:
    print("Uneligible for Loan(Salary too Low.)")
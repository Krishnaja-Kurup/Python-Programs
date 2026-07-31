consumer_name=str(input("Enter Consumer name:"))
consumer_id=int(input("Enter Consumer id:"))
unit=int(input("Enter unit consumed:"))
cost=int(input("Enter cost per unit:"))
print("Consumer datatype:",type(consumer_name))
print("Consumer id datatype",type(consumer_id))
total_bill=unit*cost
discount=(2/100)*total_bill
payable_amount= total_bill-discount
print("Total bill:", total_bill)
print("Discount:", discount)
print("Payable Amount:", payable_amount)
result=(unit>200 and payable_amount>1000)
if result:
    print("Units are greater than 200 and bill is greater than 1000.")
else:
    print("Condition not satisfied.")
print("Precedence:",200*10-(100/2)+3**5)


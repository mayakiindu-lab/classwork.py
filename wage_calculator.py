name=input("Enter Customer's Name: ")
age=int(input("Enter Customer's Age: "))
if age <18:
    print('INVALID!!!')
    exit()
else:
    print('Loan Applicable')

income=int(input("Enter Customer's Income: "))
credit=int(input("Enter Customer's Credit Score: "))
if income >= 30000 and credit >=700:
    comment='Approved'
    reason='CAN BE ABLE TO PAY THE LOAN ON TIME'
else:
    comment='Rejected !!!'
    reason='CAN FAIL TO PAY THE LOAN'
print('')
print("Customer's Name: ",name)
print("Customer's Age: ",age)
print("Customer's Income: ",income)
print("Customer's Credit Score: ",credit)
print('Loan ',comment)
print(reason)
payroll=input("Enter Payroll's Number: ")
name=input("Enter Name: ")
gender=input("Please enter your Gender: ")
salary=int(input("Please enter your Salary: "))
print('Job Groups include:')
print('J')
print('K')
print('L')
print('M')

job=input("Please Select your Job Group: ")
if job.upper() == 'J':
    allowance = 5000

elif job.upper() == 'K':
    allowance = 5500
elif job.upper() == 'L':
    allowance = 6000
elif job.upper() == 'M':
    allowance = 6500

gross_pay=salary+allowance
taxes=(12*salary)/100
net_pay=gross_pay-taxes

print("--- Employee's Details ---")
print("Payroll: ",payroll)
print("Employee's Name: ",name)
print("Gender: ",gender)
print("Salary: ",salary)
print("Job Group: ",job)
print("Allowance: ",allowance)
print("Gross Pay: ",gross_pay)
print("Tax: ",taxes)
print("Net Pay: ",net_pay)

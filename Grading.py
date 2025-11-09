name=input("Enter Name: ")
mark1=int(input("Enter First Mark: "))
mark2=int(input("Enter Second Mark: "))
mark3=int(input("Enter Third Mark: "))
average=(mark1+mark2+mark3)/3
print('')
if average >=80 and average <=100:
    grade='A'
    comment='Excellent'
elif average >=70:
    grade='B' 
    comment='Good'
elif average >=60:
    grade='C'
    comment='Good'
elif average >=50:
    grade='D'
    comment='IMPROVE!!!'
else:
    grade='F'
    comment='Fail!!!'
print('')
print(name)
print(f'Average is: {round(average,3)}')
print('Your Grade is: ',grade)
print(comment)

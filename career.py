name=input("Enter Name: ")
print('Please Select a Subject: ')
print('Math')
print('Science')
print('Art')
print('Business')
print('Home Science')
print('')
subject=input('Please Select a Subject: ')
print('')
if subject.lower() == 'math':
    comment = 'Data Analyst / Engineer'
elif subject.lower() == 'Science':
    comment = 'Lab Technician / Researcher'
elif subject.lower() == 'Art':
    comment = 'Designer / Animator'
elif subject.lower() == 'Business':
    comment = 'Marketer / Accountant'
elif subject.lower() == 'Home Science':
    comment = ' Catering & Accommodation'
else:
    comment = 'INVALID SUBJECT !!!'
    
print('Name Entered is: ',name)
print('Unit Selected: ',subject)
print('Your Career: ',comment)
print('')
print('YOUR CARRER IS THE BEST')
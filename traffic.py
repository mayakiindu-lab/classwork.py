vehicle=input("Enter Vehicles Number: ")
speed=int(input("Enter Speed: "))
if speed > 120:
    fine="15000"
elif speed >101:
    fine="7000"
elif speed >81:
    fine="3000"
else:
    fine='NO FINE'

print('Speed is: ',speed,' Km/h')
print(fine)
print('SPEED KILLS!!! PLEASE DRIVE SAFELY')



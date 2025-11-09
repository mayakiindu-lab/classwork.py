print("CAR ENGINE STATUS CHECKER")
print("_________________________")
enginetemperature=float(input("ENTER ENGINE TEMPERATURE IN DEGREES CELCIUS\n"))
oillevel=float(input("ENTER OIL LEVEL IN LITRES\n"))
battery=float(input("ENTER BATTERY VOLTAGE IN VOLTS\n"))
print("*************************")
print("INTELLIGENT FEEDBACK")
if enginetemperature<70:
    print("Engine temperature is LOW-allow the car to warm up")
elif enginetemperature>=70<100:
    print("Engine temperature is NORMAL")
elif enginetemperature>100:
    print("Engine temperature is HIGH — stop the car and check the cooling system")

if oillevel<2:
    print("Oil level is LOW — add more engine oil.")
elif oillevel>=2<=4:
    print("oil level is good")
elif oillevel>4:
    print("Oil level is TOO HIGH — reduce to recommended level")

if battery<12:
    print("Battery voltage is LOW — check your battery or alternator")
elif battery>=12<14.5:
    print("Battery voltage is NORMAL.")
elif battery>=14.5:
    print("Battery voltage is TOO HIGH — possible charging system issue")

else:
    print("ENTER VALID INPUTS!")

print("Engine check complete. Drive safely!")

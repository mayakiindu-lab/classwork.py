print("AI_BASED LOAN RECOMMENDER SYSTEM")
print("________________________________")
applicantname=input("enter applicant name\n")
fulizalimit=float(input("enter fulizalimit(KES)\n"))
monthlysalary=float(input("enter monthlysalary(KES)\n"))
CRBstatus=input("enter CRB status\n")

if fulizalimit>=10000:
    if monthlysalary>=50000:
        if CRBstatus=="not listed":
            loancategory="platinum loan"
            maxloanlimit="1000000"
            remarks="excellent borrower"
else:
    print("")

if 5000<= fulizalimit<=10000:
    if 30000<=monthlysalary<=50000:
        if CRBstatus=="not listed":
            loancategory="gold loan"
            maxloanlimit="500000"
            remarks="reliable borrower"
else:
    print("")

if fulizalimit<50000:
    if monthlysalary<30000:
        if CRBstatus=="not listed":
            loancategory="silver loan"
            maxloanlimit="100000"
            remarks="fair borrower"
else:
    print("")

if 5000<=fulizalimit>=10000:
    if 30000<=monthlysalary>=50000:
       if CRBstatus=="listed":
        loancategory="not eligible"
        maxloanlimit="0"
        remarks="CRB issue detected"
else:
    print("")

print("MESSAGE")
print("**************")
print("name:",applicantname)
print("fuliza limit:", fulizalimit)
print("salary:",monthlysalary)
print("CRBstatus:",CRBstatus)
print("loan category:",loancategory)
print("maximum loan limit:",maxloanlimit)
print("remarks:",remarks)

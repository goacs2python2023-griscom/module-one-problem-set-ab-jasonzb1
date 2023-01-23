def earlierdate (day1,month1,year1,day2,month2,year2):
    date1 = (day1, month1, year1)
    date2 = (day2, month2, year2)

    if date1 > date2:
        print("after")
    elif date1 == date2:
        print("same")
    else:
        print("before")
    
print(earlierdate(4,9,2002,4,9,2002))

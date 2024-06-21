year = int(input( "kakoi god?"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):
    print("vusokosnui")
else:
    print("obuchnyi")



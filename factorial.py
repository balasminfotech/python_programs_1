num=int(input("Enter a number: "))
factorial=1
if num <0:
    print("factorial does not exists for negative")
elif num==0:
    print("Factrial for 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factoriaal of is ;" , factorial)

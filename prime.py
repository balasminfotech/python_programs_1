num=int(input("Enter a number: "))
count=0
if num >1:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
    if count==2:
        print("Number is a prime number")
    else:
        print("number is not a prime number")
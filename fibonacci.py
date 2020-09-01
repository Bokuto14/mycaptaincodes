a=int(input("Input the number of terms in the series"))
t1,t2=0,1
b=0
if a <= 0:
    print("Please enter a positive value")
elif a==1:
    print("Fibonacci series :",t1)
else:
    print("Fibonacci series: ")
    while b<a:
        print(t1)
        c=t1+t2
        t1=t2
        t2=c
        b+=1

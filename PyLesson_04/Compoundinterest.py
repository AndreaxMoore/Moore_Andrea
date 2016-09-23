def payment(R,P,N,T):
    return((P*(1+(R/N))**(N*T))/(12*T))

r = float(input("Please enter your interest rate: "))
p = float(input("Please enter your principal: "))
n = float(input("Please enter the number of times the loan is compounded per year: "))
t = float(input("Please enter the life of the loan(in years): "))
print("Your payment on the loan is $","{:5.2f}".format(payment(r,p,n,t)))
          

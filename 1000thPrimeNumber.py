#This program finds the thousnadth prime number
#Date 25/04/2016 08:40 am
notThousandth = True
count = 1
number = 3
print "prime number is ",2
while notThousandth:
    isPrime = True
    for j in range(2,number-1) :
        if number%j == 0:
            isPrime = False
            break
    if isPrime:
        print "prime number is ",number
        count += 1
        
    if count == 1000:
        notThousandth = False
        print "Thousnadth Prime number is:",number
    number+=1

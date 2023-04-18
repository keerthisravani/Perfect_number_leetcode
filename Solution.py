def checkPerfectNumber(num):
    result=0
    i=1
    if num==1:
        return False
    while i*i<=num:
        if num%i==0:
            result+=i
            if num//i!=i and num//i!=num:
                result+=(num//i)
        i+=1
    if result==num:
        return True
    else:
        return False
num=28
print(checkPerfectNumber(num))
                     

                        







    
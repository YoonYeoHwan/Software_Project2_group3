
num = int(input("Enter your number : "))

while num != -1 :
    sum = 1
    if num >= 0 :
        for mul in range(1,num+1) :
            sum *= mul
        print("%d! = %d" %(num,sum))
        num = int(input("Enter your number : "))
    else :
        print("정수를 입력해주세요!")
        num = int(input("Enter your number : "))
INPUT =1
while INPUT !=0 :
    INPUT = int(input("숫자 입력 :: "))
    i=2
    while True:
        if(INPUT%i == 0):
            break
        i +=1
    if(i == INPUT):
        print("소수 입니다.")
    else:
        print("소수가 아닙니다.")

print("종료 합니다.")
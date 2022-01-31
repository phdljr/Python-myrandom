import random as r

list = [0, 0, 0, 0]

def gacha():
    num = r.random() #0.0~1.0
    if(num>=0.7):
        list[0]+=1
        return "레어"
    elif(0.4<=num<0.7):
        list[1]+=1
        return "에픽"
    elif(0.04<=num<0.4):
        list[2]+=1
        return "유니크"
    else:
        list[3]+=1
        return "레전더리"

count = 0
print("==========시작===========")
while True:
    count+=1
    result = gacha()
    print(result)
    if(result == ""):
        print("출력 횟수 : ", count)
        print("통계 : " , list)
        break;
    
    

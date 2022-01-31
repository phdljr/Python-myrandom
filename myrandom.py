import random as r

d = {"레어":0, "에픽":0, "유니크":0, "레전더리":0}

def gacha():
    num = r.random() * 100 #0.0~100.0
    if(num>=8.0):
        d["레어"]+=1
        return "레어"
    elif(1.7<=num<8.0):
        d["에픽"]+=1
        return "에픽"
    elif(0.2<=num<1.7):
        d["유니크"]+=1
        return "유니크"
    else:
        d["레전더리"]+=1
        return "레전더리"

count = 0
print("==========시작===========")
while True:
    count+=1
    result = gacha()
    print(result)
    if(result == ""):
        print("출력 횟수 : ", count)
        print("통계 : " , d)
        break;
    
    

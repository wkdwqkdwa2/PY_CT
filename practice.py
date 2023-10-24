cabinet={3:"유재석",100:"김태호"}
#키값을 통해 데이터에 접근하는 예
print(cabinet.get(3))

#값 추가하는 방법
cabinet["C-20"]=100
#값 삭제하는법
del cabinet[3]
#해당 키값이 없는 경우 바로 아래 있는 양식은 오류를 출력하며, 종료가 되지만 get함수를 이용한 문장은 None을 출력한다
#print(cabinet[5])
print(cabinet.get(5))
#만약 키값이 없다면 출력할 문장 설정 가능
print(cabinet.get(6,"사용가능"))

star=["정광희",'앙잉우','문문']
for customer in star:
    print("{0},안녕".format(customer))

from random import *
cnt=0
for i in range(1,51):
    time=randrange(5,51)
    if 5<=time<=15:
        print("[O] {0}번째 손님 (소요시간:{1})".format(i,time))
        cnt+=1
    else:
        print("[ ] {0}번째 손님 (소요시간:{1})".format(i,time))

print("탑승자는{0}명입니다.".format(cnt))

scores={"수학":0,"영어":50,"코딩":100}
for a,b in scores.items():
    print(a,b)
#format함수 다양한 방법으로 값 넣기 및 응용법
print("내 나이:{age} 이름:{name}".format(age=20, name="빨간"))
 
for a in range(2,4):
    for b in range(1,10):
        print('{0} *{1}={2:2}'.format(a,b,a*b))

#문자열
subway=["유재석","조세호","박명수"]
#인덱스값 출력
print(subway.index("조세호"))
#맨뒤에 입력
subway.append("하하")
#해당 위치에 입력
subway.insert(1,"정형돈")
#맨뒤에 있는 값 삭제
subway.pop()
#해당 데이터 개수 확인하기
subway.count("유재석")
#정렬기능
num_list=[5,2,4,3,1]
num_list.sort()
#순서뒤집기
num_list.reversee()
#모두 삭제
num_list.clear()

#배열 합치기
one_lsit=[5,2,4,3,2,1]
two_list=["조세호",20,True]
one_lsit.extend(two_list)

#문자열 같은 경우 불변한 성질을 가지기 때문에 수정을 원한다면 리스트로 변환해줘야함.
s = "Naze"
l = list(s)
l[2] = "m"
s = "".join(l)
print(s)
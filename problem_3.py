# 재현이는 알파벳 소문자로 이루어진 문자열 하나를 받아 그대로 두 번 연달아 썼다. 예를 들어 “abc” 를 받았다면 “abcabc” 를 썼다.
# 당신에게 문자열이 주어질 때, 이 문자열이 재현이가 만들어 낼 수 있는 문자열인지 판단하라.
T=int(input())

for test_case in range(T): 
    c_len=int(input())
    ck=0
    a=input()
    for le in range(c_len): #입력받은 문자열의 길이만큼 반복문 재생하며, b와 c가 딱 한번만 같아야 조건이 충족해지는 것을 응용, 왜냐하면 재현이는 두 번만 연달아 쓰기 때문.
         b=a[:le]
         c=a[le:]
         if(b==c):
              ck+=1
    if(ck==1):
         print("#{0}".format(test_case+1),"Yes")
    else:
         
         print("#{0}".format(test_case+1),"No")
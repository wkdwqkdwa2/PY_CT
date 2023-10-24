n = int(input())
 
li = []
for _ in range(n):
    age, name = input().split()
    li.append([int(age),name])

print(li) 
li.sort(key=lambda x:x[0]) #sort함수는 정렬해주는 함수이며, key는 함수호출, lambda는 익명의 함수이다. 즉x[0]을 기준으로 정렬하라는 의미.
 
for i in li:
    print(i[0],i[1])
n = int(input())
 
li = []
for _ in range(n):
    age, name = input().split()
    li.append([int(age),name])

print(li) 
li.sort(key=lambda x:x[0])
 
for i in li:
    print(i[0],i[1])
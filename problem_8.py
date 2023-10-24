# 어린 성훈이는 알파벳 공부를 하고 있어서, 몇 개의 알파벳을 적었다. 성훈이가 적은 알파벳을 순서대로 보면서 앞에서부터 몇 개의 알파벳이 순서에 맞게 적혀 있는지 구하는 프로그램을 작성하라.
# 단, 순서는 a부터 순서대로 일치하는 알파벳 개수를 계산하여야 한다.


T=int(input())
spel='abcdefghijklmnopqrstuvwxyz'
for tc in range(T):
    in_spel=input()
    i=0
  
    for in_len in range(len(in_spel)):
        if spel[i]==in_spel[i]:
            i+=1
            
    print("#{} {}".format(tc+1, i))
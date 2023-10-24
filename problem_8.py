T=int(input())
spel='abcdefghijklmnopqrstuvwxyz'
for tc in range(T):
    in_spel=input()
    i=0
  
    for in_len in range(len(in_spel)):
        if spel[i]==in_spel[i]:
            i+=1
            
    print("#{} {}".format(tc+1, i))
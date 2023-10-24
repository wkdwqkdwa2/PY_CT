T=int(input())

for test_case in range(T):
    c_len=int(input())
    ck=0
    a=input()
    for le in range(c_len):
         b=a[:le]
         c=a[le:]
         if(b==c):
              ck+=1
    if(ck==1):
         print("#{0}".format(test_case+1),"Yes")
    else:
         
         print("#{0}".format(test_case+1),"No")
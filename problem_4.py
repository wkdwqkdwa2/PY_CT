T=int(input())

for test_case in range(T):
    A,B=input().split()
    B=int(B)
    A = list(map(int, A))
    for b in range(B):
        index=0
        for c in range(b+1, len(A)):            
            if(A[index]<=A[c]):
                index=c

        A[index], A[b]=A[b],A[index]
    result  = ''.join(map(str, A))
    print("#{0}".format(test_case + 1), result )
    
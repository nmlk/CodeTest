A = [6,1,4,6,3,2,7,4]
K = 3
L = 2

def helper(A,K,L):
    A1 = [float('-inf')]*len(A)
    A2 = [float('-inf')]*len(A)
    
    max1 = float('-inf')
    max2 = float('-inf')
    
    for i in range(len(A)):
        if i >= K:
            max1 = max(max1,sum(A[i-K:i]))
            A1[i] = max1
            
        if i <= len(A)-L:
            max2 = max(max2,sum(A[-(i+L):-i or None]))
            A2[-(i+L)] = max2
    
    A12 = [sum(x) for x in zip(A1, A2)]
    
    return max(A12)


m1 = helper(A,K,L)
A.reverse()
m2 = helper(A,K,L)

print max(m1, m2)

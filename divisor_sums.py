def div_sum(n,a,b):
    if a>b: return 0
    N1 = n//a
    N2 = n//N1

    return N1*(N2-a+1)+div_sum(n,N2+1,b)

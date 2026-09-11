def pontencia(a,b):
    if b==0:
        return 1
    else:
        return a*pontencia(a,b-1)
print(pontencia(2,3))
print(pontencia(5,0))
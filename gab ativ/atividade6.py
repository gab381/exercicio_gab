def soma_recursiva(n):
    if n == 1:
        return 1
    else:
        return n + soma_recursiva(n - 1)
def media_n(n):
    if n <= 0:
        return 0
    return soma_recursiva(n) / n
print(media_n(5))
print(media_n(10))
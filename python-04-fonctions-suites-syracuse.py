def syracuse(n):
    d = deja_fait
    tv = 0
    tva = 0
    u0 = n
    am = u0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        tv = tv + 1

        if am < n:
            am = n
        if d:
        if n < u0:
            tva = tv - 1
            d = False
     return tv,am, tva   



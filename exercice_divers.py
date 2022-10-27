import math

def premier_diviseur(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return i
        i += 1
    return n


def test_premier_diviseur() :
    try :
        assert(premier_diviseur(1) == 1)
        assert(premier_diviseur(2) == 2)
        assert(premier_diviseur(1000) == 2)
        assert(premier_diviseur(1001) == 7)
        assert(premier_diviseur(1005150) == 2)
        print("premier_diviseur : OK")
    except :
        print("premier_diviseur : ERREUR")
        
#test_premier_diviseur()


def aire_rectangle(a, b):
    return a * b


def test_aire_rectangle() :
    try :
        assert(aire_rectangle(1, 1) == 1)
        assert(aire_rectangle(2, 2) == 4)
        assert(aire_rectangle(1000, 1000) == 1000000)
        assert(aire_rectangle(1001, 1001) == 1002001)
        print("aire_rectangle : OK")
    except :
        print("aire_rectangle : ERREUR")
        
#test_aire_rectangle()

def aire_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def test_aire_triangle() :
    try :
        # Il faut éviter de comparer des float avec ==
        assert (aire_triangle(1, 1, 1) > 0.43 and aire_triangle(1, 1, 1) < 0.44)
        assert (aire_triangle(2, 2, 2) > 1.73 and aire_triangle(2, 2, 2) < 1.74)
        assert (aire_triangle(1000, 1000, 1000) > 433012.70 and aire_triangle(1000, 1000, 1000) < 433012.71)
        print("aire_triangle : OK")
    except :
        print("aire_triangle : ERREUR")

#test_aire_triangle()



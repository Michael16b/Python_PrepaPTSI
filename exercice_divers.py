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


def reverse(s):
    return s[::-1]


def test_reverse() :
    try :
        assert(reverse("abc") == "cba")
        assert(reverse("abcde") == "edcba")
        assert(reverse("123456789") == "987654321")
        print("reverse : OK")
    except :
        print("reverse : ERREUR")

#test_reverse()

def palindrome(s):
    return s == reverse(s)

def test_palindrome() :
    try :
        assert(palindrome("abc") == False)
        assert(palindrome("abcba") == True)
        assert(palindrome("123456789") == False)
        assert(palindrome("123454321") == True)
        print("palindrome : OK")
    except :
        print("palindrome : ERREUR")

#test_palindrome()


def divise(p,n) :
    val = p
    while (val < n) :
        val = val + p
    if (val == n) :
        return True
    else :
        return False


def test_divise() :
    try :
        assert(divise(2, 1) == False)
        assert(divise(2, 2) == True)
        assert(divise(2, 3) == False)
        assert(divise(2, 4) == True)
        assert(divise(2, 5) == False)
        assert(divise(2, 6) == True)
        print("divise : OK")
    except :
        print("divise : ERREUR")

test_divise()
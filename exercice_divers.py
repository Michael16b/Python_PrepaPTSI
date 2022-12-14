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

#test_divise()


#Calcul de somme factorielle

def fact(n) :
    if (n == 0) :
        return 1
    else :
        return n * fact(n-1)
    
def somme2(n) :
    somme = 0
    for i in range(1, n + 1) :
        somme = somme + fact(i)
    return somme

def test_sommefact() :
    try :
        assert(somme2(1) == 1)
        assert(somme2(2) == 3)
        assert(somme2(3) == 9)
        assert(somme2(4) == 33)
        assert(somme2(5) == 153)
        assert(somme2(6) == 873)
        print("somme2 : OK")
    except :
        print("somme2 : ERREUR")
        
#test_sommefact()


def max_pentepos(L) :
    if (len(L) < 1) :
        return L
    pentePos = [L[0]]
    for i in range(1,len(L)):
        if (L[i] > pentePos[-1]) :
            pentePos.append(L[i])
    return pentePos

def test_max_pentepos() :
    try :
        assert(max_pentepos([1,2,3,4,5]) == [1,2,3,4,5])
        assert(max_pentepos([1,2,3,4,5,4,3,2,1]) == [1,2,3,4,5])
        assert(max_pentepos([1,2,3,4,5,4,3,2,1,2,3,4,5]) == [1,2,3,4,5])
        assert(max_pentepos([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9,10])
        print("max_pentepos : OK")
    except :
        print("max_pentepos : ERREUR")
        
#test_max_pentepos()

def maxpente(L) :
    if (len(L) < 1) :
        return L
    pente = [L[0]]
    pentePos = False # False si la pente est négative, True si la pente est positive
    if (L[1] > L[0]) :
        pentePos = True
    else :
        pentePos = False
    for i in range(1,len(L)):
        if (L[i] > pente[-1] and pentePos == True) :
            pente.append(L[i])
        elif(L[i] < pente[-1] and pentePos == False) :
            pente.append(L[i])
    return pente


def test_maxpente() :
    try :
        assert(maxpente([1,2,3,4,5]) == [1,2,3,4,5])
        assert(maxpente([5,4,3,2,1]) == [5,4,3,2,1])
        assert(maxpente([1,2,3,4,5,4,3,2,1]) == [1,2,3,4,5])
        assert(maxpente([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]) == [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1])
        print("maxpente : OK")
    except :
        print("maxpente : ERREUR")


#test_maxpente()

def checkPQ(p,q) :
    return (p > 0 and q > 0 and p < q)


# Doit renvoyer le plus petit rationnel n tel que 1/n <= p/q
def minRationnel(a,b) :
    if (checkPQ(a,b) == False) :
        return None
    n = 1
    while (1/n > a/b) :
        n = n + 1
    return n



# A Ameliorer
def test_minRationnel() :
    try :
        assert(minRationnel(1,2) == 2)
        assert(minRationnel(1,3) == 3)
        assert(minRationnel(10, 100) == 10)
        assert(minRationnel(1, 100) == 100)
        print("minRationnel : OK")
    except :
        print("minRationnel : ERREUR")


#test_minRationnel()
    
def pgcd(a,b) :
    if (a == 0) :
        return b
    elif (b == 0) :
        return a
    else :
        return pgcd(b, a % b)

def test_pgcd() :
    try :
        assert(pgcd(0,0) == 0)
        assert(pgcd(0,1) == 1)
        assert(pgcd(1,0) == 1)
        assert(pgcd(1,1) == 1)
        assert(pgcd(18,2) == 2)
        assert(pgcd(2,20) == 2)
        assert(pgcd(20,2) == 2)
        assert(pgcd(2,22) == 2)
        assert(pgcd(2,28) == 2)
        assert(pgcd(28,2) == 2)
        assert(pgcd(2,30) == 2)
        assert(pgcd(30,2) == 2)
        assert(pgcd(2,32) == 2)
        print("pgcd : OK")
    except :
        print("pgcd : ERREUR")
        
#test_pgcd()

def soustractionRationnel(a,b,c,d) :
    if (checkPQ(a,b) == False or checkPQ(c,d) == False) :
        return None
    if (b == d and a == c) :
        return [0,1]
    num1 = a*d 
    num2 = c*b 
    denoCommun = b*d 
    numDiff = num1-num2
    return [numDiff,denoCommun]

# A Ameliorer - Cas de test a ajouter
def test_soustractionRationnel() :
    try :
        assert(soustractionRationnel(1,2,1,2) == [0,1])
        assert(soustractionRationnel(1,2,1,3) == [1,6])
        assert(soustractionRationnel(1,2,1,4) == [2,8])
        assert(soustractionRationnel(1,2,1,5) == [3,10])
        print("soustractionRationnel : OK")
    except :
        print("soustractionRationnel : ERREUR")
        
test_soustractionRationnel()


def fractionEgyptienne(p, q):
    if (checkPQ(p,q) == False) :
        return []
    a,b = p,q
    liste = []
    while b % a != 0:
        m = b // a + 1
        liste.append(m)
        a = a * m - b
        b = b * m
    liste.append(b // a)
    return liste



# Ne fonctionne pas bien !
def test_fractionEgyptienne() :
    try :
        assert(fractionEgyptienne(1,2) == [2])
        assert(fractionEgyptienne(1,3) == [3])
        assert(fractionEgyptienne(1,4) == [4])
        assert(fractionEgyptienne(1,5) == [5])
        print("fractionEgyptienne : OK")
    except :
        print("fractionEgyptienne : ERREUR")

#test_fractionEgyptienne()
import time
import math
import re
import string
import itertools
import copy
##Project Euler #1


##print(sum([x for x in range(1000) if x%3==0 or x%5==0]))
##


##Project Euler #2

##def fib(n):
##	if n < 3:
##		return n
##	return fib(n-1)+fib(n-2)

##print( sum ([fib(x) for x in range(33) if fib(x) % 2 == 0]) )

##25

##def fib_len(n):
##    minus1=1
##    currentfib=2
##    oldfib = 0
##    term=3
##    while len(str(currentfib)) < n:
##        oldfib = currentfib
##        currentfib = currentfib + minus1
##        minus1 = oldfib
##        term+=1
##    return term
##
##start = time.clock()
##fib_len(1000)
##stop = time.clock()
##print (stop-start)

##Project Euler #3
##
##import math
##
##num = 600851475143
##
##
##def factor_list(n):
##    root = int(math.sqrt(n))
##    small_factors = [i for i in range(2, root + 1) if n%i == 0]
##    large_factors = [n/i for i in smallfactors]
##    return small_factors + large_factors
##
##def check_prime(n):
##    for i in factor_list(n):
##        if n%i == 0:
##            return False
##    return True
##
##print ( max ( [i for i in factor_list(num) if check_prime(i)]) )


##Project Euler #4



##print ( max ( i*k for i in range(100,1000) for k in range(100,1000) if str(i*k)==str(i*k)[::-1]) )



##Project Euler #5

##num = 2520
##

##
##def smallest_multiple(n):
##    factor = 2
##    num = 2
##    step = 2
##    while factor <= n:
##        if num % factor == 0:
##            factor+=1
##            step = num
##        else:
##            num+=step
##    return num
##
##start = time.clock()
##smallest_multiple(20)
##end = time.clock()
##print (end-start)

##
##print (num)


##Project Euler #6

##num= 100
##
##def sum_of_squares(n):
##    return sum ( [x**2 for x in range(n+1)] )
##
##def natural_sum_squared(n):
##    return (sum( [x for x in range(n+1)]))**2
##
##print ( (natural_sum_squared(num) - sum_of_squares(num) ) )
##
##
##print ( (sum( [x for x in range(101)]))**2 - sum ( [x**2 for x in range(101)] ) )
##


##Project Euler #7


##def factor_list(n):
##    root = int(math.sqrt(n))
##    small_factors = [i for i in range(2, root + 1) if n%i == 0]
##    large_factors = [n/i for i in small_factors]
##    return small_factors + large_factors
##
##def check_prime(n):
##    for i in factor_list(n):
##        if n%i == 0:
##            return False
##    return True
##
##def nth_prime(n):
##    found = 0
##    test = 2
##    while found < n:
##        if check_prime(test):
##            found+=1
##            test+=1
##        else:
##            test+=1
##    return test-1
##
##print(nth_prime(10001))
##

##Project Euler #8

##numstr = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
##
##
##def largest_product(numstr,consecutive_numbers):
##    largest = 0
##    testindex = 0
##    while testindex+consecutive_numbers < len(numstr):
##        result = 1
##        for i in range (0,consecutive_numbers):
##            result *= int(numstr[testindex+i])
##        if result > largest:
##            largest = result
##        testindex += 1
##    return largest
##
##
##print ( largest_product(numstr,5) )


##48

##def self_powers_sum(n):
##    return sum ([i**i for i in range(1,n+1)])
##
##print ( self_powers_sum(1000) )


##20

##print ( sum ([int(x) for x in str(math.factorial(100))]) )
##
##


##16

##sum(map(int,str(2**1000)))
##


##13

##
##f = open('PE13.txt')
##numlist = [line.strip() for line in f]
##f.close()
##
##print (numlist)
##
##print (sum(map(int,numlist)))
##
##print (str(sum(map(int,numlist)))[0:10])


##9


##for a in range(1,1000):
##  for b in range(a+1,1+1000-a):
##    c = 1000-(a+b)
##    if a**2 + b**2 == c**2:
##      print (a*b*c, a, b, c)


##11

##print (89*94*97*87)
##
##f = open('PE11.txt')
##numlist = [line.strip() for line in f]
##f.close()
##grid = [x.split() for x in numlist]
##
##



##10
##
##def prime_sum(n):
##    primelist = [2,3,5,7]
##    for num in range(8,n):
##        for prime in primelist:
##            if num % prime == 0:
##                break
##            if prime > math.sqrt(num)+1:
##                primelist.append(num)
##                break
##        else:
##            primelist.append(num)
##    return sum(primelist), len(primelist)
##





###14
##

##
##def longest_collatz(n):
##    colltaz_dict= {1:1}
##    longestlen = 1
##    longeststart=1
##    for i in range(2,n):
##        current = i
##        length = 1
##        while current != 1:
##            if current in colltaz_dict:
##                length+=colltaz_dict[current]
##                break
##            if current%2 ==0:
##                current=current/2
##            else:
##                current=current*3+1
##            length+=1
##        colltaz_dict[i] = length
##        if length > longestlen:
##            longestlen = length
##            longeststart = i
##    return longeststart, longestlen
##
##
##print (longest_collatz(1000000))

##12


##def find_divisors(n):
##    divcount=2
##    for i in range(2,int(math.sqrt(n))+1):
##        if n%i == 0:
##            if i == math.sqrt(n):
##                divcount+=1
##            else:
##                divcount+=2
##    return divcount
##
##
##def first_triangle_divisors(n):
##    mostdivisors = 0
##    currenttest = 3
##    prevtest= 0
##    nextplus=3
##    while mostdivisors < n:
##        divcount = find_divisors(currenttest)
##        if divcount > mostdivisors:
##            mostdivisors = divcount
##        prevtest = currenttest
##        currenttest=currenttest+nextplus
##        nextplus+=1
##    return prevtest
##
##print(first_triangle_divisors(501))



##36

##def dual_palindrome_sum(n):
##    base10_palindromes = [x for x in range(n+1) if (str(x))==str(x)[::-1]]
##    base2_union = [x for x in base10_palindromes if str(bin(x))[2:] == str(bin(x))[:1:-1]]
##    print(sum(base2_union))
##
##


##34

##
##bound = 9
##while bound < math.factorial(9)*(len(str(bound))):
##    bound = int(str(bound)+"9")
##
##def digit_factorials(bound):
##    digitfactorials= []
##    for i in range (3,bound):
##        numlist= [int(x) for x in str(i)]
##        summ =sum([math.factorial(x) for x in numlist])
##        if i == summ:
##            digitfactorials.append(i)
##    return sum(digitfactorials)
##
##print (digit_factorials(100000))
##
##
##print (sum([x for x in range(3,2540161) if sum(math.factorial(int(d)) for d in str(x)) == x]) )



##30
##
##def digit_n_powers(n):
##    powersdict = {key:value for key, value in zip([str(x) for x in range(10)],[x**n for x in range(10)])}
##    nums =[i for i in range (2,300000) if sum([powersdict[x] for x in str(i)]) == i]
##    return sum(nums), nums
##

##38
##
##
##largest = "918273645"
##for x in range (1,10000):
##    concat = str(x)
##    multiplier = 2
##    while len(concat) <= 9:
##        if len(concat) == 9:
##            if len([x for x in largest if x in concat])==9:
##                print (concat)
##                if int(concat) > int(largest):
##                    largest = concat
##                    break
##                else:
##                    break
##            else:
##                break
##        else:
##            concat+=(str(x*multiplier))
##            multiplier+=1
##
##print (largest)


##21

##def find_proper_divisors(n):
##    divlist= [x for x in range(2,int(math.sqrt(n))) if n%x==0]
##    divlist = [1]+divlist+[n/x for x in divlist if x != math.sqrt(n)]
##    return divlist
##
##def find_amicable_nums_sum(n):
##    divsorsums={key:value for key, value in zip([x+1 for x in range(n)],[sum(find_proper_divisors(x+1)) for x in range(n)])}
##    amicablenums = [x for x in range(1,n+1) if divsorsums[x] <=n and divsorsums[divsorsums[x]] == x and divsorsums[x] != x]
##    return sum(amicablenums)
##
##print (find_amicable_nums_sum(10000))




##23

##def find_proper_divisors(n):
##    divlist= [x for x in range(2,int(math.sqrt(n))+1) if n%x==0]
##    divlist = [1]+divlist+[int(n/x) for x in divlist if x != math.sqrt(n)]
##    return divlist
##
##def find_nonabundantsumints(n):
##    abundantnums = [x for x in range (12,n) if sum(find_proper_divisors(x))>x]
##    total = 0
##    for x in range(0,n):
##        test= True
##        for i in abundantnums:
##            if i > x:
##                break
##            if x-i in abundantnums:
##                test= False
##                break
##        if test == True:
##            total+=x
##    return total


####17
##
##numdict ={key:value for key, value in zip([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90],
##                                          [3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8,6,6,5,5,5,7,6,6,])}
##
##total= 11
##for x in range(1,1000):
##    digits=len(str(x))
##    if digits == 1:
##        total+=numdict[x]
##    if digits == 2:
##        if str(x)[0]=="1" or str(x)[1]=="0":
##            total+=numdict[x]
##        else:
##            total+=numdict[int(str(x)[0]+"0")]+numdict[int(str(x)[1])]
##    if digits ==3:
##        total+=7+numdict[int(str(x)[0])]
##        if str(x)[1]=="1":
##            total+=3+numdict[int(str(x)[1:])]
##        elif str(x)[2]=="0" and str(x)[1]!="0":
##            total+=3+numdict[int(str(x)[1]+"0")]
##        elif str(x)[1]!="0":
##            total+=3+numdict[int(str(x)[1]+"0")]+numdict[int(str(x)[2])]
##        elif str(x)[1]=="0" and str(x)[2]!="0":
##            total+=3+numdict[int(str(x)[2])]
##
##print(total)


##22

##f = open('names.txt')
##names = f.read()
##f.close()
##
##namelist = sorted(re.findall(r'[A-Z]+',names))
##alphavalues = {key:value for key, value in zip(string.ascii_uppercase,[x for x in range(1,27)])}
##
##total = 0
##for name in range(0,len(namelist)):
##    namevalue=0
##    for letter in namelist[name]:
##        namevalue+=alphavalues[letter]
##    total+=(namevalue*(name+1))
##print(total)


##24
##
##sibs = [x for x in itertools.permutations("0123456789",10)]
##print ("".join(possibs[999999]))


##15

##recursive solution
##def latticerec(n):
##    if n==1:
##        return 2
##    return 2*(latticerec(n-1)+(((n-1)/n)*latticerec(n-1)))
##
##def lattice(n):
##    latticevals = {1:2}
##    for x in range (2,n+1):
##        latticevals[x] = (2*(latticevals[x-1]+(((x-1)/x)*latticevals[x-1])))
##    return latticevals[n]


##19

##months = {key:val for key,val in zip([x for x in range(1,13)],[31,28,31,30,31,30,31,31,30,31,30,31])}
##days= {key:val for key,val in zip([x for x in range(1,8)],["mon","tues","wed", "thurs", "fri", "sat", "sun"])}
##
##firstsundays = 0
##dayofweek = 1
##current = [1,1,1900]
##stop = [31,12,2000]
##
##while current != [31,12,2000]:
##    if current[2] >=1901:
##        if days[dayofweek] == "sun" and current[0] ==1:
##            firstsundays+=1
##    if days[dayofweek] == "sun":
##        dayofweek = 1
##    else:
##        dayofweek+=1
##    if (current[2])%4 == 0 and current[2] != 1900:
##        months[2]=29
##    else:
##        months[2]=28
##    if current[0]==31 and current[1]==12:
##        current[2]+=1
##    if current[0] == months[current[1]]:
##        if current[1] ==12:
##            current[1]=1
##        else:
##            current[1]+=1
##        current[0]=1
##    else:
##        current[0]+=1
##
##print (firstsundays)


####18,67
##
##f = open('triangle.txt')
##tri = f.read()
##f.close()
##
##
####tri='''75
####95 64
####17 47 82
####18 35 87 10
####20 04 82 47 65
####19 01 23 75 03 34
####88 02 77 73 07 63 67
####99 65 04 28 06 16 70 92
####41 41 26 56 83 40 80 70 33
####41 48 72 33 47 32 37 16 94 29
####53 71 44 65 25 43 91 52 97 51 14
####70 11 33 28 77 73 17 78 39 68 17 57
####91 71 52 38 17 14 91 43 58 50 27 29 48
####63 66 04 68 89 53 67 30 73 16 69 87 40 31
####04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''
##numlists = [x.split(" ") for x in tri.split("\n")][::-1]
##if len(numlists) >20:
##    del(numlists[0])
##for l in range(len(numlists)):
##    for n in range (len(numlists[l])):
##        numlists[l][n]= int(numlists[l][n])
##
##
##def absorb_list(list1, list2):
##    for num in range (0, len(list1)):
##        if list2[num] >= list2[num+1]:
##            list1[num]+=list2[num]
##        else:
##            list1[num]+=list2[num+1]
##
##for l in range (0,len(numlists)-1):
##    absorb_list(numlists[l+1], numlists[l])
##
##print (numlists[-1])
##
##
####print (75+64+82+87+82+75+73+28+83+32+91+78+58+73+93)


##26

## can't make long enough floats


##possibs = [(str(x)[2:][::-1]).strip("0") for x in [1/n for n in range (2,1000)]]
##
##largestnum=7
##largestcycle=6
##
##def occurrences(string, sub):
##    count = start = 0
##    while True:
##        start = string.find(sub, start) + 1
##        if start > 0:
##            count+=1
##        else:
##            return count
##for x in range(275, len(possibs)):
##    if len(possibs[x]) < largestcycle*2:
##        continue
##    while True:
##        teststr = possibs[x][1:(largestcycle+2)]
##        print(teststr)
##        print(possibs[x])
##        count1 = occurrences(possibs[x], teststr)
##        count2 = possibs[x].count(teststr)
##        print(count1)
##        print(count2)
##        if count1 > 2:
##            break
##        if count2 == 2:
##            largestnum = x+2
##            largestcycle+=1
##        else: break
##
##print(largestnum,largestcycle)


##stole solution online

##def recurring_cycle(n, d):
##    # solve 10^s % d == 10^(s+t) % d
##    # where t is length and s is start
##    for t in range(1, d):
##        if 1 == 10**t % d:
##            return t
##    return 0
##
##longest = max(recurring_cycle(1, i) for i in range(2,1001))
##print ([i for i in range(2,1001) if recurring_cycle(1, i) == longest][0])




####27
##
##def factor_list(n):
##    root = int(math.sqrt(abs(n)))
##    small_factors = [i for i in range(2, root + 1) if n%i == 0]
##    large_factors = [n/i for i in small_factors]
##    return small_factors + large_factors
##
##def check_prime(n):
##    for i in factor_list(n):
##        if n%i == 0:
##            return False
##    return True
##
##def longest_prime_equation(n):
##    atimesb = 0
##    maxprimes = 0
##    amax=0
##    bmax=0
##    for a in range(-n+1,n):
##        for b in range(-n+1,n):
##            primecounter=0
##            while True:
##                if check_prime((primecounter**2)+(a*primecounter)+b):
##                    primecounter+=1
##                    if primecounter > maxprimes:
##                        maxprimes=primecounter
##                        atimesb=a*b
##                        amax=a
##                        bmax=b
##                else:
##                    break
##    return atimesb, maxprimes, amax, bmax
##
##
####slow but it worked (apparantely b can only be prime, which could cut down on runtime. My primeality testing functions are slow.)


##28

##def spiral_diagonals(n):
##    diagsum=1
##    currentconer=1
##    for x in range(1,int((n+1)/2)):
##        levelwidth=(x*2)
##        for c in range(0,4):
##            currentconer+=levelwidth
##            diagsum+=currentconer
##    return diagsum
##
##print (spiral_diagonals(1001))


###@29
##print (len(set([a**b for a in range (2,101) for b in range(2,101)])))


##31

##stole answer from this code----------------------

##coins = [1, 2, 5, 10, 20, 50, 100, 200]
##
##TARGET=200
##
##matrix = {}
##for y in range(0, TARGET+1):
##    # There is only one way to form a target sum N
##    # via 1-cent coins: use N 1-cents!
##    matrix[y, 0] = 1  # equivalent to matrix[(y,0)]=1
##
##for y in range(0, TARGET+1):
##    print (y, ":", 1,)
##    for x in range(1, len(coins)):
##        matrix[y, x] = 0
##        # Is the target big enough to accomodate coins[x]?
##        if y>=coins[x]:
##            # If yes, then the number of ways to form
##            # the target sum are obtained via:
##            #
##            # (a) the number of ways to form this target
##            #     using ONLY coins less than column x
##            #     i.e. matrix[y][x-1]
##            matrix[y, x] += matrix[y, x-1]
##            # plus
##            # (b) the number of ways to form this target
##            #     when USING the coin of column x
##            #     which means for a remainder of y-coins[x]
##            #     i.e. matrix[y-coins[x]][x]
##            matrix[y, x] += matrix[y-coins[x], x]
##        else:
##            # if the target is not big enough to allow
##            # usage of the coin in column x,
##            # then just copy the number of ways from the
##            # column to the left (i.e. with smaller coins)
##            matrix[y, x] = matrix[y, x-1]
##        print (matrix[y, x],)
##    print

##my code breaks down because I can't figure out how to make it account for remanders ie coin 20
####does go evenly into coin 50
##
##def pence2(n):
##    return 1 + n//2
##
##def pence5(n):
##    return sum([pence2(x) for x in [y*5 for y in range(1,(n//5)+1)]])+1
##
##def pence10(n):
##    return sum([pence5(x) for x in [y*10 for y in range(1,(n//10)+1)]])+1
##
##def pence20(n):
##    calls=0
##    summ = sum([pence10(x) for x in [y*20 for y in range(1,(n//20)+1)]])+1
##
##
##def pence50(n):
##    return sum([pence20(x) for x in [y*50 for y in range(1,(n//50)+1)]])+1
##
##def pence100(n):
##    return sum([pence50(x) for x in [y*100 for y in range(1,(n//100)+1)]])+1
##
##def pence200(n):
##    return sum([pence100(x) for x in [y*200 for y in range(1,(n//200)+1)]])+1
##
##print(pence200(200))



##40

##constant= ""
##counter = 1
##while len(constant)<1000000:
##    constant+=str(counter)
##    counter+=1
##nums = [constant[(10**x)-1] for x in range(0,7)]
##tot=1
##for i in nums:
##    tot*=int(i)
##print(tot,nums)

##works but pretty slow brute force


##42

##f = open('PE42.txt')
##words = re.findall(r"[A-Z]+",f.read())
##f.close()
##
##alphavalues = {key:value for key, value in zip(string.ascii_uppercase,[x for x in range(1,27)])}
##trianglenums = [int((n/2)*(n+1)) for n in range(1,20)]
##wordvals = []
##for word in words:
##    val = 0
##    for letter in word:
##        val+=alphavalues[letter]
##    wordvals.append(val)
##
##print (len([x for x in wordvals if x in trianglenums]))
####Code for timing


##45

##
##
##trianglenums = set(int((n/2)*(n+1)) for n in range(1,100000))
##pentnums = set(int((n/2)*(3*n-1)) for n in range(1,100000))
##hexnums = set(int((n)*(2*n-1)) for n in range(1,100000))
##print(trianglenums.intersection(pentnums).intersection(hexnums))
##

##35

##def isprime(n):
##    root = int(math.sqrt(n))
##    for i in range(2, root + 1):
##        if n%i == 0:
##            return False
##    return True
##
##primes = set(x for x in range(10,1000000) if isprime(x))
##circular = [2, 3, 5, 7]
##
##for p in primes:
##    if "0" in str(p):
##        continue
##    rotations = len(str(p))-1
##    rotate=int(str(p)[1:]+str(p)[0])
##    while rotations > 0:
##        if rotate in primes:
##            if rotations == 1:
##                circular.append(p)
##                break
##            else:
##                rotate=int(str(rotate)[1:]+str(rotate)[0])
##                rotations-=1
##        else:
##            break
##
##print (len(circular))


##33
##
##digitcancels= []
##for x in range (11,50):
##    for y in range (11,100):
##        if "0" in str(x) or "0" in str(y):
##            continue
##        if x==y:
##            continue
##        num1tens= str(x)[0]
##        num1ones= str(x)[1]
##        num2tens= str(y)[0]
##        num2ones= str(y)[1]
##        if num1tens not in str(y) and num1ones not in str(y):
##            continue
##        if num1tens == num2ones and x/y == int(num1ones)/int(num2tens):
##            digitcancels.append((x,y))
##        if num2tens == num1ones and x/y == int(num1tens)/int(num2ones):
##            digitcancels.append((x,y))
##
##numerator = 16*19*26*49
##denominator = 64*65*95*98
##print(numerator/denominator)

##37

##def isprime(n):
##    root = int(math.sqrt(n))
##    for i in range(2, root + 1):
##        if n%i == 0:
##            return False
##    return True
##
##primes = set(x for x in range(2,1000000) if isprime(x))
##
##truncatable = []
##
##for p in primes:
##    length=len(str(p))
##    if length < 2:
##        continue
##    for x in range(length-1):
##        if int(str(p)[(x+1):]) in primes and int(str(p)[:(-x)-1]) in primes:
##            if x==length-2:
##                truncatable.append(p)
##        else:
##            break
##
##print(sum(truncatable))


##39


##maxsolutions=0
##val = 0
##for x in range (5,1000):
##    solutions=0
##    for a in range (1,x//2):
##        for b in range (2,x//2):
##            if a<b:
##                if math.sqrt(a**2+b**2)+a+b == x:
##                    solutions+=1
##                    if solutions > maxsolutions:
##                        maxsolutions = solutions
##                        val = x
##
##print (maxsolutions, val)


##32


##pandigital_products = []
##digits= [str(x) for x in range (1,10)]
##
##for x in range (1,100):
##    for y in range(1,2000):
##        if sorted(str(x)+str(y)+str(x*y))==digits:
##            pandigital_products.append(x*y)
##
##print (sum(set(pandigital_products)))


##print (sum(set(x*y for x in range(1,100) for y in range(1,2000) if sorted(str(x)+str(y)+str(x*y))==[str(x) for x in range (1,10)])))


##46

##squareslist = sorted(set(2*(x**2) for x in range (1,100)))
##
##def isprime(n):
##    for i in range(2, int(math.sqrt(n)) + 1):
##        if n%i == 0:
##            return False
##    return True
##
##primes = sorted(set(x for x in range(2,10000) if isprime(x)))
##
##smallest = 0
##for x in range(9,10000,2):
##    if x in primes:
##        continue
##    match=False
##    for p in primes:
##        if p>= x:
##            break
##        for i in squareslist:
##            if i >=x:
##                break
##            if p+i == x:
##                match = True
##    if match == False:
##        smallest = x
##        break
##    else:
##        continue
##
##print(smallest)


##44


##pentagonal = sorted(set(int(x*(3*x-1)/2) for x in range (1,10000)))
##
##
##
##
##print(pentagonal)

##41
##
##def sieve_prime(n):
##    test = [x for x in range(2,n)]
##    for x in range(int(math.sqrt(len(test)))+2):
##        if test[x]== False:
##            continue
##        currentprime=test[x]
##        for y in range(x+currentprime,len(test),currentprime):
##            test[y]=False
##    return sorted(list(set(test))[1:])
##
##def largest_pandigital(n):
##    largest=0
##    primelist = sieve_prime(n)
##    for prime in range(len(primelist)-1,-1,-1):
##        if sorted(str(primelist[prime])) == [str(x) for x in range(1,len(str(prime))+1)]:
##            largest=primelist[prime]
##            break
##    return largest
##
##
##print(largest_pandigital(10000000))



##50

##def sieve_prime(n):
##    test = [x for x in range(2,n)]
##    for x in range(int(math.sqrt(len(test)))+2):
##        if test[x]== False:
##            continue
##        currentprime=test[x]
##        for y in range(x+currentprime,len(test),currentprime):
##            test[y]=False
##    return sorted(list(set(test))[1:])
##
##primelist = sieve_prime(1000000)
##
##longestterms=5
##longestprimesum=0
##
##
##
##for prime in range(0,5):
##    for terms in range(1,600):
##        summ = sum(primelist[prime:prime+terms])
##        if summ > 1000000:
##            break
##        if summ in primelist and terms > longestterms:
##            longestterms = terms
##            longestprimesum = summ
##
##
##print(longestterms,longestprimesum)


##52

##for x in range (100000,1000000):
##    if sorted(str(x)) == sorted(str(x*2)) == sorted(str(x*3)) == sorted(str(x*4)) == sorted(str(x*5)) == sorted(str(x*6)):
##        print (x)
##        break





start = time.clock()
            ##Copy function to test here
stop = time.clock()
print (stop-start)







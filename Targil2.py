#Shalev Lazarof 300209202
#Igal Vaisberg 204166714

import itertools

##-------------------------------Question 1-------------------------------#

# Decorator function - Example with call method
def LeastUsedCache(funcToDecorate):
    cache = {}

    def __call__(*args): # Must be __call__
        if (args in cache):
            return cache[args]
        else:
            answer = funcToDecorate(*args)
            cache[args] = answer
            return answer
    return __call__


#each call for sum will initiate the memoize func first and send sum to it
@LeastUsedCache
def foo(x, y):
    print("I am foo")
    return x + y

c = LeastUsedCache(foo)
print(c.__call__(10,20))
print()
print(c.__call__(5, 6))
print()
print(c.__call__(10,20))
print()
print()

# Decorator function Question solution

def memoize(funcToDecorate):
    cache = {}

    def __call__(*args):
        if (args in cache):
            return cache[args]
        else:
            answer = funcToDecorate(*args)
            cache[args] = answer
            return answer
    return __call__


#each call for sum will initiate the memoize func first and send the function to it
@memoize
def sum(x , y):
    print('calling sum')
    return x + y


@memoize
def duplicate(x , y):
    print('calling duplicate')
    return x * y


@memoize
def minus(x , y):
    print('calling minus')
    return x - y

print(sum(5,6))
print(sum(5,6))
print(sum(5,6))
print(sum(5,6))


print(duplicate(7,8))
print(duplicate(7,8))
print(duplicate(7,8))
print(duplicate(7,8))

print()

print(minus(12,7))
print(minus(12,7))
print(minus(12,7))
print(minus(12,7))

print()

##-------------------------------Question 2-------------------------------#

class Rational:

    max = None

    def __init__(self, counter, denominator = 1):

        self.counter = counter
        self.denominator = denominator

        if(Rational.max == None):
            commonDevider = self.gcd(self.counter, self.denominator)

            tempA = self.counter / commonDevider
            tempB = self.denominator / commonDevider

            Rational.max = (int(tempA), int(tempB))
        else:
            if((Rational.max[0] / Rational.max[1]) < (self.counter / self.denominator)):
                commonDevider = self.gcd(self.counter, self.denominator)

                tempA = self.counter / commonDevider
                tempB = self.denominator / commonDevider

                Rational.max = (int(tempA) , int(tempB))

    def __add__(self, other):

        firstCommonDevider = self.gcd(self.counter, self.denominator)
        selfCounter = self.counter / firstCommonDevider
        selfDenominator = self.denominator / firstCommonDevider

        secondCommonDevider = self.gcd(other.counter, other.denominator)
        otherCounter = other.counter / secondCommonDevider
        otherDenominator = other.denominator / secondCommonDevider

        tempCounter = (int(otherDenominator) * int(selfCounter)) + (int(selfDenominator) * int(otherCounter))
        tempDenominator = int(selfDenominator) * int(otherDenominator)

        return Rational(tempCounter , tempDenominator)

    def __sub__(self, other):

        firstCommonDevider = self.gcd(self.counter, self.denominator)
        selfCounter = self.counter / firstCommonDevider
        selfDenominator = self.denominator / firstCommonDevider

        secondCommonDevider = self.gcd(other.counter, other.denominator)
        otherCounter = other.counter / secondCommonDevider
        otherDenominator = other.denominator / secondCommonDevider

        tempCounter = (int(otherDenominator) * int(selfCounter)) - (int(selfDenominator) * int(otherCounter))
        tempDenominator = int(selfDenominator) * int(otherDenominator)

        return Rational(tempCounter, tempDenominator)

    def __mul__(self, other):


        firstCommonDevider = self.gcd(self.counter, self.denominator)
        selfCounter = self.counter / firstCommonDevider
        selfDenominator = self.denominator / firstCommonDevider

        secondCommonDevider = self.gcd(other.counter, other.denominator)
        otherCounter = other.counter / secondCommonDevider
        otherDenominator = other.denominator / secondCommonDevider

        resultCommonDivider = self.gcd(int(selfCounter) * int(otherCounter) , int(selfDenominator) * int(otherDenominator))
        finalCounter = (int(selfCounter) * int(otherCounter)) / resultCommonDivider
        finalDenominator = (int(selfDenominator) * int(otherDenominator)) / resultCommonDivider

        return Rational(finalCounter , finalDenominator)

    def __truediv__(self, other):

        firstCommonDevider = self.gcd(self.counter, self.denominator)
        selfCounter = self.counter / firstCommonDevider
        selfDenominator = self.denominator / firstCommonDevider

        secondCommonDevider = self.gcd(other.counter, other.denominator)
        otherCounter = other.counter / secondCommonDevider
        otherDenominator = other.denominator / secondCommonDevider

        #resultCommonDivider = ((selfCounter * otherDenominator) , (selfDenominator * otherCounter))
        finalCounter = (selfCounter * otherDenominator)
        finalDenominator = (selfDenominator * otherCounter)

        return Rational(int(finalCounter) , int(finalDenominator))

    def __lt__(self, other):
        return (self.counter / self.denominator) < (other.counter / other.denominator)

    def __le__(self, other):
        return (self.counter / self.denominator) <= (other.counter / other.denominator)

    def __eq__(self, other):
        return (self.counter == other.counter) and (self.denominator == other.denominator)

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return (self.counter / self.denominator) > (other.counter / other.denominator)

    def __ge__(self, other):
        return (self.counter / self.denominator) >= (other.counter / other.denominator)

    def __str__(self):
        commonDevider = self.gcd(self.counter , self.denominator)
        tempA = self.counter / commonDevider
        tempB = self.denominator / commonDevider
        return "'{0}/{1}'".format(int(tempA), int(tempB))

    def __repr__(self):
        commonDevider = self.gcd(self.counter , self.denominator)
        tempA = self.counter / commonDevider
        tempB = self.denominator / commonDevider
        return "Rational ({0}, {1})".format(int(tempA), int(tempB))

    def gcd(self,a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

half = Rational(5,10)
print(str(half))
print(repr(half))
print(Rational.max)
third = Rational(8, 24)
print(str(third))
print(half + third)
print(third - half)
print(half * third)
print(half / third)
print(half == third)
print(half != third)
print(half < third)
print(half <= third)
print(half > third)
print(half >= third)
print(Rational.max)

##-------------------------------Question 3-------------------------------#

#generator function (yield)
def myZip(iterable1, iterable2, fill = None):

    iter1 = iter(iterable1)
    iter2 = iter(iterable2)
    selected2 = next(iter2,fill)
    selected1 = next(iter1,fill) #only for the first next, will jump g and retrieve the value

    while (selected1 != fill or selected2 != fill):
        if (fill == None and (selected1 == fill or selected2 == fill)):
            break
        else:
            yield (selected1,selected2) # each yield will return the current values to the for loop that initiate the function, from now on each iteration of the
                                        # for loop will return to this stage and continua in the while until Stop Iteration will occur
        try:
            selected1 = next(iter1, fill)
            selected2 = next(iter2, fill)
        except StopIteration:
            break

# g is a generator object
g = (3 * i for i in range(5))
for first, second in myZip(g, ["a", "b", "c"], fill = "bye"):
    print(first, second)

##-------------------------------Question 4-------------------------------#

# user defined class that supporting iteration
class MyZip:

    # Constructor
    def __init__(self, iterable1,iterable2,fill = None):
        self.iter1 = iterable1
        self.iter2 = iterable2
        self.fill = fill

    # iterable method in the class
    def __iter__(self):
        class Iterator:
            def __init__(self, iterable1,iterable2,fill):
                self.iter1 = iter(iterable1)
                self.iter2 = iter(iterable2)
                self.fill = fill

            def __iter__(self):
                return self

            def __next__(self):

                selected1 = next(self.iter1, self.fill)
                selected2 = next(self.iter2, self.fill)

                if (selected1 != self.fill or selected2 != self.fill):
                    try:
                        if (self.fill == None and (selected1 == self.fill or selected2 == self.fill)):
                            raise  StopIteration
                        else:
                            return (selected1, selected2)
                    except StopIteration:
                        raise StopIteration
                else:
                    raise StopIteration
        return Iterator(self.iter1, self.iter2, self.fill)

# g is a generator object
g = (3 * i for i in range(5))
for first, second in MyZip(g, ["a", "b", "c"], fill="bye"):
    print(first, second)

##-------------------------------Question 5-------------------------------#

def anagram(word):
    ret = []
    fin = open('words.txt')
    flag = True

    for specificWord in fin:
        iterator = iter(word)
        iterator2 = iter(specificWord)
        flag = True
        if(len(word) == (len(specificWord) - 1)):
            for i in range(len(word)):
                letter1 = next(iterator)
                if(letter1 not in specificWord):
                    flag = False
                    break

            for i in range(len(specificWord)):
                letter2 = next(iterator2)
                if(letter2 != "\n"):
                    if(letter2 not in word):
                        flag = False
                        break
        else:
            flag = False
        if (flag == True):
            ret.append(specificWord)
    fin.close()
    return ret

print(anagram('restful'))
print(anagram('rrao'))

##-------------------------------Question 6-------------------------------#

class VariableDescriptor:
    def __init__(self):
        self.value = 0

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("%s invalid." % value)
        else:
            self.value = value
            instance.CounterOfWrite += 1
            instance._history.append(value)

    def __get__(self, instance, owner):
        instance.CounterOfRead += 1
        return self.value

class Variable:
    CounterOfRead = 0
    CounterOfWrite = 0
    value = VariableDescriptor()

    def __init__(self, value):
        self._history = []
        self.value = value

    def history(self):
        print (self._history)

    def readCount(self):
        print (self.CounterOfRead)

    def writeCount(self):
        print (self.CounterOfWrite)

print()
v = Variable(30)
v.history()
v.readCount()
v.writeCount()
print(v.value)
v.readCount()
v.writeCount()
v.value = 17
v.history()
v.writeCount()
v.value = 17
v.writeCount()
v.history()
print(v.value)
v.readCount()
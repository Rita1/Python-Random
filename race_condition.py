from time import sleep
import random
from math import sqrt
from itertools import count, islice

class RaceCondition1():

    def __init__(self):
        self.balance = 0

    def add(self):
        self.balance += 1

    def remove(self):
        self.balance -= 1

    def add_remove(self, n):
        for i in range(n):
            self.add()

            sleep(random.randrange(0, 1))
            
            self.remove()

    def getbalance(self):
        return self.balance


class RaceCondition2():

    # helper field, calculate how many instances are made
    instance_made = 0

    # there should never be more than one RaceCondition2
    # object created
    condition = None

    def __new__(cls, *args, **kw):
        cls.instance_made = cls.instance_made + 1
        i = super(RaceCondition2, cls).__new__(cls)
        return i

    @staticmethod
    def create_condition():
        i = RaceCondition2()
        return i

    @classmethod
    def get_instance(cls):
        sleep(random.randrange(0, 1))
        if cls.condition == None:
            sleep(5)
            cls.condition = cls.create_condition()

        return cls.condition


class RaceCondition3():

    def is_probable_number(n):

        return n

    def is_number(cache, x):
        if x in cache:
            return cache[x]
        answer = RaceCondition3.is_probable_number(x)
        cache[x] = answer
        return cache


if __name__ == '__main__':
    #c1 = RaceCondition2.get_instance()
    #c2 = RaceCondition2.get_instance()
    #print(c1, c2, c1.instance_made, c2.instance_made)

    cache = {}
    c1 = RaceCondition3.is_number(cache, 101599)
    c2 = RaceCondition3.is_number(cache, 38)
    c3 = RaceCondition3.is_number(cache, 101599)
    print("c1", c1, cache)
    print("c2", c2, cache)


##// This class has a race condition in it.
##public class PinballSimulator {
##
##    private static PinballSimulator simulator = null;
##    // invariant: there should never be more than one PinballSimulator
##    //            object created
##
##    private PinballSimulator() {
##       System.out.println("created a PinballSimulator object");
##    }
##
##    // factory method that returns the sole PinballSimulator object,
##    // creating it if it doesn't exist
##    public static PinballSimulator getInstance() {
##        if (simulator == null) {
##            simulator = new PinballSimulator();
##        }
##        return simulator;
##    }
##}

## // is this method threadsafe?
## /**
## * @param x integer to test for primeness; requires x > 1
## * @return true if x is prime with high probability
## */
## public static boolean isPrime(int x) {
##    if (cache.containsKey(x)) return cache.get(x);
##    boolean answer = BigInteger.valueOf(x).isProbablePrime(100);
##    cache.put(x, answer);
##    return answer;
## }
##
## private static Map<Integer,Boolean> cache = new HashMap<>();
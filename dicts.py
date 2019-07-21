#from UserDict import UserDict
import collections

#class AV1(UserDict):

#https://docs.python.org/3.0/reference/datamodel.html#object.__contains__

class AV(dict):

    def __init__(self, inpt={}):
        print(dir(dict))
        super(AV, self).__init__(inpt)

    def get(self, k, default=None):
        print("get")
        new_key = k.lower()
        print("k",k.lower())
        return super(AV, self).get(new_key, default)

    def __getitem__(self, k):
        print("getitem")
        return super(AV, self).__getitem__(k)

    def fromkeys(self):
        print("fromkeys")
        return super().fromkeys()

    def __gt__ (self, other):
        print("ge")
        return super(AV, self).ge(self,other)

    def __contains__(self, key): #if ... in
          print("contains",key)
          return super(AV, self).__contains__(key)

    def __iter__(self):
        print("iter")
        return super(AV, self).__iter__(self)

    #def keys(self): #.keys()
    #    print("keys")
    #    return super().keys(oo)

    def __setitem__(self, key, value):
        print("setitem")
        super().__setitem__(key, value)

class Check:

    my_dict = AV()

    my_dict["Aaa1"] = ("IronMan", "Thor", "Hulk", "Captain")
    my_dict["Bbb2"] = ("Scarlet", "Wich", "BlackPanter")

    def check_key(self):
        key = "aaA2"
        print(self.my_dict.keys())
        #if key.lower() in [x.lower() for x in self.my.keys()]:
        if key.lower() in self.my_dict:
            answ = True
        else:
            answ = False
        return answ

    def check_value(self):
        key = "aaA13"
        value = "tHOr"
        #new_key = [x for x in self.my_dict.keys() if x.lower() == key.lower()][0]
        #my_set = self.my_dict.get(new_key)
        my_set = self.my_dict.get(key)
        if my_set and value.lower() in [x.lower() for x in my_set]:
            answ = True
        else:
            answ = False
        return answ

o1 = Check()
to_check_key = o1.check_key()
to_check_value = o1.check_value()
print(to_check_key)
print(to_check_value)

##assertThat("expected ernie", guessFollowsGraph.keySet(), contains(equalToIgnoringCase("ernie")));
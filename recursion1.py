
#Galima isardyti list'a skaiciu ir sudeti atgal
# kuria nauja sarasa []   mergin'a du list'us +

def add1(lon):

    if not lon:
        return []
    else:
        return [lon[0]] + add1(lon[1:])

#print("add1",add1([1,2,3,4]))

# logiskai () ir + sukuria tupl'a ir mergin'a. Nu nes add1 tai taip elgiasi
# bet kazkodel reikia rasyti (1,) o () tai nieko nedaro.

def add2(tuple):
    if not tuple:
        return ()
    else:
        return (tuple[0],) + add2(tuple[1:])

#print("add2 grazino tupl'e, teoriskai net neturi veikti (imutable)", add2((1,2,3,4,5)))

def add2_2(tuple):
    if not tuple:
        return []
    else:
        return (tuple[0],) + add2(tuple[1:])

#print("add2_2 kazkodel grazino tupl'e, nors 27 eilutej []", add2_2((1,2,3,4,5)))

#teoriskai galima i tuple sudeti ne tik skaicius bet ir list'us

def add3(tuple_of_list):
    if not tuple_of_list:
        return ()
    else:
        return (tuple_of_list[0],) + add3(tuple_of_list[1:])

#print("add3 turi grazinti list'u tuple", add3(([1,2,3],[2,3,4])))

#tada logiskai galima parasyti rekursijos funkcija ir bet kokiam sarasui elementu, pvz skaiciu

def add4(*args):                                #* - grazina is gautu parametru tuple, just because :)
    if args[0] == ():
        return ()
    if type(args[0]) is not tuple:               #todel tik pirmas ne tuple
        return (args[0],) + add4(args[1:])
    else:                                        #kitus reikes "istuplint"
        return (args[0][0],) + add4(args[0][1:])

#print("add4 turi grazinti skaiciu tuple", add4(1,2,3,2,3,4))

#TADAM dabar turi veikti ir ant list'u tuplo

#print("add4 turi grazinti list'u tuple", add4([1,2,3],[2,3,4]))


def add5(lon):
   #res = []
   if not lon:
       return []
   else:
       #res = add5(lon[1:])
       #print("res",res)

       return add5(lon[1:]).append(lon[0])

print(add5([1,2,3,4]))

def add5_1(lon):
   #res = []
   if not lon:
       return []
   else:
       res = add5_1(lon[1:])
       print("res",res)

       return res.append(lon[0]) or res

print(add5_1([1,2,3,4]))

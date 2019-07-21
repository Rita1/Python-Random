#def add0(*args):
#    print(len(args))
#    print(args)
#    if not bool(args):
#        return []
#    else:
#        return args[0] + add0(args[1:])

matrix0 = [[0, 1, 4], [0, 1, 2], [1, 2, 3]]
matrix1 = [[0, 1, 5], [1, 2, 6], [3, 4, 5]]
matrix2 = [[0, 1, 2], [2, 2, 2], [2, 1, 1]]
#print(add0(matrix0, matrix1, matrix2))

def add1(lon):

    if not lon:
        return []
    else:
        return [lon[0]] + add1(lon[1:])

#print(add1([1,2,3,4]))

def add2(lon):
    res = []
    if not lon:
        return []
    else:
        res = (lon[1:])
        print(res)
        print(lon[0])
        return res.append(lon[0])

print(add2([1,2,3,4]))

#def add2_2(lon):

 #   if not lon:
  #      return []
   # else:
    #    return add2_2(lon[1:]).append(lon[0])

#print("Add2_2", add2_2([1,2,3,4]))

def add4(tuple):
    print(tuple)
    if not tuple:
        return ()
    else:
        return (tuple[0],) + add4(tuple[1:])

#print(add4(([1, 2, 3, 4],[2,4,5,6])))

def add41(tuple):
    print(tuple)
    if not tuple:
        return []
    else:
        return [tuple[0]] + add41(tuple[1:])

#print(add41(([1, 2, 3, 4],[2,4,5,6])))

def add5(*args):
    print(args)
    if not args:
        return ()
    else:
        return args[0] + add5(args[1:])

print("add5",add5(([1, 2, 3, 4],[2,4,5,6],[3,4,5,6])))

def add3(*args):

    if not args:
        return []
    else:
        print("args[1:]",args[1:])
        print("args[1]", args[1])
        return args[0] + add3(args[1:])

#print(add3([1,2,3,4],[4,3,2,1],[5,6,7,8]))


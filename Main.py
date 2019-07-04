print("Start")


def numbers():
    numvar = 123
    strvar = "abc"
    fltvar = 0.0000123
    fltvar2 = 5.9e2
    longvar = 5000000000
    complexvar = 3.J
    print("numvar:{} strvar:{} fltvar:{} fltvar2:{} longvar{} complexvar: {}"
          .format(numvar, strvar, fltvar, fltvar2, longvar, complexvar))
    del longvar
    #  print(longvar)


def strings():
    str = "Hi! I'm Archana Mayani"
    #  num = int(str)
    print(str[2])
    print(str[0:15])
    if "!" in str:
        print("yes")
    print(str[3:])
    print(str[:2])


def concat_str_num():
    str_x, str_y = "3", "4"
    print(str_x + str_y)
    x, y = int(str_x), int(str_y)
    print(x+y)


def lists(arg):
    list1 = [1, 2, 3, 'xyz', '', "yy", 20.455, ['a', 'b', arg], arg+234]
    print(list1)
    print(list1[0])
    print(list1[0:2])
    print(list1[0:3])
    print(list1[:3])
    print(list1[3:6])
    print(list1[3:])
    print(list1 + ['Done'])
    # list2 = list1.append(['list2element'])
    list1.append(['list2element'])
    print("list1: ", list1)
    list2 = list1
    print(list2)
    list2[4] = "filledUpEmptyString :) "
    print("list2: ", list2)
    print("list1: ", list1)
    print("list 2 and 1 refers same object !")
    list3 = list1.copy()
    list3[4] = 'changedElementForList3Only'
    print("list3", list3)
    print("list1 and list2: ", list1, list2)


if __name__ == "__main__":
    numbers()
    strings()
    concat_str_num()
    lists(1)
    # lists('1') # TypeError: can only concatenate str (not "int") to str

from testpkg import TestClass
from testpkg.Class_File import Test1


def test_func():
    print("Hello")
    TestClass.my_function()
    test = Test1(1,2)
    print(test.multiply(3,10))
    test._private2()
    test.printvar()


def sum(a, b):
    return a+b


if __name__ == '__main__':
    test_func()
    print(sum(5, 10))


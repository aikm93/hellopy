class Test1:

    var_1 = None


    def __init__(self, a,b):
        print("My Fiest Py Constructor")
        print("Variable is {}:{}".format(a,b))
        self.var_1 = a


    def printvar(self):
        print("Variable is {}".format((self.var_1)))


    def multiply(self,a,b):
        return a*b

    def __myprivatemethod(self):
        print("my private method")

    def _private2(self):
        print("DJ")


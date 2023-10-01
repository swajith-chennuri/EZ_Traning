class a:
    x=10
    __y=20
    print(x)
    def s(self):
        print("add")
    def work(self,x):
        self.x=x
        print(x)
class b(a):
    print("hi")
class c(a):
    print("swajith")
    print(a.x)
#main.
obj=b()
print(obj.x)
obj.s()
obj.work(50)
print(b.x)
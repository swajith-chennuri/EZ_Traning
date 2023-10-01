class swajith:
    x=input("enter a string = ")
    y=int(input("enter any integer = "))
    z=int(input("enter any integer = "))
    def sri(self,a,b):
    #a string ,b int
        print("reverse of given string = ",a[::-1])
        print("the square of a given 1st int = ",b*b)
    
    def display_results(self,x,y,z):
        print("the len of the string = ",len(x))
        print("mod of the 1st int and 2nd int = ",y%z)
obj=swajith()
obj.sri(obj.x,obj.y)
obj.display_results(obj.x,obj.y,obj.z)
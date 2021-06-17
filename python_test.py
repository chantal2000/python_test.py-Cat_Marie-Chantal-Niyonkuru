x=[100,110,120,130,140,150]
for a in x:
    [a*5 for a in x]
    print(a*5)

def divisible_by_three(n):
    m=range(1,n)
    for a in m:
        if a%3==0:
            print(a)
divisible_by_three(10)

def  flatterns():
    x=[[1,2],[3,4],[5,6]]
    for a in x  b in x:
        print(n)
   
flatterns()

def smallest(*args):
    smallestNumber=min(args)
    print(smallestNumber)
smallest(2,34,5,6,9,1)

def removeduplicates():
    x = ['a','b','a','e','d','b','c','e','f','g','h']
    y=set(x)
    x=list(y)
    print(x)
removeduplicates()

def divisible_by_seven():
    y=range(100,200)
    for h in y:
        if h%7==0:
            print(h)
divisible_by_seven()

def greet():
    students = [{"age": 19, "name": "Eunice"},
     {"age": 21, "name": "Agnes"},
     {"age": 18, "name": "Teresa"}, 
     {"age": 22, "name": "Asha"}]
    for student in students:
        print("Hello {} you were born in year {}".format(student["name"],2021-student["age"]))
greet()

class Rectangle:
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        A=self.length*self.width
        print(A)
    def perimeter(self):
        P=2*(self.length*self.width)
        print(P)
rectangle1=Rectangle(3,4)
rectangle1.area()
rectangle1.perimeter()






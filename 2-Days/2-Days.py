Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello")
Hello
dic = {"title": "TV", "price": 1000}
dic["detail"] = "TV Detail"
print(dic)
{'title': 'TV', 'price': 1000, 'detail': 'TV Detail'}
keys = dic.keys()
values = dic.values()
print( keys, values )
dict_keys(['title', 'price', 'detail']) dict_values(['TV', 1000, 'TV Detail'])
for (key, val) in dic:
    print( key, val )

    
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    for (key, val) in dic:
ValueError: too many values to unpack (expected 2)
for key, val in dic:
    print( key, val )

    
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    for key, val in dic:
ValueError: too many values to unpack (expected 2)
for key, val in dic.items():
    print( key, val )

    
title TV
price 1000
detail TV Detail
dic.pop("detail")
'TV Detail'
print(dic)
{'title': 'TV', 'price': 1000}
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
keys = myfamily.keys()
for key in keys:
    child = myfamily[key]
    print( child["name"], child["year"] )

    
Emil 2004
Tobias 2007
Linus 2011



num1 = 10
num2 = 11
if num1 == num2:
    print("sayılar eşit")
    else:
        
SyntaxError: invalid syntax
if num1 == num2:
    print("sayılar eşit")
    elif:
        
SyntaxError: invalid syntax
if num1 == num2:
    print("sayılar eşit")
elif:
    
SyntaxError: invalid syntax
if num1 == num2:
    print("sayılar eşit")
else:
    print("sayılar eşit değil")

    
sayılar eşit değil
if num1 == num2:
    print("sayılar eşit")

    
name=""
surname=""
email=""
password=""
if name == "" or surname == "" or email == "" or password == "" :
    print("Bazı alanlar boş")

    
Bazı alanlar boş
if name == "".
SyntaxError: invalid syntax
if name == "":
    print("name empty!")
elif surname == "":
    print("surname empty!")
elif email ==  "":
    print("email empty!")
elif password == "":
    print("password empty!")
else:
    print("Form Send")

    
name empty!
name="Erkan"
surname=""
email="erkan@mail.com"
password=""
SyntaxError: multiple statements found while compiling a single statement

name=""
surname=""
email=""
password=""
SyntaxError: multiple statements found while compiling a single statement
name="Erkan"
surname=""
email="erkan@mail.com"
password="12345"
if name == "":
    print("name empty!")
elif surname == "":
    print("surname empty!")
elif email ==  "":
    print("email empty!")
elif password == "":
    print("password empty!")
else:
    print("Form Send")

    
surname empty!
name="Erkan"surname=""
SyntaxError: invalid syntax
name="Erkan"
surname="Bilmem"
email="erkan@mail.com"
password="12345"
if name == "":
    print("name empty!")
elif surname == "":
    print("surname empty!")
elif email ==  "":
    print("email empty!")
elif password == "":
    print("password empty!")
else:
    print("Form Send")

    
Form Send
if num1 > 10 or num2 > 10:
    print("Koşullar sağlanıyor")
else:
    print("Koşullar sağlanmıyor")

    
Koşullar sağlanıyor
if num1 > 9 and num2 == 10:
    print("Koşullar sağlanıyor")
else:
    print("Koşullar sağlanmıyor")

    
Koşullar sağlanmıyor
data = num1 > 9 ? "9'dan Büyük" : "9'dan küçük"
SyntaxError: invalid syntax
data = num1 > 9 : "9'dan Büyük" : "9'dan küçük"
SyntaxError: invalid syntax
if num1 > 9 : dat = "9'dan Büyük"
print( dat )
SyntaxError: invalid syntax
data = ""
if num1 > 9 : data = "9'dan Büyük"
print( data )
SyntaxError: invalid syntax
if num1 > 9 : data = "9'dan Büyük"
    print( data )
    
SyntaxError: unexpected indent
if num1 > 9:
    data = "9'dan Büyük"
    print( data )

    
9'dan Büyük
x = 0
while x < 10:
    print("While Call")
    ,
SyntaxError: invalid syntax
while x < 10:
    print("While Call")
    x = x + 1

    
While Call
While Call
While Call
While Call
While Call
While Call
While Call
While Call
While Call
While Call
while x < 10:
    print("While Call :", x)
    x = x + 1

    

x = 0
while x < 10:
    print("While Call :", x)
    x = x + 1
    
SyntaxError: multiple statements found while compiling a single statement
x = 0
while x < 10:
    print("While Call :")
    x = x + 1
    
SyntaxError: multiple statements found while compiling a single statement

y = 0
while y < 10:
    print("While Call :", y)
    y = y + 1
    
SyntaxError: multiple statements found while compiling a single statement

y = 0
while y < 10:
    print("While Call :", y)
    y = y + 1
    
SyntaxError: multiple statements found while compiling a single statement

y = 0
while y < 10:
    print("While Call :", y)
    y = y + 1
    
SyntaxError: multiple statements found while compiling a single statement
y=0
while y<10:
    print("While Call :", y)
    y  = y + 1

    
While Call : 0
While Call : 1
While Call : 2
While Call : 3
While Call : 4
While Call : 5
While Call : 6
While Call : 7
While Call : 8
While Call : 9
y=0
while y<10:
    print("While Call :", y)
    y  = y + 1
    if y = 5:
        
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
y=0while y<10:
    print("While Call :", y)
    y  = y + 1
    if y == 5:
        
SyntaxError: invalid decimal literal
y=0
while y<10:
    print("While Call :", y)
    y  = y + 1
    if y == 5:
        break

    
While Call : 0
While Call : 1
While Call : 2
While Call : 3
While Call : 4
city = "İstanbul"
for char in city:
    print(char)

    
İ
s
t
a
n
b
u
l
for i in range(10):
    print("For", i)

    
For 0
For 1
For 2
For 3
For 4
For 5
For 6
For 7
For 8
For 9
for i in range(5, 15, 2):
    print("For Range", i)

    
For Range 5
For Range 7
For Range 9
For Range 11
For Range 13
def noParams():
    print("noParams Call")

    
noParams()
noParams Call
def sum( n1, n2 ):
    sm = n1 + n2
    print("Sum: ", sm)

    
sum(100,500)
Sum:  600
sum(343,565)
Sum:  908
smx = sum(100, 3453)
Sum:  3553
print (smx)
None
def returnSum(n1, n2):
    sm = n1 + n2
    return sm

smy = returnSum(234,4564)
print("Sm : ", smy)
Sm :  4798

def arrFnc( *arr ):
    print( arr[1] )

    
arrFnc("ali", "veli", "hasan")
veli
listx = ["ali", "veli", "hasan"]
arrFnc(listx)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    arrFnc(listx)
  File "<pyshell#149>", line 2, in arrFnc
    print( arr[1] )
IndexError: tuple index out of range
arrFnc(listx.extend())
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    arrFnc(listx.extend())
TypeError: list.extend() takes exactly one argument (0 given)
arrFnc("ali", "veli", "hasan")
veli
def fncDic(**dic):
    print(dic["name"])

    
fncDic( name = "Zehra", surname = "Bilmem" )
Zehra


def fncDefaultValue( yas = 0, boy = 0 ):
    end = yas / boy
    print(end)

    
fncDefaultValue(35, 170)
0.20588235294117646
fncDefaultValue(50)
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    fncDefaultValue(50)
  File "<pyshell#164>", line 2, in fncDefaultValue
    end = yas / boy
ZeroDivisionError: division by zero
def fncDefaultValue( yas = 1, boy = 1 ):
    end = yas / boy
    print(end)

    
fncDefaultValue(35)
35.0
fncDefaultValue(35, 180)
0.19444444444444445
listx = ["İstanbul", "İzmir", "Samsun", "Adana", "Ankara"]
def fncList(arr):
    for item in arr:
        print( item )

        
fncList(listx)
İstanbul
İzmir
Samsun
Adana
Ankara
def recursive( n ):
    if n == 0:
        return 1
    else:
        return 1

    
# lambda
sumLambda = lambda a, b : a + b
sumz = sumLambda(40, 55)
print( sumz )
95



class Action:
    name = "Ali"
    surname = "Bilmem"
    age = 30

    
ojb1 = Action()
print( type(obj1) )
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    print( type(obj1) )
NameError: name 'obj1' is not defined
obj1 = Action()
print( type(obj1) )
<class '__main__.Action'>
print( obj1.name, obj1.surname, obj1.age )
Ali Bilmem 30




class Settings:
    num1 = 20
    def fncAction:
        
SyntaxError: invalid syntax
class Settings:
    num1 = 20
    def fncAction():
        return num1 * num1

    
objSet = Settings()
end = objSet.fncAction()
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    end = objSet.fncAction()
TypeError: Settings.fncAction() takes 0 positional arguments but 1 was given
objSet = Settings()
objSet.fncAction()
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    objSet.fncAction()
TypeError: Settings.fncAction() takes 0 positional arguments but 1 was given
class Settings:
    num1 = 20
    def fncAction(self):
        return self.num1 * self.num1

    
objSet = Settings()
objSet.fncAction()
400
objSet.num1 = 30
objSet.fncAction()
900



class Customer:
    def __init__(self, name, surname, email, age ):
        self.name = name
        self.surname = surname
        self.age = age

        
customer = Customer("Serkan", "Bilmem", "serkan@mail", 40)
class Customer:
    def __init__(self, name, surname, email, age ):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email

        
customer = Customer("Serkan", "Bilmem", "serkan@mail", 40)
customer = Customer("Serkan", "Bilmem", "serkan@mail", 40)
print( customer.name, customer.surname, customer.email, customer.age)
Serkan Bilmem serkan@mail 40
customerx = Customer()
Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    customerx = Customer()
TypeError: Customer.__init__() missing 4 required positional arguments: 'name', 'surname', 'email', and 'age'
del customer
print( customer )
Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    print( customer )
NameError: name 'customer' is not defined. Did you mean: 'Customer'?



class Student(Customer):
    def fncName(self):
        print(self.name, self.surname)

        
std = Student("Mehmet", "Bilsin", "mehmet@mail.com", 40)
std.fncName()
Mehmet Bilsin




lst = ["Mehmet", "Ayşe", "Suna", "Ali", "Kemal"]
for item in lst:
    print(item)

    
Mehmet
Ayşe
Suna
Ali
Kemal
for item in lst:
    print(item)

    
Mehmet
Ayşe
Suna
Ali
Kemal


itr1 = iter(lst)
print( type(itr1) )
<class 'list_iterator'>
print( itr1.next() )
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    print( itr1.next() )
AttributeError: 'list_iterator' object has no attribute 'next'
print( itr1.next )
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    print( itr1.next )
AttributeError: 'list_iterator' object has no attribute 'next'
print( next(itr1) )
Mehmet
print( next(itr1) )
Ayşe
print( next(itr1) )
Suna
print( next(itr1) )
Ali
print( next(itr1) )
Kemal
print( next(itr1) )
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    print( next(itr1) )
StopIteration


itr1 = iter(lst)
itr1.sizeof()
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    itr1.sizeof()
AttributeError: 'list_iterator' object has no attribute 'sizeof'
itr1.sizeof
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    itr1.sizeof
AttributeError: 'list_iterator' object has no attribute 'sizeof'

for item in lst:
    print( next(itr1) )

    
Mehmet
Ayşe
Suna
Ali
Kemal
for item in lst:
    print( next(itr1) )

    
Traceback (most recent call last):
  File "<pyshell#282>", line 2, in <module>
    print( next(itr1) )
StopIteration


objTuple = ("Adana", "Antalya", "Mersin")
print(type(objTuple))
<class 'tuple'>
itr2 = iter(objTuple)
print( next(iter2) )
Traceback (most recent call last):
  File "<pyshell#288>", line 1, in <module>
    print( next(iter2) )
NameError: name 'iter2' is not defined. Did you mean: 'itr2'?
print( next(itr2) )
Adana





def fncSet():
    cityName = "İzmir"

    
fncSet()
print( cityName )
Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    print( cityName )
NameError: name 'cityName' is not defined
def fncSet():
    global cityName
    cityName = "İzmir"

    
fncSet()
print( cityName )
İzmir



customerName = ""
customerName = "Kemal"
def fncCustomerName():
    customerName = "Ecem"

    
print( customerName )
Kemal
fncCustomerName()
print( customerName )
Kemal
def fncCustomerName():
    self.customerName = "Ecem"

    
print( customerName )
Kemal
fncCustomerName()
Traceback (most recent call last):
  File "<pyshell#316>", line 1, in <module>
    fncCustomerName()
  File "<pyshell#314>", line 2, in fncCustomerName
    self.customerName = "Ecem"
NameError: name 'self' is not defined
def fncCustomerName(self):
    self.customerName = "Ecem"

    
print( customerName )
Kemal
fncCustomerName()
Traceback (most recent call last):
  File "<pyshell#320>", line 1, in <module>
    fncCustomerName()
TypeError: fncCustomerName() missing 1 required positional argument: 'self'
fncCustomerName(self)
Traceback (most recent call last):
  File "<pyshell#321>", line 1, in <module>
    fncCustomerName(self)
NameError: name 'self' is not defined



customerName = "Kemal"
print( hash(customerName) )
3879842008829745755
customerName = "Kemal"
print( hash(customerName) )
3879842008829745755
def fncCustomerName():
    customerName = "Ecem"
    print( hash(customerName) )

    
fncCustomerName()
-6973979295059972328

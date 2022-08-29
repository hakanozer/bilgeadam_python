Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
print("merhaba")
merhaba
print("merhaba")
merhaba
exit()
#print verilen değerin yazdırılması içindir.
"""
# tek satırlık yorum bölümü iken
3 adet tırnak çok satırlı yorum bölümüdür.
"""
'\n# tek satırlık yorum bölümü iken\n3 adet tırnak çok satırlı yorum bölümüdür.\n'
print('son satır')
son satır


# Değişkenler
# String değişken
name = 'Ali'
surname = "Bilmem"
age = 30
print(name, surname, age)
Ali Bilmem 30
action
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    action
NameError: name 'action' is not defined
action = 0
action = "Veli"
print(action)
0
action = "Veli"
action = 0
print(action)
0
status = "Veli"
status = "Serkan"
print(status)
Serkan
Serkan
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    Serkan
NameError: name 'Serkan' is not defined

num1 = 13.3
num2 = 55.7
numSum = num1 + num2
print( "Sum", numSum)
Sum 69.0

type1 = type(num1)
print( type1 )
<class 'float'>
type2 = type(name)
print(type2)
<class 'str'>

num3:int = "str"
print(num3)
str
1num = 3
SyntaxError: invalid decimal literal
num-1=3
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
username="ali"
userName="ali"
userName, userSurname, userEmail = "Veli", "Bilmem", "veli@mail.com"
print( userName, userSurname, userEmail )
Veli Bilmem veli@mail.com
arr = ["İstanbul", "Ankara", "Samsun"]
x,y,x = arr
print( x, y, z )
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print( x, y, z )
NameError: name 'z' is not defined
x,y,z = arr
print( x, y, z )
İstanbul Ankara Samsun
print( arr )
['İstanbul', 'Ankara', 'Samsun']
print( arr[0] )
İstanbul



#global variable
cityName = "İstanbul"
def fncCity():
    print(cityName)

    
fncCity()
İstanbul
def fncCity():
    cityName = "Adana"
    print(cityName)

    
fncCity()
Adana
def fncCity():
    cityNamex = "Adana"
    print(cityNamex)

    
fncCity()
Adana
print(cityName)
İstanbul
print(cityNamex)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(cityNamex)
NameError: name 'cityNamex' is not defined. Did you mean: 'cityName'?



# List
list1 = ["Ali", 30, true, 12.7]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list1 = ["Ali", 30, true, 12.7]
NameError: name 'true' is not defined. Did you mean: 'True'?
list1 = ["Ali", 30, 12.7]
list1 = ["Ali", 30, True, 12.7]
print( type(list1) )
<class 'list'>
print( list[0] )
list[0]
print( list1[0] )
Ali

print( type(list1[0]) )
<class 'str'>
print( len(list1) )
4
print( list1[-1] )
12.7
print( list1[0:2])
['Ali', 30]
newList = list1[0:2]
print( newList[0], newList[1] )
Ali 30
list1 = ["Ali", 30, True, 12.7]
if "Ali" in list1:
    print( True )

    
True
list1 = ["Ali", 30, True, 12.7]
list1[0] = "Erkan"
print(list1)
['Erkan', 30, True, 12.7]
list1 = ["Ali", 30, True, 12.7]
list1.append("Veli")
print(  list1 )
['Ali', 30, True, 12.7, 'Veli']
list1.insert(1, False)
print(  list1 )
['Ali', False, 30, True, 12.7, 'Veli']
list1.remove("False")
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    list1.remove("False")
ValueError: list.remove(x): x not in list
list1.remove(False)
print(  list1 )
['Ali', 30, True, 12.7, 'Veli']
list1.append("Ali")
list1.append("Ali")
print(  list1 )
['Ali', 30, True, 12.7, 'Veli', 'Ali', 'Ali']
list1.remove("Ali")
print(  list1 )
[30, True, 12.7, 'Veli', 'Ali', 'Ali']
list1.pop(4)
'Ali'
print(  list1 )
[30, True, 12.7, 'Veli', 'Ali']
list1.clear()
print(  list1 )
[]
del list1
print(  list1 )
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print(  list1 )
NameError: name 'list1' is not defined. Did you mean: 'list'?
list1 = [30, True, 12.7, 'Veli', 'Ali']
for x in list1:
    print(x)

    
30
True
12.7
Veli
Ali
for x in list1:
    if 'Veli' == x:
        print("This val: Veli")

        
This val: Veli
for x in list1:
    if 'Veli' == x:
        print("This val: ", x)

        
This val:  Veli
list2 = ["Ankara", "İzmir", "İstanbul", "Samsun", "Antalya", "Adana"]
list3 = []
for item in list2:
    if item in "a":
        list3.append(item)

        
print(list3)
[]
for item in list2:
    if "a" in item:
        list3.append(item)

        
print(list3)
['Ankara', 'İstanbul', 'Samsun', 'Antalya', 'Adana']
list3 = []
print(list3)
[]
list3 = [ item for item in list2  ]
print( list3 )
['Ankara', 'İzmir', 'İstanbul', 'Samsun', 'Antalya', 'Adana']
list3 = [ item for item in list2 if "a" in item ]
print(list3)
['Ankara', 'İstanbul', 'Samsun', 'Antalya', 'Adana']
list3 = [ item.upper() for item in list2 if "a" in item ]
print(list3)
['ANKARA', 'İSTANBUL', 'SAMSUN', 'ANTALYA', 'ADANA']
list2.sort()
print(list2)
['Adana', 'Ankara', 'Antalya', 'Samsun', 'İstanbul', 'İzmir']
list2.sort(reverse=True)
print(list2)
['İzmir', 'İstanbul', 'Samsun', 'Antalya', 'Ankara', 'Adana']
list4 = [33,45,67,89,23,11,23,99]
def fncSort(item):
    return item * 3
list4.sort(key=fncSort)
SyntaxError: invalid syntax
list4.sort(key = fncSort)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    list4.sort(key = fncSort)
NameError: name 'fncSort' is not defined
def fncSort(n):
    return n * 3
list4.sort(key=fncSort)
SyntaxError: invalid syntax
def fncSort(n):
    return n - 3
list4.sort(key=fncSort)
SyntaxError: invalid syntax
def myfunc(n):
  return abs(n - 50)
list4.sort(key=myfunc)
SyntaxError: invalid syntax
def myfunc(n):
  return abs(n - 50)

list4.sort(key = myfunc)
SyntaxError: invalid syntax
list4.sort( key = int.bit_count )
print(list4)
[33, 67, 11, 45, 89, 23, 23, 99]










list5 = ["A", "B", "C"]
list6 = list5
print(list6)
['A', 'B', 'C']
list5.append("D")
print(list6)
['A', 'B', 'C', 'D']
list5 = ["A", "B", "C"]
list6 = list5.copy()
print(list6)
['A', 'B', 'C']
list5.append("D")
print(list6)
['A', 'B', 'C', 'D']
SyntaxError: multiple statements found while compiling a single statement
['A', 'B', 'C', 'D']
['A', 'B', 'C', 'D']
list6 = list5.copy()
 list5.append("E")
 
SyntaxError: unexpected indent
list7 = ["A", "B", "C"]
list8  = list7.copy()
list7.append("D")
print( list8 )
['A', 'B', 'C']
list9 = list5
list10 = list5
list9 = list5
list10 = list9
SyntaxError: multiple statements found while compiling a single statement
list9 = list5
list10 = list9





listx = [ item for item in list4 ]
,
SyntaxError: multiple statements found while compiling a single statement
listx = [ item for item in list4 ]
listx.append(101)
SyntaxError: multiple statements found while compiling a single statement
listy = [ item for item in list4 ]
listy.append(101)
SyntaxError: multiple statements found while compiling a single statement
listy = [ for item in list4 ]
listy.append(101)
SyntaxError: invalid syntax
listy = [ item for item in list4 ]
print(listy)
[33, 67, 11, 45, 89, 23, 23, 99]
listy = [ item for item in list4 ]
listy.append(101)
print(listy)
[33, 67, 11, 45, 89, 23, 23, 99, 101]
print( list4 )
[33, 67, 11, 45, 89, 23, 23, 99]




arr1 = ('ali', 22, 56.7, True, 😂)
SyntaxError: invalid character '😂' (U+1F602)
arr1 = ('ali', 22, 56.7, True, U+1F602)
SyntaxError: invalid decimal literal
arr1 = ('ali', 22, 56.7, True, 😂)
SyntaxError: invalid character '😂' (U+1F602)
arr1 = ('ali', 22, 56.7, True, "Mehmet", "Serkan")
print( type(arr1) )
<class 'tuple'>
print( arr1[0] )
ali
arr1[0] = "Zehra"
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    arr1[0] = "Zehra"
TypeError: 'tuple' object does not support item assignment
newList = list(arr1)
newList[0] = "Zehra"
arr1 = tuple(newList)
print( arr1 )
('Zehra', 22, 56.7, True, 'Mehmet', 'Serkan')
for item in arr1:
    print(item)

    
Zehra
22
56.7
True
Mehmet
Serkan
for 1...3 in arr1:
    
SyntaxError: cannot assign to literal
for 1...3 arr1:
    
SyntaxError: cannot assign to literal
for i in 3 {
    
SyntaxError: '{' was never closed
for i in 3:
print(arr1[i])
SyntaxError: expected an indented block after 'for' statement on line 1
for i in 0...3:
print(arr1[i])
SyntaxError: invalid syntax
for i in range(len(arr1)):
print(arr1[i])
SyntaxError: expected an indented block after 'for' statement on line 1
for i in range(len(arr1)):
    print(arr1[i])

Zehra
22
56.7
True
Mehmet
Serkan
for i in 1...3):
    print(arr1[i])
    
SyntaxError: unmatched ')'
for i in 1...3:
    print(arr1[i])
    
SyntaxError: invalid syntax
for i in 1..3:
    print(arr1[i])
    
SyntaxError: invalid syntax
for i in 1_3:
    print(arr1[i])

    
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    for i in 1_3:
TypeError: 'int' object is not iterable
print( arr1.count )
<built-in method count of tuple object at 0x10df616c0>
print( arr1.count() )
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    print( arr1.count() )
TypeError: tuple.count() takes exactly one argument (0 given)
print( arr1.count(1) )
1
print( arr1.count(3) )
0
print( arr1[0])
Zehra
for i in 1,3:
    print(arr1[i])

    
22
True
for i in 1,len(arr1):
    print(arr1[i])

    
22
Traceback (most recent call last):
  File "<pyshell#235>", line 2, in <module>
    print(arr1[i])
IndexError: tuple index out of range
for i in 1,len(arr1) - 1:
    print(arr1[i])

    
22
Serkan
for i in 0,len(arr1) - 1:
    print(arr1[i])

    
Zehra
Serkan
for i in 0,len(arr1):
    print(arr1[i])

    
Zehra
Traceback (most recent call last):
  File "<pyshell#243>", line 2, in <module>
    print(arr1[i])
IndexError: tuple index out of range
for i in 0,len(arr1) -1:
    print(arr1[i])

    
Zehra
Serkan
for i in 0,1,2,len(arr1) -1:
    print(arr1[i])

    
Zehra
22
56.7
Serkan
sizeArr = [0,3,4]
for i in sizeArr:
    print(arr1[i])
    
SyntaxError: multiple statements found while compiling a single statement




newSet = {}
print( type(newSet) )
<class 'dict'>
newSet = {}print( type(newSet) )
SyntaxError: invalid syntax
newSet = {"Ali"}
newSet = {"Ali", "Veli", "Serkan", "Veli"}
print( newSet )
{'Veli', 'Ali', 'Serkan'}
newSet = {"Ali", "Veli", "Serkan", "Veli"}
print( type(newSet) )
<class 'set'>
print(len(newSet))
3
newSet.add("Mehmet")
print(newSet)
{'Veli', 'Ali', 'Mehmet', 'Serkan'}
newSet.remove("Serkan")
print( newSet )
{'Veli', 'Ali', 'Mehmet'}
deleteItem = newSet.pop()
print( deleteItem )
Veli
Veli
Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    Veli
NameError: name 'Veli' is not defined
print( newSet )
{'Ali', 'Mehmet'}




dic = { name: "Serkan", surname: "Bilmem", age: 30, email: "serkan@mail.com" }
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    dic = { name: "Serkan", surname: "Bilmem", age: 30, email: "serkan@mail.com" }
NameError: name 'email' is not defined. Did you mean: 'eval'?
dic = { "name": "Serkan", "surname": "Bilmem", "age": 30, "email": "serkan@mail.com" }
dic = { "name": "Serkan", "surname": "Bilmem", "age": 30, "email": "serkan@mail.com" }
print(dic)
{'name': 'Serkan', 'surname': 'Bilmem', 'age': 30, 'email': 'serkan@mail.com'}
dic = { "name": "Serkan", "surname": "Bilmem", "age": 30, "email": "serkan@mail.com", status: True}
print ( dic )
{'name': 'Serkan', 'surname': 'Bilmem', 'age': 30, 'email': 'serkan@mail.com', 'Serkan': True}
print( dic["name"] )
Serkan
print( len( dic ) )
5
keys = dic.keys()
print( keys )
dict_keys(['name', 'surname', 'age', 'email', 'Serkan'])
dic = { "name": "Serkan", "surname": "Bilmem", "age": 30, "email": "serkan@mail.com", "status": True}
keys = dic.keys()
print( keys )
dict_keys(['name', 'surname', 'age', 'email', 'status'])
print( dic["surname"] )
Bilmem
for key in keys:
    print( dic[key] )

    
Serkan
Bilmem
30
serkan@mail.com
True

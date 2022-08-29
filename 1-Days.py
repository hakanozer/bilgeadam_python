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

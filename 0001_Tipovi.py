# Komentar, hash i jedan razmak

# Digits

cijeli_broj = 2
decimalni_broj = 3.37

# dynamically typed, variable can reference any type of object
# variables are only reference to objects in memory

nesto = 1   # integer
print 'nesto' , nesto , type ( nesto )

nesto = 2.456  # decimal
print 'nesto' , nesto , type ( nesto )

# "Tipovi" su built in objects, predefined types

# Numbers

a = 5
a = 3.14
a = 3+5j
a = 0b1001

# strings

a = "Bla"	# ide i " i ' kao odrednica stringova
a = 'Bli'

# Liste, poziciono indeksirani nizovi bilokakvih objekata limitirani sa [] 

a = [ 1 , 2.345 , "Bla" , 'Bli']

print a [ 2 ]

# Dictionaries hash ( objekt na objekt ) table sa unique keyevima limitirana sa {} , key - value par povezan je sa :

d = 7    # 7 je objekt koji ce biti key ide se po valueu tj. prije dodjeljivanja key-a radi se dereferencija objekta od imena
a = { 1 : 7 , 9 : 3+7j , d : "Bla" , 'Bli' : 0b1001 }

print a [ d ]

d = 9
print a [ d ]

# Tuples 
# Files 
# Sets 
# Other core types Booleans, types, None
# Program unit types Functions, modules, classes 
# Implementation-related types Compiled code, stack tracebacks 

# operacije sa "brojevima"

print 123 + 321
print 2 / 3 		#ako krenemo sa intergerom dobiti cemo interger
print 2. / 33		#ovdje dobijemo float
print 2 / 33.		#ovdje dobijemo float
print 2 ** 99		#ako krenemo sa intergerom dobiti cemo duuuugacki interger
print 2. ** 99		#ovdje dobijemo float/ scientific notation

# matematicki modul je jako koristan

import math
print math.pi

# i random modul je koristan

import random
print random.random ()
print random.choice ( [ 2 , 5 , 9 , 3 ] )


# Strings built in object / types
# "indexed sequences"

a = "Pero Jede Jagode"
a = 'Pero jede Jagode'

# indeksiranje u sequenci ide od 0 do (len -1) ili od ( -len ) do -1

print a [ 15 ]  # isto je kao i 
print a [ -1 ]

# slajs 'slice' ode od pocetka do kraja ,, kraj nije ukljucen u slajs

print a [ 5:12 ] # 12 nije ukljucen, 5 jeste

# Kad je broj izostavljen podrazumijeba se pocetak ili kraj

print a [ :12 ]
print a [ 5: ]
print a [ : ]		#treba zapamtiti da ovo pravi novi objekt

# Treci parametar u sliceu kaze kao se biraju elemwnti

print a [ ::2 ]		#svaki drugi element
print a [ ::5 ]		#svaki peti element
print a [ ::-1 ]	#svi elementi unazad, od zadnjeg do prvog
print a [ ::-2 ]	#svaki drugi element unazad

# Sequence se mogu zbrajati ali to radi novi objekt

b = "Svaki Dan"

print a + b
print a [ ::-1 ] + b
print a [ 2:7 ] + " - " + b [ 6:2:-1 ]

# Sequence se mogu i mnoziti

print b * 3
print "Asdfghj " * 4













# Lists in python

# Lists are mutable and extendable and are sequence of objects ...

a = [ 1 , "asdf" , 3.14 , 4+7j]

print "lista puna razlicitih objekata",a

a.append ( "novi element")		# adding element on end off list

print "lista sa dodanim novim elementom",a

print "uzima se drugi element liste i uklanja iz liste -->",a.pop ( 1 )			# getting and removing second element from list

print "listi je izvadjen drugi element",a,  len ( a )

a = [ 4 , 23 ,-17 , 1]

print "lista sa brojevima",a

a.sort () 	# list is now sorted, warring with sorting problems with unsortable elements

print "sortirana lista sa brojevima",a

a.reverse () 	# list is now reversed sorted

print "inverzno sortirana lista",a

a [ 1 ] = 3		# new value in second element of the list - lists are MUTABLE

print "promijenjen drugi element u 3",a

# matrix simulation with lists

matrica = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print "matrica je",matrica	#print whole matrix

print "prvi red ",matrica [0]	#print first row

print "treci element drugog reda ", matrica [1][2]	#print 3rd element from second row

# list comprehension expression - put it in [] to create list

secound_column = [ red [1] for red in matrica ]		# secound column from matrix, red is variable for iterating matrica elements

print "drugi stupac",secound_column

print [ red [2] for red in matrica if red [2] % 2 != 0] # print odd elements

print "dijagonala matrice je ", [ matrica [iteratoric][iteratoric] for iteratoric in [0,1,2]]

# contrroled and directed list cretion

listica = range ( 4 )

print "lista napravljena sa range-om",listica

listica = list ( range (4)) # in pzthon 3.x list *() is necesary range do not return list

print "lista napravljena sa range-om u python 3 stilu",listica

listica = range (-96 , 39 , 14) # range ( start, stop , step)

print "lista napravljena u rangeu sa step-om",listica

listica =  [[iteratoric, iteratoric * 2, iteratoric ** 2 ] for iteratoric in range (-23 , 29 , 3 ) if (iteratoric > 5 or iteratoric < -5 ) ]

print "lista napravljena range-om, negativnim stepom i if-om",listica

#listica = range ( 176.4 , - 22.8  , - 17)  error range operate with integers

listica = range ( 176 , - 22  , - 17)

print "lista napravljena range-om i negativnim stepom ",listica

print "lista prije inserta", a

a.insert (1,98765) # na drugo mjesto se stavlja objekt

print "lista poslije inserta", a  # dodan je novi element i svi elementi poslije njega su pomaknuti za jedno mjesto ulijevo

del a [3]	# mice se cetvrti element iz liste

print "lista poslije del-a", a  # uklonjen je element iz liste 

a.remove (-17)		# mi;e se objekt '-17' iy liste

print "lista poslije removea", a  # uklonjen je odredjeni objekt iz liste 



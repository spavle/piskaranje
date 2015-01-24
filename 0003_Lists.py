# Lists in python

# Lists are mutable and extendable and are sequence of objects ...

a = [ 1 , "asdf" , 3.14 ]

print a

a.append ( "novi element")		# adding element on end off list

print a

print a.pop ( 1 )			# getting and removing second element from list

print a,  len ( a )

a.sort () 	# list is now sorted

print a

a.reverse () 	# list is now reversed sorted

print a

a [ 1 ] = 3		# new value in second element of the list

print a

# matrix simulation with lists

matrica = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print matrica	#print whole matrix

print matrica [0]	#print first row

print matrica [1][2]	#print 3rd element from second row

# list comprehension expression

secound_column = [ red [1] for red in matrica ]		# secound column from matrix, red is variable for iterating matrica elements

print secound_column
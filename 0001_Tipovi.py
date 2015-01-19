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

# "Tipovi" su built in objects

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







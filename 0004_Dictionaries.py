# Dictionaries are key-value map  sequences

# - pristupa se po kljucu ne po poziciji
# - nesortirana/neporedana kolekcija bilo kakvih objekata
# - promjenjive duzine ( mutable ) sadrzi raznorodne objekte i moze se nestati do beskraja, neogranicena dubina
# - mutable maping objekt 
# - tablica referenci na objekte "hash table"

rjecnik = { 1 : 3 , 5 : "value" , 'key' : 12+7j ,  13.9 : [ 1 , 3 , 7 ]  } # uobicajeno kreiranje dictionarya keys i values su bilo koji objekti key mora biti "hashable"

print "vrijednost za kljuc 13.9 ==>",rjecnik [ 13.9 ]

print "poredak je slucajan", rjecnik

print "duzina dictionarya", len ( rjecnik )

print "dali je kljuc 2 u dictionaryu", 2 in rjecnik
print "dali je kljuc 1 u dictionaryu", 1 in rjecnik

print "svi kljucevi iz dictionarya", rjecnik.keys ()

rjecnik  [ 1 ] = 9 # kljucu 1 se dodaje nova vrijednost

print "nova vrijednost za kljuc 1", rjecnik

del rjecnik [ "key" ] # unistava se maping sa kljucem "key"

print "uklonjena vrijednost i kljuc", rjecnik

rjecnik  [ 22 ] = 7		#dodan novi maping

print "dictionary sa novim mapingom u sebi", rjecnik

print "rjecnik je tipa" , type ( rjecnik )

# pravljene dictionarya keywordom dict ()

bla='naslov'  #ovaj nece biti prihvaceno kao objekt referenca u slijedecoj liniji nego kao string
novi_rijecnik = dict (bla=1, bli=2 , blu=3 , ble='bleee') # izgeda da ovo prima samo stringove kao kljuceve 

print "novi rijecnik" , novi_rijecnik

novi_rijecnik2 =  {'bla':'bli' , 'blu':1 , 2:'ble' , 3:4}
print "novi rijecnik2" , novi_rijecnik2

novi_rijecnik2 = dict ( {'bla':'bli' , 'blu':1 , 2:'ble' , 3:4} )	#glupost
print "novi rijecnik2" , novi_rijecnik2

novi_rijecnik2 = dict ( zip ([ 'bla', 'blu',2,3],[ 'bli',1,'ble',4] )	)
print "novi rijecnik2" , novi_rijecnik2

novi_rijecnik2 = dict ( [ ('bla','bli') , ('blu',1) , (2,'ble') , (3,4) ] )	#LISTA "PAROVA"
print "novi rijecnik2" , novi_rijecnik2





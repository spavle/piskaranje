# Touples are sequences of IMMUTABLE OBJECTS

nesto = ( 3, "bal", 51.9 , 7+3j, [ 2 , 6 , 'ina'] )

print "Touple", nesto

# touple je sequenca i ima iterator i sve ostalo
print nesto [ 2: ]

for a in nesto:
   print a

# vrijedi sve kao za listu samo je immutable

print "touple", nesto , "ima" , len ( nesto ) , "elemenata"

# trazenje elementa

print " 'bal' je u toupleu ",nesto.index ('bal')+1,'. po redu, a nalazi se na indexu  ',nesto.index('bal')
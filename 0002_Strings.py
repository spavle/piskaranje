# Sequences of unicode chars

# String a imutable once created it can not be changed

a = 'Pero jede jagode  '

print a
#a [ 6 ] = 'M' --> this will produce error
print a

a = a [ :6 ] + 'M' + a [ 7:] # this will create new string and nonect it with name a
print a

# Find first offset of substring

print a.find ( 'e' )
print a.find ( 'ago' )

# find substring and replace with provided WARRNING method create new string because strings are immutable

print a.replace ( 'jagode' , 'kukuruz' )
print a										#original object is intacted

# split string in list of strings by provided delimiter

print a.split ( 'de' )

# strip whitespaces from right

print a.rstrip ()

# is it leters

print a.isalpha ()
print 'pero'.isalpha ()

# to uppercase

print a.upper ()

#execution chain

print a.replace ( 'jagode' , 'kukuruz' )
print a.replace ( 'jagode' , 'kukuruz' ).upper ()
print a.replace ( 'jagode' , 'kukuruz' ).upper ().split ( 'MDE' )

# string formating

# old-school

print 'Pero %s jede %s Jagode' % ( 'bum' , 'BUM' )

# extended and indexed by .format method on string

print 'Pero {0} jede {1} Jagode'.format ( 'bum' , 'BUM' )
print 'Pero {1} jede {0} Jagode'.format  ( 'bum' , 'BUM' )

# extended and positional, non - indexed

print 'Pero {} jede {} Jagode'.format ( 'bum' , 'BUM' , 'Bam')

# multiline strings determined by triple quotes

m = """ pero
jede
jagode

"""

print m

# inicode

print a
print a.encode ( 'utf8' )
print a.encode ( 'utf16' )
# print a.encode ( 'utf16' ).decode( 'latin1' ) ????




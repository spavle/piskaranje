# Jako cesto koristeni python objekti
# TODO: provjeriti dali se ponasaju kao unix streams, redirekcija, file descriptori stdin, stdout, stderrr ....

# osnovni nacin kreiranja keyword open
# ima sys.stdout !

fajla = open ("zbrlj.txt","w")

fajla.write ( "Bok\n" )
fajla.write ( "oyla\n")

fajla.close()
# ovo pise stalno od pocetka fajle kao sto se vidi iz testa dolje
fajla = open ("zbrlj.txt","r")

tekst = fajla.read()

print tekst

# gdje sam 

import os

print("Path at terminal when executing this file")
print(os.getcwd() + "\n")

# listanje svih fajli u cwd
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
   print f
   
# i file objekt ima iterator

for lajna in open ('zbrlj.txt'):
   print lajna




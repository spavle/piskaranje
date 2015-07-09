# prvo importi
import os,sys 	# oba za svaki slucaj
import re		# ubaci regular expression
# programske konstante
radni_dir = "C:\\rad"
popis_fajli = []
# pozicioniraj se 
os.chdir ( radni_dir )
#gdjesam = os.getcwd()
#print gdjesam

# izlistaj datoteke (development poslije disable)

for subdir, dirs, files in os.walk('./'):		#rekurzivno prolazi cijelo stablo
#   print "subdiri: ", subdir
#   print "diri: ", dirs
#   print "Datoteke: -------------------------------------------------------"
#   print files
#   print type (files)
   for file in files:
      B = re.search ( r'WoWScrnShot_(\d{6})_(\d{6})\.jpg' , file )
      if B:
#         print file, "Drugi B"  , B.group ()
         popis_fajli.append ( file )	#dodaj pronadjeno u listu
   break		# ne idi u poddirektorije


# izlistaj datoteke pronadjene po filteru

# print "pronasao " , popis_fajli

# prodji po listi , kreiraj novo ime datoteke, muvaj datoteku u novo ime

for slika in popis_fajli:
   novoime = "MyWoWmeme_20" + slika [16:18] + "_"  + slika [12:14] + "_"  + slika [14:16] + "_" + slika [19:25] + ".jpg"

   print slika, " ---> ", novoime
#   print " Godina ", slika [16:18]
#   print " Mjesec ", slika [12:14]
#   print " Dan ", slika [14:16]
   os.rename ( slika , novoime )
   

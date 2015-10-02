# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#mossy coblestone tijelo
crtaj_kvadar ( orMj , (9,-41,-13)  , (43,41,1) , orSm , 98 , 1 )
crtaj_kvadar ( orMj , (22,-40,-13)  , (42,40,-13) , orSm , 3 )


#2 kocke ravno
crtaj_kvadar ( orMj , (1,-2,0)  , (2,2,1) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (1,-2,-1)  , (2,2,-1) , orSm , 3 )

#3 kocke ravno podignut strop
crtaj_kvadar ( orMj , (2,-2,0)  , (6,2,2) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (2,-2,-1)  , (6,2,-1) , orSm , 3 )

#4 stepenice dolje
for br in range (5):
   crtaj_kvadar ( orMj , (6+br,-2,0-br)  , (6+br,2,3-br) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (6+br,-2,-1-br)  , (6+br,2,-1-br) , orSm , 3 )
   
# podest 6 x 7
crtaj_kvadar ( orMj , (10,-3,-4)  , (16,3,0) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (10,-3,-5)  , (16,3,-5) , orSm , 3 )

# lijeve stepenice 3 dolje

for br in range (4):
   crtaj_kvadar ( orMj , (10,-4 - br ,-4 -br)  , (16,-4 -br,0) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (10,-4 - br ,-5 -br)  , (16,-4 -br,-5 -br) , orSm , 3 )

# desne stepenice 3 dolje

for br in range (4):
   crtaj_kvadar ( orMj , (10,4 + br ,-4 -br)  , (16,4 +br,0) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (10,4 + br ,-5 -br)  , (16,4 +br,-5 -br) , orSm , 3 )
   
#lijevi podest
crtaj_kvadar ( orMj , (10,-8,-8)  , (16,-14,0) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (10,-8,-9)  , (16,-14,-9) , orSm , 3 )

#desni podest
crtaj_kvadar ( orMj , (10,8,-8)  , (16,14,0) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (10,8,-9)  , (16,14,-9) , orSm , 3 )

# lijeve stepenice 5 dolje
for br in range (5):
   crtaj_kvadar ( orMj , (17+br,-8,-8-br)  , (17+br,-14,0) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (17+br,-8,-9-br)  , (17+br,-14,-9-br) ,  orSm , 3 )

# desne stepenice 5 dolje
for br in range (5):
   crtaj_kvadar ( orMj , (17+br,8,-8-br)  , (17+br,14,0) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (17+br,8,-9-br)  , (17+br,14,-9-br) , orSm , 3 )
   

# prvi volumen od ruba do ruba stepenica
crtaj_kvadar ( orMj , (22,-40,-12)  , (42,40,0) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (22,-40,-13)  , (42,40,-13) , orSm , 3 )


# srednji volumen izmedu stepenica
crtaj_kvadar ( orMj , (17,-7,-12)  , (21,7,0) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (17,-7,-13)  , (21,7,-13) , orSm , 3 )

#lijevi volumen iza stepenica
crtaj_kvadar ( orMj , (10,-15,-12)  , (21,-40,0) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (10,-15,-13)  , (21,-40,-13) , orSm ,3 )

#desni volumen iza stepenica
crtaj_kvadar ( orMj , (10,15,-12)  , (21,40,0) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (10,15,-13)  , (21,40,-13) , orSm , 3 )
# podzemna citadela SA GALERIJOM OKOLO

from crtanje import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

sirina = 40
dubina = 50

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#mossy coblestone tijelo
crtaj_kvadar ( orMj , (8, -sirina-4,-16)  , (8 + 6 + 4 + dubina,sirina + 4,1) , orSm , 98 , 1 )
crtaj_kvadar ( orMj , (11+3,-sirina,-16)  , (11+3 + dubina ,sirina,-16) , orSm , 3 )

crtaj_kvadar ( orMj , (11,-sirina - 3,-5)  , (11+6+dubina,sirina +3,0) , orSm , AIR.id , blok_dv = 0 )   #podest okolo
crtaj_kvadar ( orMj , (11+3,-sirina ,-15)  , (11+3+dubina,sirina ,0) , orSm , AIR.id , blok_dv = 0 )     #centralna rupa

#2 kocke ravno
crtaj_kvadar ( orMj , (1,-2,0)  , (2,2,1) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (1,-2,-1)  , (2,2,-1) , orSm , 3 )

#4 kocke ravno podignut strop
crtaj_kvadar ( orMj , (3,-2,0)  , (6,2,2) , orSm , AIR.id , blok_dv = 0 )
crtaj_kvadar ( orMj , (3,-2,-1)  , (6,2,-1) , orSm , 3 )
crtaj_kvadar ( orMj , ( 4 , -3 , 2 )  , ( 4 , -3 , 2 ) , orSm , 89 ) #prvi par lampi na sredini zida
crtaj_kvadar ( orMj , ( 4 , 3 , 2 )  , ( 4 , 3 , 2 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 7 , -3 , 0 )  , ( 7 , -3 , 0 ) , orSm , 89 ) #drugi par lampi iznad pocetka stepenica
crtaj_kvadar ( orMj , ( 7 , 3 , 0 )  , ( 7 , 3 , 0 ) , orSm , 89 )

#4 stepenice dolje
for br in range (5):
   crtaj_kvadar ( orMj , (6+br,-2,0-br)  , (6+br,2,3-br) , orSm , AIR.id , blok_dv = 0 )
   crtaj_kvadar ( orMj , (6+br,-2,-1-br)  , (6+br,2,-1-br) , orSm , 3 )
   
# podest 9 x 7 +++
crtaj_kvadar ( orMj , (11,-3,-6)  , (19,3,-16) , orSm ,98 , 1 )
crtaj_kvadar ( orMj , (11,-3,-6)  , (19,3,-6) , orSm , 3 )
crtaj_kvadar ( orMj , ( 19 , -3 , -5 )  , ( 19 , -3 , -5 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 19 , 3 , -5 )  , ( 19 , 3 , -5 ) , orSm , 89 )

# lijeve stepenice 3 dolje
for br in range (4):
   crtaj_kvadar ( orMj , (14,-4 - br ,-7 -br)  , (19,-4 -br,-16) , orSm , 98 , 1 )
   crtaj_kvadar ( orMj , (14,-4 - br ,-6 -br)  , (19,-4 -br,-6 -br) , orSm , 3 )

# desne stepenice 3 dolje
for br in range (4):
   crtaj_kvadar ( orMj , (14,4 + br ,-7 -br)  , (19,4 +br,-16) , orSm ,  98 , 1 )
   crtaj_kvadar ( orMj , (14,4 + br ,-6 -br)  , (19,4 +br,-6 -br) , orSm , 3 )
   
#lijevi podest
crtaj_kvadar ( orMj , (14,-7,-10)  , (19,-12,-16) , orSm ,  98 , 1 )
crtaj_kvadar ( orMj , (14,-7,-9)  , (19,-12,-9) , orSm , 3 )
crtaj_kvadar ( orMj , ( 19 , -12 , -8 )  , ( 19 , -12 , -8 ) , orSm , 89 )

#desni podest
crtaj_kvadar ( orMj , (14,7,-10)  , (19,12,-16) , orSm ,  98 , 1 )
crtaj_kvadar ( orMj , (14,7,-9)  , (19,12,-9) , orSm , 3 )
crtaj_kvadar ( orMj , ( 19 , 12 , -8 )  , ( 19 , 12 , -8 ) , orSm , 89 )

#lijeve stepenice 5 dolje
for br in range (6):
   crtaj_kvadar ( orMj , (20+br,-7,-11-br)  , (20+br,-12,-16) , orSm ,  98 , 1 )
   crtaj_kvadar ( orMj , (20+br,-7,-10-br)  , (20+br,-12,-10-br) ,  orSm , 3 )
crtaj_kvadar ( orMj , ( 19 , -5 , -14 )  , ( 19 , -5 , -14 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 26 , -13 , -15 )  , ( 26 , -13 , -15 ) , orSm , 89 )


#desne stepenice 5 dolje
for br in range (6):
   crtaj_kvadar ( orMj , (20+br,7,-11-br)  , (20+br,12,-16) , orSm ,  98 , 1 )
   crtaj_kvadar ( orMj , (20+br,7,-10-br)  , (20+br,12,-10-br) , orSm , 3 )
crtaj_kvadar ( orMj , ( 19 , 5 , -14 )  , ( 19 , 5 , -14 ) , orSm , 89 )
crtaj_kvadar ( orMj , ( 26 , 13 , -15 )  , ( 26 , 13 , -15 ) , orSm , 89 )

#lampe okolo

for br in range ( 5 , sirina + 1, 5 ) :   # lampe na podestu napred/nazad
   crtaj_kvadar ( orMj , (10,br,-2)  , (10,br,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (10,-br,-2)  , (10,-br,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (16+dubina+2,br,-2)  , (16+dubina+2,br,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (16+dubina+2,-br,-2)  , (16+dubina+2,-br,-2) , orSm , 89 )
   
for br in range ( 5 , dubina + 1, 5 ) :   # lampe na podestu lijevo/desno
   crtaj_kvadar ( orMj , (10+ br,sirina + 4,-2)  , (10 + br,sirina + 4,-2) , orSm , 89 )
   crtaj_kvadar ( orMj , (10+ br,-sirina - 4,-2)  , (10 + br,-sirina - 4,-2) , orSm , 89 )

for br in range ( 5 , sirina + 1, 5 ) :   # lampe na dnu napred/nazad
   crtaj_kvadar ( orMj , (13,br,-14)  , (13,br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13,br,-9)  , (13,br,-9) , orSm , 89 )
   crtaj_kvadar ( orMj , (13,-br,-14)  , (13,-br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13,-br,-9)  , (13,-br,-9) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+dubina+2,br,-14)  , (13+dubina+2,br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+dubina+2,br,-9)  , (13+dubina+2,br,-9) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+dubina+2,-br,-14)  , (13+dubina+2,-br,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+dubina+2,-br,-9)  , (13+dubina+2,-br,-9) , orSm , 89 )
   
for br in range ( 5 , dubina + 1, 5 ) :   # lampe dnu lijevo/desno
   crtaj_kvadar ( orMj , (13+ br,sirina+1 ,-14)  , (13 + br,sirina +1,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+ br,sirina+1 ,-9)  , (13 + br,sirina +1,-9) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+ br,-sirina-1 ,-14)  , (13 + br,-sirina-1 ,-14) , orSm , 89 )
   crtaj_kvadar ( orMj , (13+ br,-sirina-1 ,-9)  , (13 + br,-sirina-1 ,-9) , orSm , 89 )


#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


for br in range (0,4) :

   crtaj_stepenice ( gdjeSam () , ( 3 + 2 * br , -1 , 0 )  , ( 3 + 2 * br  , 1 , 0 ) , gdjeGledam ()  ,  br  )
#crtaj_stepenice ( origin , poc  , smjer , blok_id = 53 , rel_smjer = 0  , gore_dolje = 0  )

   
"""


crtaj_kvadar ( gdjeSam () , ( 1 , 0 , 0 )  , ( 3 , 0 , 2 ) , gdjeGledam () , 1 ) 
#crtaj_kvadar ( gdjeSam () , ( 2 , 0 , 0 )  , ( 2 ,0 , 1 ) , gdjeGledam () , 0 ) 
crtaj_vrata ( gdjeSam () , ( 2 , 0 , 0 )  , gdjeGledam () , 3 )

"""
# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
import time 
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 1
dv = 1

#prvi red
crtaj_kvadar ( orMj , [ 2  , 0, 0 ]  , [ 2  , 4 , 0  ] , orSm , materijal , dv ) # temeljniblok
crtaj_redstonedust ( orMj , [ 2 , 0, 1 ]  , [ 2 ,  0 , 1  ] , orSm )
crtaj_repeater ( orMj , [ 2 , 1, 1 ]  , [ 2 ,  1 , 1  ] , orSm , rel_smjer  = "desno" )
crtaj_kvadar ( orMj , [ 2  , 2, 1 ]  , [ 2  , 2 , 1  ] , orSm , materijal , dv )
crtaj_redstonetorch ( orMj , [ 2  , 3, 1 ]   ,  orSm  , "desno" ) 
time.sleep ( 1 ) 

#drugi red
crtaj_kvadar ( orMj , [ 2  , 1, 2 ]  , [ 2  , 1 , 2  ] , orSm , materijal , dv )
crtaj_redstonetorch ( orMj , [ 2  , 0, 2 ]   ,  orSm  , "lijevo" )  
crtaj_comparator ( orMj , [ 2  , 2, 2 ]  , [ 2  , 2 , 2  ]  , orSm , rel_smjer  = "lijevo" )
crtaj_dropper    ( orMj , [ 2  , 3, 2 ]  , [ 2  , 3 , 2  ]  , orSm , rel_smjer  = "gore" )
crtaj_hopper    ( orMj , [ 2  , 4, 2 ]  , [ 2  , 4 , 2  ] , orSm , "lijevo" )
time.sleep ( 1 )

#treci red
crtaj_kvadar ( orMj , [ 2  , 0, 3 ]  , [ 2  , 0 , 3  ] , orSm , materijal , dv )
crtaj_redstonetorch ( orMj , [ 2  , 1, 3 ]   ,  orSm  , "desno" )
crtaj_dropper    ( orMj , [ 2  , 3, 3 ]  , [ 2  , 3 , 3  ]  , orSm , rel_smjer  = "gore" )
crtaj_kutiju ( orMj , [ 2 , 4, 3 ]  , [ 1 ,  4 , 3  ] , orSm , rel_smjer  = "desno" , blok_id = 54     )
time.sleep ( 1 )

for br in range ( 0 , 61 , 2 ):
   #cetvrti red

   crtaj_kvadar ( orMj , [ 2  , 1, 4 + br  ]  , [ 2  , 1 , 4  + br ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 0, 4 + br ]   ,  orSm  , "lijevo" )  
   crtaj_redstonetorch ( orMj , [ 2  , 2, 4 + br ]   ,  orSm  , "desno" )
   crtaj_dropper    ( orMj , [ 2  , 3, 4 + br ]  , [ 2  , 3 , 4 + br  ]  , orSm , rel_smjer  = "gore" )
   #time.sleep ( 1 )

   # peti red

   crtaj_kvadar ( orMj , [ 2  , 0, 5 + br ]  , [ 2  , 0 , 5  + br ] , orSm , materijal , dv )
   crtaj_redstonetorch ( orMj , [ 2  , 1, 5  + br]   ,  orSm  , "desno" )
   crtaj_dropper    ( orMj , [ 2  , 3, 5 + br ]  , [ 2  , 3 , 5  + br ]  , orSm , rel_smjer  = "gore" )
   #time.sleep ( 1 )
   
crtaj_kvadar ( orMj , [ 2  , 1, 66  ]  , [ 2  , 1 , 66 ] , orSm , materijal , dv )
crtaj_redstonetorch ( orMj , [ 2  , 0, 66 ]   ,  orSm  , "lijevo" )  
crtaj_redstonetorch ( orMj , [ 2  , 2, 66 ],  orSm  , "desno" )
crtaj_dropper    ( orMj , [ 2  , 3, 66 ]  , [ 2  , 3 , 66  ]  , orSm , rel_smjer  = "gore" )
   
#kutija na vrhu

crtaj_kutiju ( orMj , [ 2 , 3, 67 ]  , [ 2 ,  4 , 67  ] , orSm , rel_smjer  = "meni" , blok_id = 54     )











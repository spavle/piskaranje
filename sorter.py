# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#sandstone glatki
materijal = 24
dv = 2

def pocetak_sortera () :
   crtaj_hopper    ( orMj , [ 2  , 1, 4 ]  , [ 2 ,  1 , 4  ] , orSm , "odmene" ) # gornji
   crtaj_kutiju ( orMj , [ 1 , 1, 5 ]  , [ 2 ,  1 , 5  ] , orSm , rel_smjer  = "lijevo" )

def crtaj_modul ( dX  ):
   """
   dx - udaljenost modula
   koja_kutija - par - obicna , nepar - traped
   """
   """
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv  )
   """
   crtaj_kvadar ( orMj , [ 3 + dX , 0, 0 ]  , [ 3 + dX , -2 , 2  ] , orSm , materijal , 2 ) # blok
   crtaj_kvadar ( orMj , [ 3 + dX , -2, 2 ]  , [ 3 + dX ,  -2 , 2  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , -1, 1 ]  , [ 3 + dX ,  -1 , 1  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , 0, 0 ]  , [ 3 + dX ,  0 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_kvadar ( orMj , [ 3 + dX , -2, 0 ]  , [ 3 + dX ,  -2 , 0  ] , orSm , 0 , 0 ) # zrak
   crtaj_redstonedust ( orMj , [ 3 + dX , -2, 2 ]  , [ 3 + dX ,  -2 , 2  ] , orSm )
   crtaj_redstonedust ( orMj , [ 3 + dX , -1, 3 ]  , [ 3 + dX ,  -1 , 3  ] , orSm )
   crtaj_redstonetorch ( orMj , [ 3 + dX , 1, 1 ]  ,  orSm  , "desno" )  
   crtaj_comparator ( orMj , [ 3 + dX , 0, 3 ]  , [ 3 + dX ,  0 , 3 ]  , orSm , rel_smjer  = "lijevo" )
   crtaj_repeater ( orMj , [ 3 + dX , -1, 1 ]  , [ 3 + dX ,  -1 , 1  ]  , orSm , rel_smjer  = "desno" )
   
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 2 ]  , [ 3 + dX ,  1 , 3  ] , orSm , "desno" ) # dva doljnja
   crtaj_hopper    ( orMj , [ 3 + dX , 1, 4 ]  , [ 3 + dX ,  1 , 4  ] , orSm , "odmene" ) # gornji
   
   kutija = 54
   tkutija = 146
   if ( int ( dX ) % 2 == 1 ) :
      kmat = kutija
   else :
      kmat = tkutija
   crtaj_kutiju ( orMj , [ 3 + dX , 2, 2 ]  , [ 3 + dX ,  3 , 2  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     )
   crtaj_hopper    ( orMj , [ 3 + dX , 3, 1 ]  , [ 3 + dX ,  3 , 0  ] , orSm , "desno" ) # hopper ispod kutije
   crtaj_kutiju ( orMj , [ 3 + dX , 4, 1 ]  , [ 3 + dX ,  5 , 0  ] , orSm , rel_smjer  = "meni" , blok_id = kmat     ) # dodatne kutije
   
   
   
pocetak_sortera ()
   
for br in range ( 0, 45 ):
   crtaj_modul ( br )

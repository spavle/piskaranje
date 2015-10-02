#definicija objekta i poziv rutine za crtanje & LAME TOOL
from crtanje import *		#tu je funkcija koju zovem
from crtanje2 import *		#tu je funkcija koju zovem
from mc import *			

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

crtaj_kvadar ( gdjeSam () , [ 1 , 0 , -1  ]  , [ 62 , 0 , -1  ] , gdjeGledam () , 2 , 0 )
#crtaj_kvadar ( gdjeSam () , [ 2 , -3 , -1 ]  , [ 2 , 30 , 4  ] , gdjeGledam () , 5 , 0 )

"""
podloga stepenica
for dd in range ( 0 , 6 ) :
   crtaj_kvadar ( gdjeSam () , [ 1 , - dd , dd ]  , [ 13 , -dd , dd  ] , gdjeGledam () , 5 , 0 )

oak fence	85   
spruce_fence	188
"""
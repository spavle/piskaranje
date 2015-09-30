# crtanje automatizirani sorter
#definicija objekta i poziv rutine za crtanje
import time 
import sys
from crtanje import *		#tu je funkcija koju zovem

from mc import *			
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom




print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
print '/give spavle axe'

# origin ispred na sredini 
orMj = gdjeSam ()
orSm = gdjeGledam ()

#oakwood slab
materijal = 126
dv = 8


#crtaj_kvadar ( orMj , ( 1  , -1 , -1 ) , ( 3 , 1 , -1 ) , orSm , materijal , dv ) # zrak iznad stepenica

bla = rel2abs ( orMj , ( 5  , 0 ,  0  ) , orSm )

#mc.setBlockWithNBT(bla,63,5,"{id:\"Sign\",Text1:\"Line1\",Text2:\"Pablo\",Text3:\"Line3\",Text4:\"Line4\"}")

#mc.setBlockWithNBT(bla,54,1, "{id:\"Chest\",CustomName:\"GLUPOST\",Items:[0:{Slot:1b,id:\"minecraft:diamond_axe\",Count:25b,Damage:0s,},1:{Slot:13b,id:\"minecraft:dirt\",Count:22b,Damage:0s,},]}" )
bla = rel2abs ( orMj , ( 1  , 0 ,  0  ) , orSm )
print ( mc.getBlockWithNBT (bla) )
#[12:09:39] [Thread-248/INFO]: [CHAT] Block(54, 2, '{Items:[0:{Slot:1b,id:"minecraft:diamond_axe",Count:1b,Damage:0s,},1:{Slot:13b,id:"minecraft:dirt",Count:22b,Damage:0s,},],id:"Chest",Lock:"",}')

"""
mc.postToChat("gdjex: %s " % ( bla ) )

#mc.setBlock (bla [ 0 ],bla [ 1 ],bla [ 2 ],63,1, "{id:\"Sign\",TTTText1:\"Line1\",Text2:\"Line2\",Text3:\"Line3\",Text4:\"Line4\"}")

mc.conn.send("world.setBlock",bla [ 0 ],bla [ 1 ],bla [ 2 ],63,1,"{id:\"Sign\",Text1:\"Line1\",Text2:\"Line2\",Text3:\"Line3\",Text4:\"Line4\"}")

mc.setBlock(-1,-1,-1,1)
mc.conn.send("world.setBlocks",1,4,0,1,0,0,63,4,"{id:\"Sign\",Text1:\"AAAAAAPablo\,Text2:\"Line2\"}")
"""


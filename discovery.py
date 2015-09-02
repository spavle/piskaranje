import time 
from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


   
   
  

  
  
  
  
  
def go_south ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.player.setPos(pos.x - pomak , 180 , pos.z)
      time.sleep ( 3 )
      
def go_west ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.player.setPos(pos.x  , 180 , pos.z - pomak)
      time.sleep ( 3 )
      
      
def go_north ( koliko , pomak ) :
   for brojalica in range ( 0 , koliko ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.player.setPos(pos.x + pomak , 180 , pos.z)
      time.sleep ( 3 )
def go_east ( koliko , pomak ) :
   for brojalica in range (  0 , koliko ):
      mc.postToChat("brojalica : %f " % ( brojalica  ) )
      pos = mc.player.getTilePos()
      mc.player.setPos(pos.x  , 180 , pos.z + pomak)
      time.sleep ( 3 )
      
korak = 25
pocetak =  mc.player.getTilePos()
for krug in range ( 2 , 250 , 2) :
   mc.postToChat("krug : %f " % ( krug  ) )
   go_south ( 1 , korak )
   go_west ((krug / 2 + 1 ) , korak )
   go_north ( krug , korak )
   go_east ( krug , korak )
   go_south ( krug , korak )
   go_west ((krug / 2 + 1 ) , korak )
   
mc.player.setPos( pocetak.x ,  pocetak.y ,  pocetak.z )
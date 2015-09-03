
#ispred lika cisti trapezoidni lik i to samo blokove iz liste 

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def Kanal ():
   """
   ispred lika cisti trapezoidni lik i to samo blokove iz liste
   """
   zaMaknuti = [ SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id]
   zaMaknutiOpasno = [ WATER_FLOWING.id , WATER_STATIONARY.id , LAVA_FLOWING.id , LAVA_STATIONARY.id]
   #gdje sam
   radnaPozicija = mc.player.getPos()		
   #kamo gledam
   smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
   #smjer gledanja radi preglednosti spremimo u "vektor""
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)
   # nadji stepenice 
   stepenice_marker = 1
   udaljenost = 1 # ovdje pise koliko je daleko
   dZ = 0   # ne provjeravamo po lijevo desno
   while ( stepenice_marker == 1 ) :      #trazi se 128 sandstone
      gdjeX=radnaPozicija.x + Vx*( - udaljenost ) + Vz*dZ    		# pomak po x
      gdjeY=radnaPozicija.y + ( - udaljenost )						# pomak po y
      gdjeZ=radnaPozicija.z + Vx*dZ + Vz*( - udaljenost )			# pomak po Z
      if ( mc.getBlock ( gdjeX , gdjeY , gdjeZ ) == 128 ) :
         stepenice_marker = 0
      else :
         udaljenost += 1
   
   #for dubina in range ( 2 ) : # ili ici jedan po jedan
   # postavi nove stepenice
      
   # ochisti ispod i u nivou
   
   # napravi kanal
      
      
     
        

   
   
   
   
   
   
Kanal ()
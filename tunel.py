#ispred lika cisti pravokutnik  3x5 i dugacak 100 i to samo blokove iz liste poplocen glovestone

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def tunel ():
   """
   iispred lika cisti pravokutnik  3x5 i dugacak 100 i to samo blokove iz liste poplocen glovestone
   """
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
   #mc.postToChat("vX: %f vZ: %f " % ( Vx , Vz  ) )

   #crtanje
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45
      for dZ in  range( -1 , 2 ) :    		# prodji cijeli pravokutnik
         for dY  in  range ( -1 , 5 ) : 
            for dX in  range ( 1 , 101  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               if dY == -1 :
                  mc.setBlock( gdjeX , gdjeY , gdjeZ , 89 )		#u podlogu obavezno stavi glowstone
               elif mc.getBlock ( gdjeX , gdjeY , gdjeZ ) in zaMaknuti :
                  mc.setBlock(gdjeX , gdjeY , gdjeZ , AIR)			#postavi blok
   return 1

   
   
zaMaknuti = [ SAND.id , STONE.id , DIRT.id , GRAVEL.id , GRASS.id , GRASS_TALL.id , COBBLESTONE.id , WATER_FLOWING.id , WATER.id , LAVA_FLOWING.id , LAVA.id ]

tunel ()
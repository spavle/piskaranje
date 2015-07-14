#ispod lika radi piramidu

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def chep ():
   """
   funkcija za crtanje chepa od pjeska dimenzija 9x3x3 neposredno ispred lika
   """
   #gdje sam
   radnaPozicija = mc.player.getPos()	
   radnaPozicija.y -= 1
   #mc.postToChat("vX: %f vZ: %f " % ( Vx , Vz  ) )
   sirina = 0		#pocetna sirina je 0
   #crtanje
   mc.setBlock(radnaPozicija.x  , radnaPozicija.y  , radnaPozicija.z , GOLD_BLOCK)
   while 1 :		# ne pod 45
      sirina += 1
      for dZ in  range( -sirina , sirina +1) :    		# prodji chep
         mc.setBlock(radnaPozicija.x + sirina , radnaPozicija.y - sirina , radnaPozicija.z + dZ , DIAMOND_BLOCK)			#postavi blok   
         #mc.setBlock(radnaPozicija.x + sirina , radnaPozicija.y - sirina , radnaPozicija.z - dZ , DIAMOND_BLOCK)			#postavi blok   
         mc.setBlock(radnaPozicija.x - sirina , radnaPozicija.y - sirina , radnaPozicija.z + dZ , DIAMOND_BLOCK)			#postavi blok   
         #mc.setBlock(radnaPozicija.x - sirina , radnaPozicija.y - sirina , radnaPozicija.z - dZ, DIAMOND_BLOCK)			#postavi blok   
         mc.setBlock(radnaPozicija.x + dZ , radnaPozicija.y - sirina , radnaPozicija.z + sirina , DIAMOND_BLOCK)			#postavi blok   
         mc.setBlock(radnaPozicija.x - dZ , radnaPozicija.y - sirina , radnaPozicija.z - sirina , DIAMOND_BLOCK)			#postavi blok   
         if mc.getBlock ( radnaPozicija.x , radnaPozicija.y - sirina , radnaPozicija.z ) == BEDROCK.id :
            return 1
   return 1
   
chep ()
#ispred lika vrt

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def vrt ():
   """
   funkcija za crtanje chepa od pjeska dimenzija 9x3x3 neposredno ispred lika
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
      for dZ in  range( -5 , 6 ) :    		# prodji chep
         for dY  in  range ( 0,1 ) : 
            for dX in  range ( 1 , 12  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               mc.setBlock(gdjeX , gdjeY , gdjeZ , 1)			#postavi blok kamenja
      for dZ in  range( -4 , 5 ) :    		# prodji chep
         for dY  in  range ( 0,1  ) : 
            for dX in  range ( 2 , 11  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               mc.setBlock(gdjeX , gdjeY , gdjeZ , 60)			#postavi blok farmlanda
      for dZ in  range ( 0 , 1 ) :    		# prodji chep
         for dY  in  range ( 0,1 ) : 
            for dX in range ( 6 , 7  ) :
               gdjeX=radnaPozicija.x + Vx*dX + Vz*dZ    		# pomak po x
               gdjeY=radnaPozicija.y + dY
               gdjeZ=radnaPozicija.z + Vx*dZ + Vz*dX			# pomak po Z
               mc.setBlock(gdjeX , gdjeY , gdjeZ , 9)			#postavi blok voda

   return 1
   
vrt ()
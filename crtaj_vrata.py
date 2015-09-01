#crta vrata na zadanim koordinatama zadane vrste

from mc import * #import api-ja
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def crtaj_vrata (X1,Y1,Z1,koja_vrata=195):   
   """
   funkcija za crtanje vrata na zadanim koordinatama zadane vrste
   X1,Y1,Z1 - pozicija
   koja_vrata - koja vrata default obicna
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

   #crtanje
   if  abs ( Vx )  != abs ( Vz ) :		# ne pod 45

      gdjeX1=radnaPozicija.x + Vx*X1 + Vz*Z1    # modificiraj pocetnu koordinatu
      gdjeY1=radnaPozicija.y + Y1
      gdjeZ1=radnaPozicija.z + Vx*Z1 + Vz*X1
      mc.setBlock ( gdjeX1 , gdjeY1 , gdjeZ1 , koja_vrata , 0 ) # doljnji dio vrata
      gdjeY1=radnaPozicija.y + 1
      mc.setBlock ( gdjeX1 , gdjeY1 , gdjeZ1 , koja_vrata , 8 ) # gornji dio vrata
   return 1
   

   

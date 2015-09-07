# crta objekt zadan u dostavljenoj listi
from mc import * # ajmo probati ovaj import
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

def crtanje (ulaz):
   """
   funkcija za crtanje prima listu listi sa po 4 parametra
   1. parametar x koordinata
   2. parametar z koordinata
   3. parametar y koordinata
   4. parametar id bloka koji se postavlja
   """
   #gdje sam detaljno
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
      for brojalica in ulaz :    		# prodji listu
         gdjex=radnaPozicija.x + Vx*brojalica [0] - Vz*brojalica[1]    		# pomak po x
         gdjez=radnaPozicija.z + Vx*brojalica[1] + Vz*brojalica[0]			# pomak po y
         #mc.postToChat("gdjex: %f gdjez: %f z-os: %f " % ( gdjex , gdjez , brojalica [1] ) )
         mc.setBlock(gdjex , brojalica[2] , gdjez , brojalica[3], brojalica[4])			#postavi blok
   return 1
   
def rel2abs ( inPoz ,  dPoz  , smjer  ) :
   """
   funkcija za pretvaranje relativnih u apsolutne koordinate  prima parametre: 
   1. Parametar inPoz
      1. parametar origin x koordinata
      2. parametar origin z koordinata
      3. parametar origin y koordinata
   2. Parametar dPoz
      1. parametar dX
      2. parametar dZ
      3. parametar dY
   3. smjer
      1. Vx smjer
      2. Vy smjer gledanja
   
   DEFAULT: "gleda prema" X pozitivnoj osi
   
   vraca listu sa 3 koordinate
   
   1. x
   2. y
   3. z
   """
   if  abs ( smjer [0] )  != abs ( smjer [1] ) :		# ne pod 45
      """
      gdjeX=inX + Vx*dX - Vz*dZ    		# pomak po x
      gdjeZ=inZ + Vx*dZ + Vz*dX			# pomak po y
      gdjeY  = inY + dY
      """
      gdjeX=inPoz [0] + smjer [0]*dPoz[0] - smjer [1]*dPoz[1]    		# pomak po x
      gdjeZ=inPoz [1] + smjer [0]*dPoz[1] + smjer [1]*dPoz[0]			# pomak po y
      gdjeY  = inPoz [2] + dPoz[2]
      
   return (  [ gdjeX , gdjeY , gdjeZ  ] )
   
def crtaj_tocku ( inLista , blok_id , blok_dv = 0 , pomakX = 0 , pomakZ = 0 ) :
   """
   funkcija za crtanje tocke
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. koji blok 
   3. koja varijanta bloka DFAULT osnovni oblik
   4. pomak po X osi
   5. pomak po Z osi 
   """
   mc.setBlock( inLista [ 0 ] , inLista [ 1 ], inLista [ 2 ] , blok_id , blok_dv )
   return
 

def crtaj_bitmap ( inOrigin ,  smjer , inBitmap , pomakX = 0 , pomakZ = 0) :
   """
   funkcija za crtanje bitmape
   funkcija za crtanje tocke
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. smjer
   3. bitmapa
   4. pomak po X osi
   5. pomak po Z osi 
   
   Origin je zadan ili pozicija treba pretuci u apsolutne koordinate i nacrtati tocku za svaki red 
   """
   for red in inBitmap :
      crtaj_tocku ( rel2abs (  inOrigin ,  [ red  [0] + pomakX, red  [1] + pomakZ, red  [2] ] , smjer ) , red  [3] , red  [4] )
      
   return


def crtaj_kvadar ( origin , poc  , kraj , smjer , blok_id , blok_dv = 0 ) :
   """
   funkcija za crtanje tocke
   1. parametar lista sa koordinatama ( X , Y , Z )
   2. parametar lista sa koordinatama ( X , Y , Z )
   3. parametar lista sa koordinatama ( X , Y , Z )
   4. smjer crtanja
   3. koji blok 
   4. koja varijanta bloka DFAULT osnovni oblik
   
   
   """
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   return

   
   
def gdjeSam ():
   """
   odredjuje trenutnu poziciju lika i vraca je u listi:
   1. X
   2. Z
   3. Y
   formatirano za rel2abs
   """
   
   #gdje sam detaljno
   radnaPozicija = mc.player.getPos()	
   return (  [radnaPozicija.x , radnaPozicija.z , radnaPozicija.y  ] )

   
def gdjeGledam () :
   """
   odredjuje trenutni smjer lika i vraca ga u listi:
   1. Vx
   2. Vz
   formatirano za rel2abs
   """
   
   smjerRada = mc.player.getDirection ()			#uzmem kamo gledam
   #smjer gledanja radi preglednosti spremimo u "vektor""
   Vx=0												#pocetne vrijednosti su nule
   Vz=0
   if abs (smjerRada.x) > abs (smjerRada.z): 		#nadje se dominanti smjer i spremi u vektor
      Vx=round(smjerRada.x)
   else:
      Vz=round(smjerRada.z)   
   return ( [Vx , Vz] )



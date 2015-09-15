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


def crtaj_vrata ( origin , polozaj , smjer , rel_smjer = 0 , blok_id = 195     ) :
   """
   funkcija za crtanje vrata
   1. parametar lista sa koordinatama ( X , Z , Y )
   2. parametar lista sa koordinatama ( X , Z , Y )
   3. smjer crtanja
   4. koji blok 
   5. gdje su okrenute 

   gore_dolje = 4 stepenice su "naopako"
   rel_smjer 0 - premameni 1 - odmene 2 - lijevo 3 - desno

   
   stepenice imaju zadano u Minecraftu
   0: Facing west
   1: Facing north
   2: Facing east
   3: Facing south
   """
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 0 , 2 , 1 , 3 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 2 , 0 , 3 , 1 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 1 , 3 , 2 , 0 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 3 , 1 , 0 , 2 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   od = rel2abs ( origin , polozaj , smjer )
   mc.setBlock (  od , blok_id , blok_dv )
   do = ( od [ 0 ] , od [ 1 ] +1  , od [ 2 ]  )
   mc.setBlock (  do , blok_id , 8 )
   

def crtaj_deblo ( origin , poc , kraj , smjer , blok_id = 53 , podtip = 0 , rel_smjer = 0   ) :
   """
   funkcija za crtanje debla
   1. parametar lista sa koordinatama ( X , Z , Y )
   2. parametar lista sa koordinatama ( X , Z , Y )
   3. parametar lista sa koordinatama ( X , Z , Y )
   4. smjer crtanja
   5. koji blok ( 17 ili 162) prva ili druga grupa 
   6. koji tip debla
   6. gdje su okrenute 
 
   rel_smjer 0 - gore/dolje 1 - lijev/desno 2 - napred/nazad
  
   debla imaju zadano u Minecraftu
    3. i 4 bit
    0:    Facing Up/Down
    1:    Facing East/West
    2:    Facing North/South
    3:    Only bark
   """   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = (  0 , 8 , 4 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = (  0 , 8 , 4 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 0 , 4 , 8 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 4 , 8 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ] + podtip
 
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   
   
def crtaj_stepenice ( origin , poc , kraj , smjer , blok_id = 53 , rel_smjer = 0  , gore_dolje = 0  ) :
   """
   funkcija za crtanje stepenica
   1. parametar lista sa koordinatama ( X , Z , Y )
   2. parametar lista sa koordinatama ( X , Z , Y )
   3. parametar lista sa koordinatama ( X , Z , Y )
   4. smjer crtanja
   5. koji blok 
   6. gdje su okrenute 
   7. naopravo ili naopako
  
   
   gore_dolje = 4 stepenice su "naopako"
   rel_smjer 0 - lijevo 1 - desno 2 - odmene 3 - prema
   
   
   stepenice imaju zadano u Minecraftu
   0: East
   1: West
   2: South
   3: North
   """
   
   tablica_smjera = {}     # definira se tablica prevoda
   tablica_smjera [ ( 1 , 0  ) ] = ( 2 , 3 , 1 , 0 ) # gledam north
   tablica_smjera [ ( -1 , 0 ) ] = ( 3 , 2 , 0 , 1 ) # gledam south
   tablica_smjera [ ( 0 , 1 ) ] = ( 1 , 0 , 3 , 2 )  # gledam east
   tablica_smjera [ ( 0 , -1 ) ]= ( 0 , 1 , 2 , 3 )  # gledam weast
   
   buff = tablica_smjera [ ( smjer [ 0 ] , smjer [ 1 ] )   ]
   blok_dv =  buff [ rel_smjer ]
   if gore_dolje != 0 :
      blok_dv +=  4  # okreni naopako ako treba
   od = rel2abs ( origin , poc , smjer )
   do = rel2abs ( origin , kraj , smjer )
   mc.setBlocks ( od , do , blok_id , blok_dv )
   return

   
def crtaj_kvadar ( origin , poc  , kraj , smjer , blok_id , blok_dv = 0 ) :
   """
   funkcija za crtanje tocke
   1. parametar lista sa koordinatama ( X , Z , Y )
   2. parametar lista sa koordinatama ( X , Z , Y )
   3. parametar lista sa koordinatama ( X , Z , Y )
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



# crta malu kucu

from mc import * #import api-ja
from crtaj_vrata import *
from crtaj_blok import *
mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom


crtaj_blok ( 1 , -1 , -2 , 5, 0 , 2 , 98 )   # kameni temelji
crtaj_blok ( 1 , 1 , -2 , 5 , 2 , 2 , 5 , 2)    # drveni zidovi
crtaj_blok ( 2 , 0 , -1 , 4 , 1 , 1 , 0 )    # prazno unutra

crtaj_blok ( 1, 1, -2 , 1 ,2 , -2 , 5  )  # stupovi na uglovima
crtaj_blok ( 1, 1, 2 , 1 ,2 , 2 , 5  )
crtaj_blok ( 5, 1, -2 , 5 ,2 , -2 , 5  )
crtaj_blok ( 5, 1, 2 , 5 ,2 , 2 , 5  )

crtaj_vrata ( 1 , 0 , 0 , 194 , 0 )
crtaj_vrata ( 1 , 0 , -1 , 194 , 0 )
crtaj_vrata ( 1 , 0 , 1 , 194 , 0 )

crtaj_vrata ( 5 , 0 , 0 , 194 , 2 )
crtaj_vrata ( 5 , 0 , -1 , 194 , 2 )
crtaj_vrata ( 5 , 0 , 1 , 194 , 2 )

crtaj_vrata ( 2 , 0 , -2 , 194 , 1 )
crtaj_vrata ( 3 , 0 , -2 , 194 , 1 )
crtaj_vrata ( 4 , 0 , -2 , 194 , 1 )

crtaj_vrata ( 2 , 0 , 2 , 194 , 3 )
crtaj_vrata ( 3 , 0 , 2 , 194 , 3 )
crtaj_vrata ( 4 , 0 , 2 , 194 , 3 )

"""
for dx in range ( 1 , 21 ):
   pomak = 9 * dx
   crtaj_blok ( 1 + pomak , -1 , -2 , 4 + pomak , 0 , 2 , 98 )   # kameni temelji
   crtaj_blok ( 1 + pomak , 1 , -2 , 4 + pomak , 2 , 2 , 5 , 2)    # drveni zidovi
   crtaj_blok ( 2 + pomak , 0 , -1 , 3 + pomak , 1 , 1 , 0 )    # prazno unutra

   crtaj_blok ( 1 + pomak , 1, -2 , 1 + pomak ,2 , -2 , 5  )  # stupovi na uglovima
   crtaj_blok ( 1+ pomak , 1, 2 , 1+ pomak  ,2 , 2 , 5  )
   crtaj_blok ( 4+ pomak , 1, -2 , 4+ pomak  ,2 , -2 , 5  )
   crtaj_blok ( 4+ pomak , 1, 2 , 4 + pomak ,2 , 2 , 5  )
   
   crtaj_vrata ( 1 + pomak , 0 , 0 , 194 )
"""
#definicija objekta i poziv rutine za crtanje
from crtanje import *		#tu je funkcija koju zovem
from mc import *			

mc = Minecraft() #inicijalizacija sustava za rad sa Minecraftom

#strelica
lik=[
[2,0,-1,STONE ,0],
[3,0,-1,STONE,0],
[4,-1,-1,STONE,0],
[4,0,-1,STONE,0],
[4,1,-1,STONE,0],
[5,0,-1,STONE,0],
]

#zid sa prozorom
zid=[
[4,-1,0,1,0],
[4,0,0,1,0],
[4,1,0,1,0],
[4,-1,1,1,0],
[4,0,1,102,0],
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],

]

#zid sa vratima 

zid_ulaz = [
[4,-1,0,1,0],	#prvo nacrtamo zid
#[4,0,0,1,0],	#moramo ostaviti rupu u zidu za vrata
[4,1,0,1,0],
[4,-1,1,1,0],
#[4,0,1,1,0],	#moramo ostaviti rupu u zidu za vrata
[4,1,1,1,0],
[4,-1,2,1,0],
[4,0,2,1,0],
[4,1,2,1,0],
[4,0,0,195,0], #i na kraju postavimo vrata
[4,0,1,195,8], #8 govori da je ovo gornji dio vrata
]

crtanje ( zid_ulaz )
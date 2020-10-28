
def xor(lista1, lista2):
	auxXOR=[]
	for x in range(len(lista1)):#Se realiza el xor bit por bit de los bytes actuales.
		auxXOR.append(str(int(lista1[x])^int(lista2[x])))
	return auxXOR
	
def LS(lst):
	aux=lst[0]
	for x in range(0,len(lst)-1):
		lst[x]=lst[x+1]
	lst[-1]=aux
	return lst

def subK():
	global key,subKey1,subKey2,keyIP, subKConfig
	key=permuter(key,keyIP)
	key=LS(key[:(len(key))//2])+key[(len(key))//2:]
	key=key[:(len(key))//2]+LS(key[(len(key))//2:])
	subKey1=permuter(key,subKConfig)
	key=LS(LS(key[:(len(key))//2]))+key[(len(key))//2:]
	key=key[:(len(key))//2]+LS(LS(key[(len(key))//2:]))
	subKey2=permuter(key,subKConfig)
	
def permuter(lista, config):
	aux=[]
	for x in range(0,len(config)):
		aux.append(lista[int(config[x])])
	return aux


def main():
	s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]] #Sbox
	s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]#Sbox
	keyIP=[2,4,1,6,3,9,0,8,7,5]#Initial Permutation Key.
	initialP=[1,5,2,0,3,7,4,6]#Initial Permutation Int.
	finalP=[3,0,2,4,6,1,7,5]#Final Permutation  Int.
	s01P=[1,3,2,0]
	subKConfig=[5,2,6,3,7,4,9,8]
	entrieXpndr=[3,0,1,2,1,2,3,0]
	subKey1=[]
	subKey2=[]
	choice=input().strip().upper()
	key=list(input().strip().upper())#almacena la llave.
	entrie=list(input().strip().upper())#almacena la cadena de entrada.
	subK()
	scheduler=[subKey1,subKey2]
	if choice == 'D':
		scheduler.reverse()
	entrie=permuter(entrie,initialP)#permutacion inicial.
	Li=entrie[:len(entrie)//2]#Li almacena el lado izquierdo.
	Ri=entrie[len(entrie)//2:]#Ri almacena el lado derecho.
	auXr=xor(scheduler[0],permuter(Ri,entrieXpndr))
	s01=list(bin(s0[int(auXr[0]+auXr[3],2)][int(auXr[1]+auXr[2],2)])[2:].zfill(2)+bin(s1[int(auXr[4]+auXr[7],2)][int(auXr[5]+auXr[6],2)])[2:].zfill(2))
	s01=permuter(s01,s01P)
	aux=Ri
	Ri=xor(s01,Li)
	Li=aux
	auXr=xor(scheduler[1],permuter(Ri,entrieXpndr))
	s01=list(
	bin(s0[int(auXr[0]+auXr[3],2)][int(auXr[1]+auXr[2],2)])[2:].zfill(2)+
	bin(s1[int(auXr[4]+auXr[7],2)][int(auXr[5]+auXr[6],2)])[2:].zfill(2))
	s01=permuter(s01,s01P)
	Li=xor(s01,Li)
	output=Li+Ri
	print(''.join(permuter(output,finalP)))

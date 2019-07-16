fat,gog=input().strip().split(" ")
gog=int(gog)
wow=0
while wow<len(fat)-1 and gog:
	if(fat[wow]>fat[wow+1]):
		gog-=1
		fat=fat[:wow]+fat[wow+1:]
		if(wow!=0):
			wow-=1
	else:
		wow+=1
pea=fat[:len(fat)-gog]
print(pea)




            

    
  
    
            

            

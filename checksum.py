import math
chain="040440003CC31004"

def checksum(chain):
  a=0
  for i in range (len(chain)):
    if(i%2 != 0):
      a+=int (chain[i],16)
  llevashexal=math.floor(a/16)
 
  ulthexal= a-(16*llevashexal)

  a=0
  for i in range (len(chain)):
    if(i%2 == 0):
      a+=int (chain[i],16)
  a+=llevashexal

  newchain1=hex(ulthexal)
  newchain=hex(a)
#newchain=newchain.replace("0x","").upper()+newchain1.replace("0x","").upper()
  newchain=(newchain+newchain1).replace("0x","").upper()
  binar=bin(int(newchain,16)).replace("0b","")
  #print(binar)

  co=len(binar)
  flag=0
  binary=""
  #print(hex(int(binar,2)).replace("0x","").upper())
  
  for i in range (len(binar)):
    co=co-1
    if(flag==1):
      flag=co+1
      break
    else:
      if(co!=0):
        if(binar[co]=="1"):
          flag=1
      
  
  
  

  for i in range(flag):
    
    if(binar[i]=="1"):
      binary=binary+"0"
    else:
      binary=binary+"1"
  #print(binary)
  
  
  for i in range(len(binar)-flag):
    binary=binary+binar[flag]
    flag=flag+1
  #print(binar)
  #print(binary)
  check=hex(int(binary,2)).replace("0x","").upper()
  check=check[-2]+check[-1]
  #print(check)
  return check
checksum(chain)
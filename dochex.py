CO="3A00053DFE01CA32040601FE02CA3204044F90FE00FA2404FE00C2120479FE01C2030476793DB8C24004DD23DD7100C31D04DD23DD7700FE01CA23040DC31D043CC31004"
ini="0400"
def dochex(CO,ini):
    import math
    from checksum import checksum
    xoxo=len(CO)
    xox=math.floor((xoxo%32)/2)
    
    
    lns=math.floor(xoxo/32)
    #print(xoxo,xox,lns)
    extra=0
    if(xox!=0):
      extra=1
    a=[]
    for i in range (lns+extra):
      a.append(":")
    k=0
    for i in range (lns):
      a[i]=a[i]+"10"+ini+"00"
      
      
      for j in range(32):
        a[i]=a[i]+CO[k]
        k=k+1
      
      ini=hex(int(ini,16)+16)
      if(len(ini)==5):
        ini=ini.replace("0x","0").upper()
      if(len(ini)==4):
        ini=ini.replace("0x","00").upper()
      if(len(ini)==3):
        ini=ini.replace("0x","000").upper()
      if(len(ini)==2):
        ini=ini.replace("0x","0000").upper()
      if(len(ini)==6):
        ini=ini.replace("0x","").upper()
    
    if(extra==1):
      ini=hex(int(ini,16))#+xox-16#)
      if(len(ini)==5):
        ini=ini.replace("0x","0").upper()
      if(len(ini)==4):
        ini=ini.replace("0x","00").upper()
      if(len(ini)==3):
        ini=ini.replace("0x","000").upper()
      if(len(ini)==2):
        ini=ini.replace("0x","0000").upper()
      if(len(ini)==6):
        ini=ini.replace("0x","").upper()
      
      xxx=hex(xox).replace("x","")
    
      a[lns]=a[lns]+xxx+ini+"00"
      for j in range(2*xox):
        a[lns]=a[lns]+CO[k]
        k=k+1
      
      
    a.append(":00000001FF")
    #print(a)
    
    print("\n")
    for i in range(len(a)-1):
        aux=""
        for j in range(len(a[i])-1):
            aux=aux+a[i][j+1]
        a[i]=a[i]+checksum(aux)
    print(a)
    f=open("HEX.hex","w")
    for i in (range(len(a))):
        f.write(a[i])
        f.write("\n")
    f=f.close
dochex(CO,ini)
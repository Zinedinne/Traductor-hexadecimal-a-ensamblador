def manejoEtis(p,a,tS,CL):
    if p==1:
        #Para la pasada 1
            print("Entra pasada 1")
            eti=a.find("eti")
            dDot=a.find(":")
            tS.update({a[eti:dDot]:CL})
            a=a.replace(a[eti:dDot+1],"")
            return a,eti,dDot,tS


    if p==2:
        #Para la pasada 2
        print("Entra pasada 2")
        eti=a.find("eti")
        dDot=a.find(":")
        a=a.replace(a[eti:dDot+1],"")
        return a


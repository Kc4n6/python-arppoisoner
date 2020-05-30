import os
import time
import random
import subprocess
def getnewmac():
        krktrs = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
        newmac = ""
        for i in range(1,6):
                if(len(newmac)==0):
                        krktr1 = random.choice(krktrs)
                        krktr2 = random.choice(["2","4","6","8","0","a","c","e"])
                        newmac = newmac + "".join([krktr1,krktr2]) + ":"
                if(len(newmac) == 15):
                    newmac = newmac + "".join(random.sample(krktrs,2))
                else:
                    newmac = newmac + "".join(random.sample(krktrs,2)) + ":"
        print(newmac)
        return newmac


def changemac(ag_karti,newmac):
        os.system("sudo ifconfig "+ag_karti+" down")
        time.sleep(1)
        komut = ['sudo','ifconfig',ag_karti,'hw','ether',newmac]
        cikti = subprocess.Popen(komut, stdout=subprocess.PIPE).communicate()[0]
        print(cikti)
        time.sleep(1)
        print(cikti.decode() + "bunlar cikti kardes")
        os.system("sudo ifconfig "+ag_karti+" up")

newmac = getnewmac()
changemac("Network kartınızın adını giriniz...",newmac)

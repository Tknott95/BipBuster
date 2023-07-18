# A sloppy python permutative-based "precision" wallet brute forcer (have to run local-node and cardano wallet)
# if you recover too many at once syncs can take a crazy amount of time, which you need a certain % synced to check balance even if keys worked and a wallet was found, so this might be a bad way to approach this
# on big scrapes you will recover many empties with successful keys

import itertools
import requests
import json

from twilio.rest import Client

ALL_BIPS = [line.rstrip('\n') for line in open('bips.txt')]

a1 = ["judge","innocent","reform"]
a2 = ["reflect","moment"] 
a3 = ["riot"]
a4 = ["owner"] # "own"
a5 = ["dune"] 
a6 = ["kind"]
a7 = ["vacant", "theme"]
a8 = ["address"]
a9 = ["boil"]
a10 = ["album"]
a11 = ["crouch"]
a12 = ["over"]
a13 = ["pet"] # curve
a14 = ["able"]
a15 = ["decrease"]
a16 = ALL_BIPS # ["segment", "cement", "payment"]
a17 = ["flag","banner"]
a18 = ["fresh"]
a19 = ["skill"] # "leader", ,"theme" ,"document"
a20 = ["spice"]
a21 = ["brick"]
a22 = ["payment"]
a23 = ["skate"]
a24 = ["paper"]

ijk = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24]

permutationList = list(itertools.product(*ijk))



account = "<acc-id>"
token = "<token-id>"
client = Client(account, token)

url = 'http://localhost:1338/v2/wallets'


i=0
for x in permutationList:
        myobj = {
        "name": "X4Wallet137",
        "mnemonic_sentence": x,
        "passphrase": "X4Wallet137!",
        }

        objSTR = str(myobj)
        x = requests.post(url, json = myobj)
        if(x.status_code != 400):
            if(x.text[2] == "a"):
                txtToSend = " #" +str(i) + objSTR
                i = i+1
                print(myobj)
                message = client.messages.create(to="<WHO-AM-I-SENDING-TO?>", from_="+19064482247", body=txtToSend)
        # print(x.text)

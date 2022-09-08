import random
import time

# do not commit die
# (c) 21/02/22
# IAGO F. ALAGADO

letters = range(33,127)

desired = "bruhtava"

baselist = ["*","*","*","*","*","*","*","*"]
while ''.join(baselist) != desired:

    ramble_text = ''.join([chr(random.choice(letters)) if i == "*" else i for i in baselist])

    for i in range(len(ramble_text)):

        if desired[i] == ramble_text[i]:
            
            baselist[i] = desired[i]
    
    print(ramble_text,end="\r")
    time.sleep(0.025)
print("\n")

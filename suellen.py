import time
import os

# do not commit die
# (c) 21/02/22
# IAGO F. ALAGADO

lines = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
word  = "suellen"
index = [1,2,3,2,1,0,0]
cur_max = 1
# print("\033[H\033[J", end="")
os.system("cls")
while index != [0,0,0,0,0,0,0]:

    if cur_max != -1:
        index[cur_max] = 3

    for i in range(len(index)):

        index[i] -= 1 if index[i] > 0 else 0
    
    for i in range(len(index)):

        lines[index[i]][i] = word[i]
    
    lines.reverse()

    for line in lines:

        print(''.join(line))

    lines = [[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
    if cur_max < len(word):
        cur_max += 1
    if cur_max >= len(word):
        cur_max = -1
    time.sleep(0.025)
    #print("\033[H\033[J", end="")
    os.system("cls")

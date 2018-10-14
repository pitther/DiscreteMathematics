import string
import os
import sys


association_char = "*"
crossing_char = "^"
difference_char = "\\"
symmetric_difference_char = "%"
addition_char = "_"


U = [] #universum
print ("Input universum (1 2 3 | a b c):")
res = input()
AUTO_UNIVERSUM = False
if (res != ""):
    u_raw = res.split(" ")
    for e in u_raw:
        if (e != ""):
            U.append(e)
else:
    AUTO_UNIVERSUM = True


BUFFS = []

PLURALS_ALPHABET = list(string.ascii_uppercase)
ALPHABET_ITERAL = -1

PLURALS_DICT = {}
PLURALS_DICT_V = {}

inp_s = " "
while (inp_s != ""):
    ALPHABET_ITERAL += 1
    print()
    print("Enter set "+PLURALS_ALPHABET[ALPHABET_ITERAL]+", or stop (ENTER): ")
    
    inp_s = input()

    if (inp_s != ""):
        BUFF = [] #BUFF plural 
        
        buff_raw = inp_s.split(" ")
        for e in buff_raw:
            if (e != ""):
                BUFF.append(e)

        BUFF.sort()
        BUFF = list(set(BUFF))
        BUFFS.append(BUFF)
        BUFFS.sort()
        BUFF.sort()

        PLURALS_DICT[PLURALS_ALPHABET[ALPHABET_ITERAL]] = BUFF
    else:
        break
    
PLURALS = BUFFS
ACTUAL_ALPHABET = []
for i in range( len(PLURALS) ):
    ACTUAL_ALPHABET.append(PLURALS_ALPHABET[i])


# calculating universum
if (AUTO_UNIVERSUM):
    for L in PLURALS:
        U.extend(L)
        U = list(set(U))
    U.sort()
else:
    U_VER_BUFF = []
    for L in PLURALS:
        U_VER_BUFF.extend(L)
        U_VER_BUFF = list(set(U_VER_BUFF))

    U.sort()
    U_VER_BUFF.sort()
    
    if (len(U) < len(U_VER_BUFF) ):
        print ("Universum that you have entered does not cover all elements: ")
        print ("    Your universum: ", U)
        print ("    Actual universum: ", U_VER_BUFF)
        sys.exit('')


for K in PLURALS_DICT.keys():
    V_ITER = 0
    BUFF = []
    P = PLURALS_DICT.get(K)
    for E in U:
        if (E in P):
            BUFF.append(1)
        else:
            BUFF.append(0)
            
    PLURALS_DICT_V[K] = BUFF
    V_ITER += 1        

def display_plurals():
    print ("- - - - - - - - -")
    print ("Current sets (sorted): ")
    BUFF_ITERATOR = 0
    for K in PLURALS_DICT.keys():
        L = PLURALS_DICT.get(K)
        print ("   "+ K + " = {"+', '.join(str(e) for e in L)+"}")
        BUFF_ITERATOR += 1
    print ("- - - - - - - - -")
    print ("Universum: ")
    print ('   U = {'+ ', '.join(str(e) for e in U)+'}')
    print ("- - - - - - - - -")
    print ("Boolean sets: ")
    BUFF_ITERATOR = 0
    for K in PLURALS_DICT_V.keys():
        L = PLURALS_DICT_V.get(K)
        print ("   "+ K + "<->{"+', '.join(str(e) for e in L)+"}")
        BUFF_ITERATOR += 1
    print ("- - - - - - - - -")


last_exp_inp = []
last_exp_res = []



def display_last_expressions():
    if ( len(last_exp_inp) > 0 ):
        print ("- - - - - - - - -")
        print ("Expression history: ")

    BUFF_ITER = 0
    for e in last_exp_inp:
        spacing = '   '
        if (len(e) > 4):
            spacing = ' '


        print (spacing+e + " = {"+', '.join(str(e) for e in v_t_p(last_exp_res[BUFF_ITER]) )+"}")
        print ("         {"+', '.join(str(e) for e in last_exp_res[BUFF_ITER])+"}")
        
        BUFF_ITER += 1



###########################
# obyednannya (association) - ^^ 
# peretyn (crossing) - ^
# riznyca (difference) - \
# symetrichna riznyca (symmetric difference) - %
# dodavannya (addition)- _
# @pe os
##########################

def v_t_p(v):
    BUFF_ITER = 0
    PLUREAL_BUFF = []
    for e in v:
        if (e == 1):
            PLUREAL_BUFF.append(U[BUFF_ITER])
        BUFF_ITER += 1
    return PLUREAL_BUFF

#c = a * b
#0 1 2 3 4
#c = a _
#a _
#a * b

def exp_handler(inp):
    if (True):
        APPROP = False
        EXP_CHAR = ''
        EXP_P1_K = ''
        EXP_P2_K = ''
        if ( '=' in inp ):
            APPROP = True
            APPROP_PLURAL_K = inp[0]
            EXP_CHAR = inp[3]
            if (EXP_CHAR != addition_char):
                EXP_P1_K = inp[2]
                EXP_P2_K = inp[4]
            else:
                inp += ' '
                EXP_P1_K = inp[2]
            #inp = inp[2:]
        else:
            EXP_CHAR = inp[1]
            if (EXP_CHAR != addition_char):
                EXP_P1_K = inp[0]
                EXP_P2_K = inp[2]
            else:
                inp += ' '
                EXP_P1_K = inp[0]

        if (EXP_P1_K not in PLURALS_DICT.keys() or (EXP_P2_K != '' and EXP_P2_K not in PLURALS_DICT.keys()) ):
            return 0

        last_exp_inp.append(inp)
        RES_BUFF_V = []
        ITER_BUFF = 0
        if (EXP_CHAR == association_char):
            for e1 in PLURALS_DICT_V.get(EXP_P1_K):
                e2 = PLURALS_DICT_V.get(EXP_P2_K)[ITER_BUFF]
                if e1 == 1 or e2 == 1:
                    RES_BUFF_V.append(1)
                else:
                    RES_BUFF_V.append(0)
                ITER_BUFF += 1
        elif (EXP_CHAR == crossing_char):
            for e1 in PLURALS_DICT_V.get(EXP_P1_K):
                e2 = PLURALS_DICT_V.get(EXP_P2_K)[ITER_BUFF]
                if e1 == 1 and e2 == 1:
                    RES_BUFF_V.append(1)
                else:
                    RES_BUFF_V.append(0)
                ITER_BUFF += 1
        elif (EXP_CHAR == difference_char):
            for e1 in PLURALS_DICT_V.get(EXP_P1_K):
                e2 = PLURALS_DICT_V.get(EXP_P2_K)[ITER_BUFF]
                if e1 == 1 and e2 != 1:
                    RES_BUFF_V.append(1)
                else:
                    RES_BUFF_V.append(0)
                ITER_BUFF += 1
        elif (EXP_CHAR == symmetric_difference_char):
            for e1 in PLURALS_DICT_V.get(EXP_P1_K):
                e2 = PLURALS_DICT_V.get(EXP_P2_K)[ITER_BUFF]
                if (e1 == 1 and e2 != 1) or (e1 != 1 and e2 == 1):
                    RES_BUFF_V.append(1)
                else:
                    RES_BUFF_V.append(0)
                ITER_BUFF += 1
        elif (EXP_CHAR == addition_char):
            for e in PLURALS_DICT_V.get(EXP_P1_K):
                if e == 1:
                    RES_BUFF_V.append(0)
                else:
                    RES_BUFF_V.append(1)

        last_exp_res.append(RES_BUFF_V)
        if (APPROP):
            PLURALS_DICT_V[APPROP_PLURAL_K] = RES_BUFF_V
            PLURALS_DICT[APPROP_PLURAL_K] = v_t_p(RES_BUFF_V)

    else:
        print ("Incorrect input: Use only existing sets")
    


inp_s = " "
while (inp_s != ""):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    display_last_expressions()
    display_plurals()
    print("Available expressions: ")
    print("    Union  "+association_char+"                   ex. C=A"+association_char+"B ")
    print("    Intersection  "+crossing_char+"            ex. C=A"+crossing_char+"B ")
    print("    Difference  "+difference_char+"              ex. C=A"+difference_char+"B ")
    print("    Symmetric difference  "+symmetric_difference_char+"    ex. C=A"+symmetric_difference_char+"B ")
    print("    Complement  "+addition_char+"              ex. C=A"+addition_char+" ")
    print ("- - - - - - - - -") 
    print("Type expression or exit (ENTER): ")
    inp_s = input()

    if (inp_s != ""):
        inp_s = inp_s.upper()
        exp_handler(inp_s)

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print ("Final results: ")
display_plurals()

    










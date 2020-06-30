#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import platform
import Evaluate

drugbox=[]
drugpath=[]
run=2
vinapath='./autodock_vina/bin/vina'
if platform.system()=='Linux':
    pass
elif platform.system()=='Darwin':
    vinapath='./autodock_vina_mac/bin/vina'

def main():
    global vinapath
    global run
    global drugpath
    global drugbox
    print("Start autodock vina docking")
    if not os.path.exists('./out'):
        os.mkdir('./out')
    print('Reading all the existing inhibitors...')
    f=os.listdir('./ligands')
    for i in f:
        if '.pdbqt' in i:
            print(">>>",i[:-6])
            drugbox.append(i[:-6])
            drugpath.append('./ligands/'+i)
    #print(drugbox)
    tmp=3
    print("Now processing all these inhibitors to autodock vina analysis")
#    tmp=input("please enter the number of runs on each sample: (default is 3)\n>>> ")
    try:
        tmp=int(tmp)
        run=tmp
    except ValueError:
        run=3

    for drug in drugbox:
        print("Now start to process",drug)
        vinarun(drug)
    Evaluate.Evaluating()


def vinarun(inhibitor):
    def appendInt2(num):
        value = str(num)
        if len(value) > 1:
            secondToLastDigit = value[-2]
            if secondToLastDigit == '1':
                return 'th'
        lastDigit = value[-1]
        if (lastDigit == '1'):
            return 'st'
        elif (lastDigit == '2'):
            return 'nd'
        elif (lastDigit == '3'):
            return 'rd'
        else:
            return 'th'
    if not os.path.exists('./out/'+inhibitor):
            os.mkdir('./out/'+inhibitor)
    for i in range(1,run+1):
        num=str(i)+appendInt2(i)
        eq="="*50
        print(eq)
        print("Processing the",num,"run on inhibitor",inhibitor)
        vina(inhibitor,i)



def vina(inhibitor,runtime):
    tmp0 ='./out/' + inhibitor + '/'+ str(runtime)
    tmp = 'mkdir ./out/' + inhibitor + '/'+ str(runtime)+ '>>vina.log'
    if not os.path.exists(tmp0):
        os.system(tmp)
    tmp = 'touch ./out/' + inhibitor + '/'+ str(runtime) + "/out.log"+ '>>vina.log'
    tmp0 ='./out/' + inhibitor + '/'+ str(runtime)+ '/out.log'
    if not os.path.exists(tmp0):
        os.system(tmp)
    tmp = vinapath+" --config conf.txt --ligand ligands/" + inhibitor +\
          ".pdbqt " + "--out out/" + inhibitor + '/'+ str(runtime) + "/out.pdbqt --log ./out/" + inhibitor + '/'+ str(runtime) + "/out.log >> vina.log"
    #print(tmp)
    tmp0 ='./out/' + inhibitor + '/'+ str(runtime)+ '/out.pdbqt'
    if not os.path.exists(tmp0):
        os.system(tmp)
    else:
        time.sleep(2)
    #os.system(tmp)
    tmp="cat ./out/" + inhibitor + '/'+ str(runtime) + "/out.log|tail -n13"
    os.system(tmp)


if __name__ == '__main__':
    main()
    print("Done!")

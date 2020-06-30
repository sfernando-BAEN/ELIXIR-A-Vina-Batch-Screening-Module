#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import sys
import numpy
import csv

#for i in range(30):
#     sys.stdout.write('.')
#     sys.stdout.flush()
#     time.sleep(0.001)
#print('\n')

def Evaluating():
    with open('VinaScore.csv','w', newline='') as csvfile:
        csvout = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvout.writerow(["Number","BindingScore","Std","Library"])
        chems=os.listdir('./out')
        if '.DS_Store' in chems:
            chems.remove('.DS_Store')
        logfile=open('VinaResult.log','w')
        energy={}
        for chemname in chems:
            if chemname not in energy:
                energy[chemname]=[]
            runs=os.listdir('./out/'+chemname)
            top3=''
            for i in runs:
                if '.' in i:
                    continue
                chemdir='./out/'+chemname+'/'+i+'/out.log'
                f=open(chemdir,'r')
        #            tmp=f.readlines()[26:29]
                tmp=f.readlines()[26:27]
                title='The docking energy of '+chemname+':(highest energy of each of run)'
                title+='\n'
                for ind,line in enumerate(tmp):
                    #calculate the average energy
                    energy[chemname].append(float(line.split()[1]))
                    #create the log file
                    top3+=str(line.split()[1])+' kcal/mol '
                    top3+='\n'
            print(title)
            print(top3)
        #        time.sleep(0.5)
            logfile.write(title)
            logfile.write(top3)
            f.close()
#        chems.sort(key=lambda x:sum(energy[x]))
        chems.sort(key=lambda x:x)
        for i in range(20):
            sys.stdout.write('....')
            sys.stdout.flush()
            time.sleep(0.005)
        title='The average docking energies of these '+str(len(chems))+' chemicals are sorted:'
        print(title)
        title+='\n'
        logfile.write(title)
        for che in chems:
            tmp=che.ljust(12)+' '+str(round(sum(energy[che])/max(1,(1.0*len(energy[che]))),3)).ljust(6)+' kcal/mol'
            print(tmp)
            tmp+='\n'
            logfile.write(tmp)
            tmp='Standard deviation: '+str(round(numpy.std(energy[che]),3)).ljust(6)+'\n'
            print(tmp)
            logfile.write(tmp)
            csvout.writerow([che[-4:],str(round(sum(energy[che])/max(1,(1.0*len(energy[che]))),3)),str(round(numpy.std(energy[che]),3)),chemname[:-5]])
        logfile.close()
def Evaluatingcsv():
    with open('VinaScore.csv','w', newline='') as csvfile:
        csvout = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvout.writerow(["Number","BindingScore","Std","Library"])
        for chemname in chems:
            csvout.writerow([chemname[-4:],str(round(sum(energy[che])/(1.0*len(energy[che])),3)),str(round(numpy.std(energy[che]),3)),chemname[:-5]])
    
if __name__ == '__main__':
    print('\nEvaluating Docking energy for all the docking test files\n')
    Evaluating()

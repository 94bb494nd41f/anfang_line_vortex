# -*- coding: utf-8 -*-

import os
import math
import pandas as pd
import numpy as np
from numpy import genfromtxt
#os.system('postProcess -func sampleDict_plane_U')
def Einlesen():
    cwd=os.getcwd()
    print('\n das ist die cwd:\n ', cwd)
    #folder=
    print('\nlist:\n',os.listdir(cwd))
    os.chdir(cwd+'/sampleDict_plane_U')
    list_timesteps=os.listdir(os.getcwd())
    print('Timesteps',list_timesteps)
    listemitdingen=[]   #tupel fuer liste
    maxima_lambda2=0
    i=0
    x='str'
    finaleliste=[]
    #finaleliste_input = (x_dir, -x / 1.2192, 'p/lambda2', x, y, z)
    #finaleliste(timestep,span, p/lambdavalue, koordinaten)
    #erstezeile=('(x_dir, -x / 1.2192, p/lambda2, x, y, z')
    #finaleliste.append(erstezeile)
    samplewd=os.getcwd()
    letztertimestep_liste=[int(i) for i in list_timesteps]
    Letztertimestep=[]
    Letztertimestep.append(max(letztertimestep_liste))
    for x_dir in Letztertimestep:
        os.chdir(samplewd+'/'+str(x_dir))
        l_data=os.listdir(os.getcwd())
        print('list_timestep',list_timesteps[0])
        print('list_timestep mit x_dir',x_dir)
        #x=l_data
        for y_dir in l_data[:]:
             p_tupel = (0, 0, 0, 0)
             L_tupel = (0, 0, 0, 0)
             #hat google vorgeschlagen, lief mit panda nicht so gut weil keine CSV
             mydata = np.genfromtxt(str(y_dir),skip_header=2,  dtype=float)
             #mydata = mydata.astype(float) #scheinbar nicht notwenigd
             #print('y', y_dir, mydata.shape, 'type', type(mydata))
             #print(mydata.item((0,0)), type(mydata.item((0,0))))
             #print(y_dir[0])
             #print(type(y_dir[0]), y_dir[0])
             erster_buchstab=str(y_dir[0])
             # #fuer p
             # if 'p'==erster_buchstab:
             #     print('suche nach p_min')
             #     p_min = mydata.item((0, 3))
             #     x = mydata.item((0, 0))
             #     y = mydata.item((0, 1))
             #     z = mydata.item((0, 2))
             #     p = p_min
             #     for i in mydata[:]:
             #         #print('i',i)
             #         p=i.item(3)
             #         #print('p',p)
             #         if p>p_min:
             #             p_min=p
             #             x=mydata.item(0)
             #             y=mydata.item(1)
             #             z=mydata.item(2)
             #             p_tupel = (x, y, z, p_min)
             #     print('p_min',p_tupel)
             #     finaleliste_input = (x_dir, x / 1.2192, p, x, y, z, 'p')
             #     finaleliste.append(finaleliste_input)
             # #Fuer lambda kontrollieren
             if 'L'==erster_buchstab:
                 #print('Suche nach lambda')
                 L_max = mydata.item((0, 3))
                 x = mydata.item((0, 0))
                 y = mydata.item((0, 1))
                 z = mydata.item((0, 2))

                 #backup


                 for i in mydata[:]:
                     #print('i',i,type(i))
                     L=i.item(3)
                     #print('l',L)
                     if L>L_max:
                         L_max=L
                         x=i.item(0)
                         y=i.item(1)
                         z=i.item(2)
                         #L_tupel=(x,y,z,L_max)
                 #print('L_max:',L_tupel,'timestep:',x_dir)
                 finaleliste_input = (x_dir, x / 1.2192, L_max, x, y, z, 'L\n')
                 print('x_dir:', x_dir,'C', x / 1.2192,'Lambda:', L_max,'(', x,'|', y,'|', z,')', '\n')
                 finaleliste.append(finaleliste_input)
    for i in range(0, len(finaleliste)-2):
        w_1=finaleliste[i]
        w_2=finaleliste[i+1]
        #berechnung der distanz zwischen p und l maxima
        x_1 = w_1[3]
        y_1 = w_1[4]
        z_1 = w_1[5]
        x_2 = w_2[3]
        y_2 = w_2[4]
        z_2 = w_2[5]
        distanz=((x_1-x_2)**2+(y_1-y_2)**2+(z_1-z_2)**2)**0.5
        #print('distanz zwischen', w_1, 'und', w_2, ':', distanz)

    return(listemitdingen,finaleliste)

def linienlegen(finaleliste):
    punkte = []
    for i in range(len(finaleliste)-18,len(finaleliste)):
        #print('finaleliste:', finaleliste[i])
        letztereintrag=finaleliste[i]
        a=0.5
        #letztereintrag=finaleliste[len(finaleliste)-18]
        c_stern=letztereintrag[1]
        #print('cstern',c_stern)
        x=letztereintrag[3]
        y=letztereintrag[4]
        z=letztereintrag[5]
        #punkte_tupel=
        punkte.append((x, y + a, z, x, y - a, z, str(c_stern) + '_1')) #senkrechter schnitt fuer chow
        a=a*0.5
        punkte.append((x, y + a, z, x, y - a, z, str(c_stern)+ '_2'))
        punkte.append((x, y + a, z, x, y - a, z, str(c_stern)+'_3'))
        punkte.append((x, y + a, z, x, y - a, z, str(c_stern)+'_4'))
        #achtung, die schiefen punkte passen nicht mehr!
        #print('len',len(punkte))
        #print('punkte:',punkte)
    #print('punkte2:',punkte,'len',len(punkte))
    return(punkte)

def sampledict(punkte,):
    cwd=os.getcwd()
    #os.path.abspath(os.path.join(__file__ ,"../.."))
    os.chdir('..')
    os.chdir('..')
    os.chdir('..')
    os.chdir(os.getcwd()+'/system/')
    #print(os.getcwd())
    f=open('sampleDict_python_plotlines','w')
    #schreiben des Openfoamheaders
    f.write('FoamFile\n'
            '{\n'
            'version\t2.0;\n'
            'format\tascii;\n'
            'class\tdictionary;\n'
            'object\tsampleDict;\n'
            '}\n\n\n')
    #schreiben settings für sampleDict
    f.write( 'type sets;\n libs    ("libsampling.so");\n setFormat  raw;\n interpolationScheme cellPoint;\n  writeControl writeTime;\n startTime latestTime;\ntimeInterval 1;\nfields (U);\n sets \n( \n')
    #schreiben der auszulesenden lines
    for i in punkte[:]:
        #print('i,punkte',i)
        #Welche liniennummer
        line=i[6]
        line_nummer=line[len(line)-1]
        c=round(float(i[6]), 1)
        #kontrollausgabe
        #print('i:', i[6])
        x_1=i[0]
        y_1=i[1]
        z_1=i[2]
        x_2=i[3]
        y_2=i[4]
        z_2=i[5]
        #kontrollausgaben
        #print('c*'+str(c)+'_'+str(line_nummer)+'\n')
        #print('c*' + i[6] + '_' + str(line_nummer) + '\n')
        f.write('c*'+str(c)+'_'+str(line_nummer)+'\n'
            ' {\n'
            ' type uniform;\n'
            ' axis xyz;\n'
            ' start ( '+str(x_1)+' '+str(y_1)+' '+str(z_1)+');\n'
            ' end (' +str(x_2)+' '+str(y_2)+' '+str(z_2)+');\n'
            ' nPoints \t 400;\n'
            '}\n\n')

    f.write(');')
    f.close()





if __name__ == '__main__':
    print('Bitte README lesen')
    listemitdingen,finaleliste=Einlesen()
    #print('listemitdingen:',listemitdingen)
    punkte=linienlegen(finaleliste)
    sampledict(punkte)
    #print('finaleliste:',finaleliste)
    cwd=os.getcwd()
    #print(cwd)
    #os.chdir()



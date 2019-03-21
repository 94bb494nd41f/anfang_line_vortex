import os
import math
import pandas as pd
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import shutil

def Einlesen():
    cwd=os.getcwd()
    print('\n das ist die cwd:\n ', cwd)


    os.chdir(cwd+'/sampleDict_python_plotlines')
    list_timesteps=os.listdir(os.getcwd())
    print('Timesteps', list_timesteps)
    #konvertieren der string-liste in float um spaeter den maximalen timestep zu finden.
    list_timesteps_float=[float(i) for i in list_timesteps]

    samplewd=os.getcwd()
    for x_dir in list_timesteps[:]:
        print('xdir', x_dir)
        os.chdir(samplewd+'/'+str(x_dir))

        # removing previous plots
        if 'plots' in os.listdir(os.getcwd()):
            shutil.rmtree(os.getcwd() + '/plots')
        os.mkdir(os.getcwd() + '/plots', 0o777)

        l_data=os.listdir(os.getcwd())
        print('current timestep', x_dir)
        #x=l_data
        c_list = []
        line_list = []
        #muss so eingelesen werden, sonst zuordnung lines zu plane schwierig. gibt bestimmt einfacheren weg
        for y_dir in l_data[:]:
            #sonst werden auch ordner etc versucht zu laden
            if 'c'==y_dir[0]:
               if y_dir[2:5] not in c_list:
                   c_list.append(y_dir[2:5])
               line_list.append(y_dir[6])


                #print('linelist:', line_list, 'max', max(line_list))

        for c in c_list[:]:
            print('c', c)
            #x,y,z,u_x,u_y,u_z
            c_mean =[]
            #loading into mydata
            for i in range(1, int(max(line_list))+1):
                filename='c*'+str(c)+'_'+str(i) + '_' + 'U.xy'
                #print('timestep', x_dir, 'currentfile', str(c)+'_'+str(i) + '_' + 'U')
                if i==1:
                    mydata_1 = np.genfromtxt(str(filename), skip_header=0, dtype=float)
                    #print(mydata_1.item((0, 0)),mydata_1.item((0, 1)), mydata_1.item((0, 2)))
                if i==2:
                    mydata_2 = np.genfromtxt(str(filename), skip_header=0, dtype=float)
                    #print(mydata_2.item((0, 0)), mydata_2.item((0, 1)), mydata_2.item((0, 2)))
                if i==3:
                    mydata_3 = np.genfromtxt(str(filename), skip_header=0, dtype=float)
                    #print(mydata_3.item((0, 0)), mydata_3.item((0, 1)), mydata_3.item((0, 2)))
                if i==4:
                    mydata_4 = np.genfromtxt(str(filename), skip_header=0, dtype=float)
                    #print(mydata_4.item((0, 0)), mydata_4.item((0, 1)), mydata_4.item((0, 2)))


                #annahme isotroper wirbeleigenschaften, koordinaten egal.

            #'kleinste liste' bestimmen, falls line in wing ragt und nicht sampeln kann

            #averging over mydata
            len_min=min(len(mydata_1), len(mydata_2), len(mydata_3), len(mydata_4))
            for i in range(0,len_min):
                #da x=const,
                #wird ueber kleinste strecke berechnet
                #c_mean: x|y|z|u_x|u_y|u_z  u gemittelt, x,y,z kommen aus mydata_1
                c_mean.append((
                    1.0*mydata_1.item((i,0)), mydata_1.item((i,1)), mydata_1.item((i,2)),
                    1.0*(mydata_1.item((i,3))+0*mydata_2.item((i,3))+0*mydata_3.item((i,3))+0*mydata_4.item((i,3))),
                    1.0*(mydata_1.item((i,4))+0*mydata_2.item((i,4))+0*mydata_3.item((i,4))+0*mydata_4.item((i,4))),
                    1.0*(mydata_1.item((i,5))+0*mydata_2.item((i,5))+0*mydata_3.item((i,5))+0*mydata_4.item((i,5)))
                )) #achtung!alle ausser mydata_1 sind rausgenullt
            #ploting
            print('plot of c*', c, 'cwd', os.getcwd())
            f = plt.figure()
            x_val = [x[1] for x in c_mean]
            y_val = [x[5] for x in c_mean]
            plt.xlabel('y')
            plt.ylabel('u_z')
            plt.plot(x_val, y_val)
            plt.plot(x_val, y_val, 'or')
            #plt.show()

            f.savefig('plots/c_mean*'+str(c)+'.pdf', bbox_inches='tight')
            plt.close()



    return()





if __name__ == '__main__':
    print('Bitte README lesen')


    n=Einlesen()
    #print('listemitdingen:',listemitdingen)
    #punkte=linienlegen(finaleliste)
    #sampledict(punkte)
    #print('finaleliste:',finaleliste)
    #cwd=os.getcwd()
    #print(cwd)
    #os.chdir()



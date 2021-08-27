import os 
import unicodedata
def initialize(slot,a=0):

    print("clonckuido")
    for i in range(0,a):
        slot.append('')
    
    return slot

def entry(lote,str,cor,dict):
    flag=0
    for k in dict.keys():
        flag=0
        if dict[k][0] =='':
            print('carro addicionado ')
            unicodedata.normalize('NFKD',str).encode('ascii', 'ignore')
            unicodedata.normalize('NFKD',color).encode('ascii', 'ignore')
            o=[str,color,dict]
            dict[K] =0
            flag=1
            break
    if flag == 0:
        return ' inteiro'
    return  dict 

def saida_ do_carro(str,str,dict):

    for k in dict.keys():
        lis = dict[k]
        if list [0] == str:
            dict[k][0]=""
            dict[k][1] =""            
        
        print('lote liberado ')

    
def get_carros_com_cor(col,dict1):
    ans=dict()

    for k in dict1.keys():

        if dict1[k][1]==col:
            ans[k]=dict1[k]

    return  ans

def get_placa_carro(str,dict):
    ans2=dict()
    for k in dict1.keys():

        if dict1[k][0]==str:
            ans2[k]=dict1[k]
    return ans2

def mostre_os_carros():
    print(dict)


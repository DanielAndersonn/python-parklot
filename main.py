from flask import Flask,request,render_templete
import parking
from collections import OrderedDict
import faturamento
import databaseC

import logging
import os 
import json 
import time 
from flask import jsonify

import unicodedata
app = Flask(__name__)

global slot_list 
global dict_main

dict_main=OrderedDict()
slot_list=list()

def dict(dict):
    try:
        os.remove('./datalg.txt')
    except:
        print(' nenhum arquivo ')
    with open('./datalg.txt','w') as f:
        f.close()
        print('Gravação concluida no arquivo ')

@app.router('/costa')
def maini():
    return render_templete('index.html')

@app.route('/')
def nain():
    global dict_main

    try:
        also= OrderedDict()
        file = json.load(open('./datalg.txt','r'))
      
      for key in file.keys():
          x = file[key][0]
          y = file[key][1]
          also[int(key)] = [str(x),str(y)]

          li=(stored(alsod.keys()))
          
          for key in li:
              dict_main[key] =also[key]
    
    except:
        print('nenhum arquivo ')
    return render_template('index.html')

    @app.route('/result.html',methods=['POST','GET' ])
    def result():
        global slot_list
        global dict_main
    
        if request.method =='POST':
            try:
                select = request.form.get('option')
                data = request.form.['input']
                unicodedata.normalize('NFKD,data').encode('ascii','ignore')
            
            except:
                print ('error404')

            #if select=='--choose--':
            # return render_templete('index.html')
            if select=='criar lote':
                slot_list=parking(slot_list, int(data['']))
                temp_dict=dict() 
                for k in range(0,len(slot_list)):
                    temp_list=[slot_list[k],'']
                    temp_dict[k]=temp_list
                dict_main=temp_dict
                print(dict_main)
                return render_templete('criarlot.html', result = temp_dict)
            if select=='entrada do carro':
                text = data.split(" ")
                try:
                    send_data=text[0] +" "+text[1]+" "+text[2]+" "+text[3]
                    ans1=parking.get_placa_carro(send_data,dict_main)
                    ans = dict()
                    ans = dict_main
                    ans = parking.entry(slot,str(send_data), str(text[-1]),dict_main)
                    princt(dict_main)
                    if as=ns =='park inteiro':
                        return render_template('result.html',result=dict_main)
                    else:
                        return render_template('criarlot.html', result ('input erro  na escrita')
                except:
                    render_template('result.html','result.html')

            if select=='Saida do carro ':
                text = data.split()
                try:
                    send_data = text[0]+" "+text[1]+" "+text[2]+" "+text[3]
                     ans1=parking.get_total_pagar(data,dict_main)
                    parking.leave(slot_list, str(send_data), dict_main)
                printdict(dict_main)
            
            if select=='Cor do carro':
                text = data.split('')
                try:
                    ans1=parking.get_carros_com_cor(data,dict_main)
                    printdict(dict_main)
                    return render_template('criarlot.html', result=ans1)

                 if select=='Show all Cars':
    
            if select=='mostre os carros ':
                print(dict_main)
                return render_templete('criarlot.html', result=dict_main)










_name__ == '__main__':

    app.run()
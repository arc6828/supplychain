# -*- coding: utf-8 -*-
import numpy as np
import urllib, json

import requests

class ExportPotential:
    def __init__(self):
        print("Hello")

    @staticmethod
    def getCountries():
        print("Countries")   
        
        #FETCH
        url = "https://exportpotential.intracen.org/api/en/countries"        
        r = requests.get(url)
        print(r.json())
        
        #SAVE
        data = r.json()        
        with open('countries.json', 'w') as outfile:
            json.dump(data, outfile)
            
    
    @staticmethod
    def readCountries():
        print("Countries")   
        #READ
        with open('countries.json') as json_file:
            data = json.load(json_file)
            for c in data:
                print('Id: ' + c['code'])
                print('Country: ' + c['name'])
            print(len(data))
            
    @staticmethod
    def saveRankingProductsFromCountries():
        print("Countries")   
        #READ
        with open('countries.json') as json_file:
            data = json.load(json_file)
            length = len(data)
            i=1
            for c in data:
                
                #print(len(data))
                #FETCH
                url = "https://exportpotential.intracen.org/api/en/epis/products/from/i/764/to/j/"+c['code']+"/what/k/all"        
                r = requests.get(url)
                print(r.json())
                
                #SAVE
                data = r.json()        
                with open('products/'+c['name']+'.json', 'w') as outfile:
                    json.dump(data, outfile)
                
                txt = "{0}/{1} : ({2}) {3}".format( i, length , c['code'] , c['name'])
                print(txt)
                i = i + 1
                break;
        
        
    
    
        

ExportPotential.saveRankingProductsFromCountries()



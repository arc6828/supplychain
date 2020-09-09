# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import urllib, json
import os

import requests

class ExportPotential:
    def __init__(self):
        print("Hello")
        
    @staticmethod
    def getProducts():
        print("Products")   
        
        #FETCH
        url = "https://exportpotential.intracen.org/api/en/products"        
        r = requests.get(url)
        #print(r.json())
        
        #SAVE
        data = r.json()        
        with open('standard-products.json', 'w') as outfile:
            json.dump(data, outfile)

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
    def getWorld():
        print("World")   
        
        #FETCH
        url = "https://exportpotential.intracen.org/api/en/epis/products/from/i/764/to/w/all/what/k/all"        
        r = requests.get(url)
        #print(r.json())
        
        
        data = r.json()   
        
        #READ
        with open('all_products.json') as json_file:
            products = json.load(json_file)
            keys = list(map(lambda item : str(item['code']) , products))
            print(keys)
            data = list(filter(lambda item : (item['ItemCode'] in keys) , data)) 
            
        #SAVE
        with open('products/World-5P.json', 'w') as outfile:
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
    def saveRankingProducts():
        print("Countries")   
        #READ
        with open('countries.json') as json_file:
            data = json.load(json_file)
            data.append({"code":"World", "name":"World"})
            length = len(data)
            i=1
            for c in data:                
                filename = "products/"+c['name']+".json"
                if os.path.isfile(filename):
                    i = i + 1
                    continue
                #print(len(data))
                #FETCH
                url = "https://exportpotential.intracen.org/api/en/epis/products/from/i/764/to/j/"+c['code']+"/what/k/all"        
                if c['code'] == "World":
                    url = "https://exportpotential.intracen.org/api/en/epis/products/from/i/764/to/w/all/what/k/all"
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
                    'Accept-Language' :'en-US,en;q=0.9,th;q=0.8'
                }
                r = requests.get(url, headers=headers)
                r = requests.get(url)
                print(r)
                print(url)
                
                #SAVE
                data = r.json()        
                with open(filename, 'w') as outfile:
                    json.dump(data, outfile)
                
                txt = "Success {0}/{1} : ({2}) {3}".format( i, length , c['code'] , c['name'])
                print(txt)
                i = i + 1
                #break;
        
        
    @staticmethod
    def saveRankingMarkets():
        if os.path.isfile('products.json'):
            print("Product")   
        #READ
        with open('products.json','r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            #data.append({"code":"World", "name":"World"})
            length = len(data)
            i=1
            for c in data:
                filename = "markets/{0}-{1}-{2}.json".format(c['category'],c['code'],c['name'])
                if os.path.isfile(filename):
                    i = i + 1
                    continue
                #print(len(data))
                #FETCH
                url = "https://exportpotential.intracen.org/api/en/epis/markets/from/i/764/to/j/all/what/k/"+c['code']                       
                r = requests.get(url)
                #print(r)
                #print(url)
                
                #SAVE
                data = r.json()        
                with open(filename, 'w') as outfile:
                    json.dump(data, outfile)
                
                txt = "Success {0}/{1} : ({2}) {3}".format( i, length , c['code'] , c['name'])
                print(txt)
                i = i + 1
                #break; 
                
    @staticmethod
    def saveRankingExporters():
        if os.path.isfile('products.json'):
            print("Product")   
        #READ
        with open('countries.json','r', encoding='utf-8') as json_file:
            countries = json.load(json_file)
            #data.append({"code":"World", "name":"World"})
            #length = len(data)
            with open('products.json','r', encoding='utf-8') as json_file:
                data = json.load(json_file)
                #data.append({"code":"World", "name":"World"})
                length = len(data)
                i=1
                for country in countries :
                    for c in data:
                        filename = "exporters/"+country['name']+"/{0}-{1}-{2}.json".format(c['category'],c['code'],c['name'])
                        if not os.path.exists("exporters/"+country['name']):
                            os.makedirs("exporters/"+country['name'])
                        if os.path.isfile(filename):
                            i = i + 1
                            continue
                        #print(len(data))
                        #FETCH
                        #url = "https://exportpotential.intracen.org/api/en/epis/markets/from/i/764/to/j/all/what/k/"+c['code']                       
                        url = "https://exportpotential.intracen.org/api/en/epis/exporters/from/r/all/to/j/"+country['code']+"/what/k/"+c['code'] 
                        r = requests.get(url)
                        #print(r)
                        #print(url)
                        
                        #SAVE
                        data = r.json()        
                        with open(filename, 'w') as outfile:
                            json.dump(data, outfile)
                        
                        txt = "Success {4} {0}/{1} : ({2}) {3}".format( i, length , c['code'] , c['name'],country['name'])
                        print(txt)
                        i = i + 1
                        #break; 
                        
    @staticmethod
    def convertJsonToExcel(source, target):
        #https://www.marsja.se/how-to-convert-json-to-excel-python-pandas/
        print(555)
        #READ
        with open(source) as json_file:
            data = json.load(json_file)
            # for c in data:
            #     print('Id: ' + c['code'])
            #     print('Country: ' + c['name'])
            # print(len(data))
            
            df = pd.DataFrame(data)
            df.to_excel(target)
            
    @staticmethod
    def convertExcelToJson(source,sheet,target):
        #https://www.journaldev.com/33335/python-excel-to-json-conversion
        excel_data_df = pd.read_excel(source, sheet_name=sheet)
        json_str = excel_data_df.to_json(orient='records')
                
        #SAVE        
        data = json.loads(json_str)     
        with open(target, 'w') as outfile:
            json.dump(data, outfile)
        
        
                
           
    
        

# ExportPotential.saveRankingProducts()
ExportPotential.getWorld()
# ExportPotential.saveRankingMarkets()
# ExportPotential.saveRankingExporters()

# ExportPotential.getProducts()
            
# ExportPotential.convertJsonToExcel("standard-products.json", "hscode_ept.xlsx")
# ExportPotential.convertExcelToJson("hscode_ept.xlsx", "Sheet2", "all_products.json")


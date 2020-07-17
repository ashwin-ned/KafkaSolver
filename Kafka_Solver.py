#!/usr/bin/python3.7
"""
Yungo Coding Challenge - Kafka SLD
Start Date: 16.07.2020
End Date:
Author: Ashwin Nedungadi
"""
import os
import math
import csv





def import_data():

    sld = list()
    with open(filename, 'r') as csvfile:
        for line in csvfile:
            row = (line.split(','))
            #print(row[0],row[1],row[2])
            #print(row[1])
            sld.append(row[1])
        sld.sort()  # Puts header last to pop later
        for val in sld:
            sld_schema = val.split(';')
            sld_schema.pop()
            L = len(sld_schema)
            sld_schema = list(map(int, sld_schema))

            S = sum(sld_schema)

            print(L,val, S)
            
            #print(sld_schema)
            











if __name__ == "__main__":

    rootdir = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge'
    filename = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge\kafka_sld.csv'
        
    import_data()

    #Sort_data()

 

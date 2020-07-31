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
from operator import itemgetter
import numpy as np
w = 50
h = 50
output_matrix = [[0 for x in range(w)] for y in range(h)]

def sld_data():
    """ Prints SLD Data in a Matrix with trailing zeros"""

    sld = list()
    with open(filename, 'r') as csvfile:
        for line in csvfile:
            row = (line.split(','))
            #print(row[0],row[1],row[2]) # Row index corresponds directly to Colum in CSV
            sld.append(row[1])
        sld.sort()  # Puts header last to pop later
        for val in sld:
            sld_schema = val.split(';')
            sld_schema.pop()


            L = len(sld_schema)

            sld_schema = list(map(int, sld_schema))

            S = sum(sld_schema)

            if len(sld_schema) != 45:       # 45 as it was the max len of sld_schema
                zeros = 45 - len(sld_schema)
                for i in range(zeros):
                    sld_schema.append(0)
            print(sld_schema)

def make_matrix(sld_matrix):
    """len(sld_array) ---> Y Position"""
    #x_pos = len(sld_array)
    #y_pos = sld_array.pop()

    for cable in sld_matrix:
        cable_id = cable[0]
        sld_array = cable[1]

        #print(cable_id,sld_array)

        x_pos = len(sld_array)
        y_pos = sld_array.pop()

        output_matrix[x_pos][y_pos] = cable_id



def matrix_sort(array):

    #array.sort(key=lambda item: (-len(item), item), reverse = True)
    #sorted(array,key=lambda x:(-x[1],x[0]))
    array.sort(key=itemgetter(1))
    for val in array:
        l = len(val[1])
        print(val, l)
        #sorted(val, key = l)


def extract_sld():
        sld = list()
        cable_id = list()
        matrix = list()

        sld_matrix = list()

        with open(filename, 'r') as csvfile:
            for line in csvfile:
                row = (line.split(','))

                sld.append(row[1])
                cable_id.append(row[0])
            sld.sort()  # Puts header last to pop later

            for val in sld:
                sld_schema = val.split(';')
                sld_schema.pop()
                L = len(sld_schema)
                sld_schema = list(map(int, sld_schema))
                #print(sld_schema)
                matrix.append(sld_schema)

            cable_id.pop(0)
            matrix.pop()
            #print(cable_id, len(matrix), len(cable_id))

            for i in range(len(cable_id)):
                sld_matrix.append([cable_id[i],matrix[i]])

            #matrix_sort(sld_matrix)
            #print(sld_matrix)
            make_matrix(sld_matrix)

            #matrix.sort(key=lambda item: (-len(item), item), reverse = True)
            #for l in matrix:
                #print(l)
                #make_matrix(l)




if __name__ == "__main__":

    rootdir = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge'
    filename = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge\kafka_sld.csv'

    #sld_data()
    extract_sld()
    #print(np.matrix(output_matrix))

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

def recurse_position(x_pos, y_pos, cable_id, sld_len):

    if output_matrix[y_pos-1][x_pos-1] == 0:
        output_matrix[y_pos-1][x_pos-1] = cable_id + "-" + sld_len
        return
    else:
        y_pos += 1
        recurse_position(x_pos, y_pos, cable_id, sld_len)

def make_matrix(sld_matrix):
    """len(sld_array) ---> Y Position"""
    #x_pos = len(sld_array)  col
    #y_pos = sld_array.pop() row

    for cable in sld_matrix:
        cable_id = cable[0]
        sld_array = cable[1]
        sld_len = len(sld_array)

        #CV = sorted(cable, key=itemgetter(1))
        #CV = cable.sort(key = lambda i:i[1])

        x_pos = len(sld_array)
        y_pos = sld_array.pop()
        #print(CV)
        #print(cable)
        #print(cable_id,y_pos,x_pos)
        recurse_position(x_pos, y_pos, str(cable_id), str(sld_len))

        #print(cable_id,y_pos,x_pos)

def print_sld_matrix(array):

    for Ar in array:
        #Ar = list(map(int, Ar))
        #if sum(Ar) != 0:
        print(Ar)

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

            sld_matrix.sort(key = lambda x: len(x[1]))
            #sld_matrix = sorted(sld_matrix, key= lambda x : len(sld_matrix[1]))
            #print(sld_matrix)
            #matrix_sort(sld_matrix)
            #for sld in sld_matrix:
                #print(sld)
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
    #print(output_matrix)
    print_sld_matrix(output_matrix)

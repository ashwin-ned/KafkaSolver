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

def recurse_position(x_pos, y_pos, cable_id, sld_len):

    if output_matrix[y_pos-1][x_pos-1] == 0:
        output_matrix[y_pos-1][x_pos-1] = cable_id
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



        x_pos = len(sld_array)
        y_pos = sld_array.pop()

        recurse_position(x_pos, y_pos, cable_id, sld_len)

def print_sld_matrix(array):

    for Ar in array:
        Ar = [ int(x) for x in Ar ]
        if sum(Ar) != 0:
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

            #for val in sld_matrix:
                #print(val[1])
            make_matrix(sld_matrix)



if __name__ == "__main__":

    rootdir = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge'
    filename = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge\kafka_sld.csv'


    extract_sld()

    print_sld_matrix(output_matrix)

#!/usr/bin/python3.7
"""
'ascii': ('|', '|-- ', '+-- '),
            'ascii-ex': ('\u2502', '\u251c\u2500\u2500 ', '\u2514\u2500\u2500 '),
            'ascii-exr': ('\u2502', '\u251c\u2500\u2500 ', '\u2570\u2500\u2500 '),
            'ascii-em': ('\u2551', '\u2560\u2550\u2550 ', '\u255a\u2550\u2550 '),
            'ascii-emv': ('\u2551', '\u255f\u2500\u2500 ', '\u2559\u2500\u2500 '),
            'ascii-emh
"""
import os
import math
import csv
#import treelib
from treelib import Node, Tree

def import_data():

    sld = list() # List with SLD Schema
    tree = Tree()
    Nodes = list()

    with open(filename, 'r') as csvfile:
        line_number = 0
        for line in csvfile:
            line_number += 1
            row = (line.split(','))
            sld.append(row[1])
            #print(row[4], '---->', row[7])
            Nodes.append([row[4],row[7],row[0]])
            #tree.create_node(row[3], parent = row[4])
        Nodes.pop()
        Nodes.pop(0)
        Nodes.pop(0)
        #print(Nodes)
        sld.sort()  # Puts header last to pop later
        for val in sld:
            sld_schema = val.split(';')
            sld_schema.pop()


        """ MAKING THE TREE"""

        tree.create_node("72","GAL/A001")
        tree.create_node("25", "GAL/A002", parent="GAL/A001")
        Nodes.pop(0)
        for n in Nodes:
            tree.create_node(n[2], n[1], parent = n[0])



        tree.show(nid = None, idhidden=False, line_type='ascii-em')


if __name__ == "__main__":

    rootdir = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge'
    filename = r'C:\Users\AshwinNedungadi\Desktop\GraphChallenge\kafka_sld.csv'

    import_data()

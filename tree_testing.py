#!/usr/bin/python3.7
"""
Yungo Coding Challenge - Kafka SLD
Start Date: 16.07.2020
End Date:
Author: Ashwin Nedungadi
"""

from treelib import Node, Tree


tree = Tree()


tree.create_node("GAL/A001","GAL/A001")

tree.create_node("GAL/A002", "GAL/A002", parent="GAL/A001")

tree.create_node("GAL/A003", "GAL/A003", parent="GAL/A002")

tree.create_node("GAL/A007", "GAL/A007", parent="GAL/A003")
tree.create_node("GAL/A005", "GAL/A005", parent="GAL/A007")
tree.create_node("GAL/A006", "GAL/A006", parent="GAL/A007")
tree.create_node("GAL/A004", "GAL/A004", parent="GAL/A007")
#tree.create_node("GAL/A007", "GAL/A007a", parent="GAL/A273")

tree.create_node("GAL/A008", "GAL/A008", parent="GAL/A001")
tree.create_node("GAL/A274", "GAL/A274", parent="GAL/A008")
tree.create_node("GAL/A010", "GAL/A010", parent="GAL/A274")

tree.create_node("GAL/A009", "GAL/A009", parent="GAL/A274")
tree.create_node("GAL/A011", "GAL/A011", parent="GAL/A274")

tree.show()

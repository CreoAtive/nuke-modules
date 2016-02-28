import nuke

import sys
import os

sys.path.append(os.path.dirname(__file__))

import myexceptions

def assertNode(curr_node):
    if isinstance(curr_node, nuke.Node):
        return True

    return False

def matchNode(curr_node, node_name):
    if not assertNode(curr_node): raise myexceptions.NoNodeException('matchNode: curr_node is not an instance of nuke.Node')

    return (curr_node.Class().lower() == node_name.lower() or curr_node.name().lower().startswith(node_name.lower()))

def findNode(node_name):
    for node in nuke.allNodes():
        if matchNode(node, node_name):
            return node

    raise myexceptions.NoMatchException('findNode: No node matches {node_name}'.format(node_name = node_name))

import nuke

import sys
import os

sys.path.append(os.path.dirname(__file__))

import nodes
import myexceptions

def findNodeUpstream(curr_node, node_name):
    if not nodes.assertNode(curr_node): raise myexceptions.NoNodeException('findNodeUpstream: curr_node is not an instance of nuke.Node')

    if nodes.matchNode(curr_node, node_name):
        return curr_node
    else:
        for index in range(curr_node.inputs()):
            if curr_node.input(index):
                try:
                    result = findNodeUpstream(curr_node.input(index), node_name)
                except myexceptions.NoMatchException:
                    pass
                else:
                    return result

    raise myexceptions.NoMatchException('findNodeUpstream: No matching node could be found')

def findNodeDownstream(curr_node, node_name):
    if not nodes.assertNode(curr_node): raise myexceptions.NoNodeException('findNodeDownstream: curr_node is not an instance of nuke.Node')

    if nodes.matchNode(curr_node, node_name):
        return curr_node
    else:
        for dependee in curr_node.dependent():
            try:
                result = findNodeDownstream(dependee, node_name)
            except myexceptions.NoMatchException:
                pass
            else:
                return result

    raise myexceptions.NoMatchException('findNodeDownstream: No matching node could be found')

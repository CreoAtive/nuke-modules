import nuke

import sys
import os

sys.path.append(os.path.dirname(__file__))

import nodes
import nodetree
import myexceptions
import testing

reload(nodes)
reload(nodetree)
reload(testing)

def formatException(exception, message):
    return '{exception}: {message}'.format(exception = exception.__name__, message = message)

def findNodeUpstreamTest():
    start_node = 'Write1'
    find_node = 'Read'

    upstream_test = testing.Test('findNodeUpstreamTest').ensure(lambda: nodes.findNode(start_node)).condition(lambda x: x.name() == start_node).then(lambda x: nodetree.findNodeUpstream(x, find_node)).condition(lambda x: x.name() == find_node).evaluate()

def findNodeDownstreamTest():
    start_node = 'Read1'
    find_node = 'Viewer1'

    downstream_test = testing.Test('findNodeDownstreamTest').ensure(lambda: nodes.findNode(start_node)).condition(lambda x: x.name() == start_node).then(lambda x: nodetree.findNodeDownstream(x, find_node)).condition(lambda x: x.name() == find_node).evaluate()

def findNodeDownstreamTestOld():
    start_node = 'Read1'
    find_node = 'Viewer1'

    print 'Start findNodeDownstreamTest'

    try:
        selected_node = nodes.findNode(start_node)
    except myexceptions.NoMatchException as message:
        print formatException(myexceptions.NoMatchException, message)
    else:
        try:
            matching_node = nodetree.findNodeDownstream(selected_node, find_node)
        except myexceptions.NoNodeException as message:
            print formatException(myexceptions.NoNodeException, message)
        except myexceptions.NoMatchException as message:
            print formatException(myexceptions.NoMatchException, message)
        else:
            assert matching_node.name() == find_node, 'matching_node name is not matching {name}'.format(name = find_node)

            print 'Test Passed'
    finally:
        print 'Finished Test'

def main():
    findNodeUpstreamTest()

    findNodeDownstreamTest()

if __name__ == '__main__':
    main()

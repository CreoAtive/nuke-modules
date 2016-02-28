# nuke-modules

## nodes.py

The Nodes-Module contains some basic methods for identifying and finding a node in the nukescript

### Find a node in nukescript

```python
import nodes

matching_node = nodes.findNode('Read1')
```

## nodetree.py

The Nodetree-Module contains methods for traversing up and down the nodetree. This works only for connected nodes and will include multiple inputs and outputs of nodes to find the first matching node.

### Find a node upstream

```python
import nuke

import nodetree

current_node = nuke.selectedNodes()[0]
matching_node = nodetree.findNodeUpstream(current_node, 'Read1')
```

### Find a node downstream

```python
import nuke

import nodetree

current_node = nuke.selectedNodes()[0]
matching_node = nodetree.findNodeDownstream(current_node, 'Write1')
```

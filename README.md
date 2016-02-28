# nuke-modules

## Find a node in nukescript

```python
import nodes

matching_node = nodes.findNode('Read1')
```

## Find a node upstream

```python
import nuke

import nodetree

current_node = nuke.selectedNodes()[0]
matching_node = nodetree.findNodeUpstream(current_node, 'Read1')
```

## Find a node downstream

```python
import nuke

import nodetree

current_node = nuke.selectedNodes()[0]
matching_node = nodetree.findNodeDownstream(current_node, 'Write1')
```

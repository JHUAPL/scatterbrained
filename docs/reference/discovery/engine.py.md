## *Class* `DiscoveryEngine`


A `DiscoveryEngine` is a manager class for the process of identifying and communicating with other peers in the Scatterbrained network.

The `DiscoveryEngine` is responsible for maintaining a list of peers, and periodically sending heartbeats to the network, which other peers can use to determine if the sending node is still alive.

Identities of peers are stored in `DiscoveryEngine.peers`.

Identities of the current node are stored in `DiscoveryEngine.identities` and can be manually added or removed using `DiscoveryEngine.add_identity` and `DiscoveryEngine.remove_identity`.


## *Function* `heartbeat(self)`


Retrieve the heartbeat interval in seconds.


## *Function* `heartbeat(self, value)`


Set the heartbeat interval in seconds.

### Arguments
> - **value** (`float`: `None`): The heartbeat interval in seconds.

### Returns
    None



## *Function* `peers(self)`


Retrieve the list of peers.

### Returns
> - **Set[scatterbrained.discovery.types.Identity]** (`None`: `None`): The list of peers.



## *Function* `add_identity(self, identity: Identity) -> None`


Add an identity to the list of identities for the current node.

### Arguments
> - **identity** (`scatterbrained.discovery.types.Identity`: `None`): The identity to add.

### Returns
    None



## *Function* `remove_identity(self, identity: Identity) -> None`


Remove an identity from the list of valid identities for the node.

### Arguments
> - **identity** (`scatterbrained.discovery.types.Identity`: `None`): The identity to remove.

### Returns
    None



## *Function* `stop(self)`


Gracefully stop the `DiscoveryEngine`.

### Returns
    None

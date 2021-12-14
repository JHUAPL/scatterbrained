## *Class* `OperatingMode(Enum)`


The mode for the Node to operate in.

> - **Leech** (`None`: `None`): Listen for broadcasts; do not share.
> - **Offline** (`None`: `None`): Do not listen or broadcast.
> - **Peer** (`None`: `None`): Listen and broadcast.
> - **Seeding** (`None`: `None`): Broadcast but do not listen.



## *Class* `Namespace`


A Namespace is a collection of Scatterbrained nodes that share a common model or parameter state space. When connecting or disconnecting from a community, a Scatterbrained node joins a named namespace, or creates a new namespace with a unique name.

Note that this  class shouldn't be instantiated directly, rather instances should created via the `scatterbrained.Node.namespace` method.



## *Function* `operating_mode(self)`


Get the operating mode for this namespace.

### Returns
> - **scatterbrained.OperatingMode** (`None`: `None`): The operating mode for this namespace.



## *Function* `launch(self)`


Launch the Namespace.

This is usually done by entering the `Namespace` context manager. You should not need to call this method directly.



## *Function* `close(self)`


Close out the Namespace gracefully.

This is usually done by exiting the `Namespace` context manager. You should not need to call this method directly.



## *Function* `connect_to(self, peer: Identity) -> bool`


Connect to a peer in this Namespace by its Identity.

The method will not connect to the given peer if the `OperatingMode` of this Namespace is either `LEECHING` or `OFFLINE`, or the `Identity` is rejected by this instance's `peer_filter`.

### Arguments
> - **peer** (`scatterbrained.Identity`: `None`): The peer to connect to.

### Returns
> - **bool** (`None`: `None`): `True` if the connection was successful, `False` otherwise.



## *Function* `disconnect_from(self, peer: Identity) -> bool`


Disconnect from a peer in this `Namespace` by its `Identity`.

### Arguments
> - **peer** (`scatterbrained.Identity`: `None`): The peer to disconnect from.

### Returns
> - **bool** (`None`: `None`): `True` if the disconnection was successful, `False` otherwise.



## *Function* `send_to(self, peer: Identity, *payload: bytes) -> None`


Send a byte sequence payload to a peer by its `Identity`.

### Arguments
> - **peer** (`scatterbrained.Identity`: `None`): The peer to send to.
> - **payload** (`bytes`: `None`): The payload to send.

### Returns
    None



## *Function* `recv(self, timeout: Optional[float] = None) -> Tuple[Identity, Sequence[bytes]]`


Receive a message from the network.

This will block until a message is received, or the timeout is reached.

### Arguments
> - **timeout** (`float`: `None`): The timeout in seconds to wait for a message to be received.

### Returns
> - **bytes]** (`None`: `None`): The sender's Identity and the payload.



## *Class* `Node`


Scatterbrained peer node.

Manages all networking infrastructure, providing an interface for other  classes to establish connections, and send and receive data.


## *Function* `listening(self)`


Whether or not the `Node` is listening for incoming connections.

### Returns
> - **bool** (`None`: `None`): Whether or not the Node is listening for incoming connections.



## *Function* `launch(self) -> None`


Launch the `Node`.

This will start the `DiscoveryEngine` and `NetworkEngine` and begin listening for new connections.

Note that this method is usually called automatically when entering an `async with` block and is not meant to be called manually.

### Returns
    None



## *Function* `close(self)`


Gracefully close the `Node`.

This will close the `DiscoveryEngine` and `NetworkEngine`.

Note that this method is usually called automatically when exiting an `async with` block and is not meant to be called manually.

### Returns
    None



## *Function* `namespace(self, name: str, *args, **kwargs) -> Namespace`


Gets the namespace with the given name, or creates a new one.

Also accepts the same arguments as `scatterbrained.Namespace` if creating a new namespace.

### Arguments
> - **name** (`str`: `None`): The name of the namespace.

### Returns
> - **scatterbrained.Namespace** (`None`: `None`): The namespace with the given name.

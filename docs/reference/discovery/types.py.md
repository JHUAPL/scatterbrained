## *Class* `Publisher(Protocol)`


A Publisher is a class that can publish a message to a set of peers.

Note that this is a protocol and shouldn't be used directly!



## *Function* `publish(self, data: bytes) -> None`


Publish the given payload to a set of peers.


## *Function* `open(self) -> None`


Open the underlying connection mechanism, enabling this instance to send messages.


## *Function* `close(self) -> None`


Close the underlying connection mechanism, stopping this instance from sending messages.


## *Class* `Subscriber(Protocol)`


A Subscriber is a class that can subscribe to messages from a set of peers.

Note that this is a protocol and shouldn't be used directly!



## *Function* `open(self) -> None`


Open the underlying connection mechanism, enabling this instance to receive messages.


## *Function* `close(self) -> None`


Close the underlying connection mechanism, stopping this instance from receiving messages.

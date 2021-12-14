from dataclasses import dataclass


@dataclass(frozen=True)
class Identity:
    """
    Represents the identity of a scatterbrained.Node (either local or remote) for a particular namespace.

    Args:
        id (str): The id of the Node.
        namespace (str): The namespace the Node is operating in.
        host (str): The advertised address of this Node.
        port (int): The advertised port of this Node.

    """

    id: str
    namespace: str
    host: str
    port: int


__all__ = ["Identity"]

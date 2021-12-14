import asyncio

import scatterbrained as sb


async def main():
    # NOTE: in a real deployment you'd want everything to use the same port, but because we're running on the
    # same system here, we need to bind to different ports.
    de1 = sb.discovery.DiscoveryEngine(
        publisher=sb.discovery.UDPBroadcaster("127.0.0.1", port=9002),
        subscriber=sb.discovery.UDPReceiver("127.0.0.1", port=9001),
        heartbeat=2,
    )
    de2 = sb.discovery.DiscoveryEngine(
        publisher=sb.discovery.UDPBroadcaster("127.0.0.1", port=9001),
        subscriber=sb.discovery.UDPReceiver("127.0.0.1", port=9002),
        heartbeat=2,
    )
    async with sb.Node(id="foo", host="127.0.0.1", discovery_engine=de1) as node1, sb.Node(
        id="bar", host="127.0.0.1", discovery_engine=de2
    ) as node2:
        async with node1.namespace(name="foobar") as ns1, node2.namespace(name="foobar") as ns2:
            await asyncio.gather(ns1.wait_for_peers(peers="bar"), ns2.wait_for_peers(peers="foo"))
            await ns1.send_to(ns2._id, b"hello")
            sender, payload = await ns2.recv(5.0)
            print(sender, payload)
            await asyncio.sleep(10)
        await asyncio.sleep(15)


if __name__ == "__main__":
    asyncio.run(main())

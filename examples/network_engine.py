import asyncio

import scatterbrained as sb


async def send_msgs(engine, identity, peer, n=10):
    for i in range(n):
        await engine.send_to(identity, peer, f"hello there x{i}".encode())
        await asyncio.sleep(1.0)


async def main():
    id1 = sb.types.Identity("foo", "baz", "127.0.0.1", 9001)
    id2 = sb.types.Identity("bar", "baz", "127.0.0.1", 9002)

    rx1 = sb.network.ZMQReceiver()
    rx2 = sb.network.ZMQReceiver()

    ne1 = sb.network.NetworkEngine(rx1, lambda: sb.network.ZMQTransmitter("foo"))
    ne2 = sb.network.NetworkEngine(rx2, lambda: sb.network.ZMQTransmitter("bar"))

    await ne1.bind(id1.host, id1.port)
    await ne2.bind(id2.host, id2.port)

    await ne1.connect_to(id2)
    await ne2.connect_to(id1)

    async def on_recv(identity, payload):
        print("RECV:", identity, payload)

    async def on_malformed(peer_id, segments):
        print("MALFORMED:", peer_id, segments)

    async def on_error(ex):
        print("ERROR", ex)

    d1 = ne1.subscribe(on_recv=on_recv, on_malformed=on_malformed, on_error=on_error)
    d2 = ne2.subscribe(on_recv=on_recv, on_malformed=on_malformed, on_error=on_error)

    await asyncio.wait([send_msgs(ne1, id1, id2), send_msgs(ne2, id2, id1)])

    await asyncio.sleep(1.0)
    await d1.dispose()
    await d2.dispose()


if __name__ == "__main__":
    asyncio.run(main())

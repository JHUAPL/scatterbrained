import asyncio
import dataclasses
import json

from loguru import logger

import scatterbrained as sb


async def on_appear(v):
    await asyncio.sleep(0.1)
    logger.info(f"Appear: {v}")


async def on_disappear(v):
    await asyncio.sleep(0.1)
    logger.info(f"Disappear: {v}")


async def on_error(e):
    await asyncio.sleep(0.1)
    logger.opt(exception=e).error("local error")


async def on_remote_recv(v):
    logger.info(f"Remote: {v}")


async def on_remote_error(e):
    logger.opt(exception=e).error("remote error")


async def main():
    # NOTE: in a real deployment you'd want everything to use the same port, but because we're running on the
    # same system here, we need to bind to different ports.
    local_pub = sb.discovery.udp.UDPBroadcaster("127.0.0.1", port=9002)
    local_sub = sb.discovery.udp.UDPReceiver("127.0.0.1", port=9001)
    # Fake a remote node.
    remote_pub = sb.discovery.udp.UDPBroadcaster("127.0.0.1", port=9001)
    remote_sub = sb.discovery.udp.UDPReceiver("127.0.0.1", port=9002)

    await asyncio.wait([local_pub.open(), local_sub.open(), remote_pub.open(), remote_sub.open()])

    engine = sb.discovery.DiscoveryEngine(
        local_pub,
        local_sub,
        identities=[sb.types.Identity(id="baz", namespace="bar", host="omg", port=3223)],
        heartbeat=2,
    )
    await engine.start(on_appear=on_appear, on_disappear=on_disappear, on_error=on_error)

    peer = sb.types.Identity(id="foo", namespace="bar", host="meme", port=32233)

    remote_sub.subscribe(on_recv=on_remote_recv, on_error=on_error)
    await remote_pub.publish(json.dumps(dataclasses.asdict(peer)).encode())
    await asyncio.sleep(15)

    await engine.stop()
    await asyncio.wait([local_pub.close(), local_sub.close(), remote_pub.close(), remote_sub.close()])


if __name__ == "__main__":
    asyncio.run(main())

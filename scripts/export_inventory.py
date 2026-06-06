import asyncio
import csv
import json
import os
from pathlib import Path

import websockets
from dotenv import load_dotenv

load_dotenv()

HA_URL = os.getenv("HA_URL")
HA_TOKEN = os.getenv("HA_TOKEN")

WS_URL = HA_URL.replace("http://", "ws://").replace("https://", "wss://")
WS_URL += "/api/websocket"

DOCS = Path("docs")
DOCS.mkdir(exist_ok=True)

async def ws_call(ws, msg_id, msg_type):
    await ws.send(json.dumps({
        "id": msg_id,
        "type": msg_type
    }))

    while True:
        msg = json.loads(await ws.recv())
        if msg.get("id") == msg_id:
            return msg["result"]

async def export():
    async with websockets.connect(WS_URL) as ws:

        # auth_required
        await ws.recv()

        await ws.send(json.dumps({
            "type": "auth",
            "access_token": HA_TOKEN
        }))

        await ws.recv()

        areas = await ws_call(ws, 1, "config/area_registry/list")
        devices = await ws_call(ws, 2, "config/device_registry/list")
        entities = await ws_call(ws, 3, "config/entity_registry/list")

        with open(DOCS / "areas.json", "w", encoding="utf-8") as f:
            json.dump(areas, f, indent=2, ensure_ascii=False)

        with open(DOCS / "devices.json", "w", encoding="utf-8") as f:
            json.dump(devices, f, indent=2, ensure_ascii=False)

        with open(DOCS / "entity_registry.json", "w", encoding="utf-8") as f:
            json.dump(entities, f, indent=2, ensure_ascii=False)

        with open(DOCS / "areas.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "area_id",
                    "name",
                    "floor_id",
                    "icon",
                    "temperature_entity_id",
                    "humidity_entity_id",
                ],
                extrasaction="ignore",
            )
            writer.writeheader()
            writer.writerows(areas)

        with open(DOCS / "devices.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "id",
                    "name_by_user",
                    "name",
                    "area_id",
                    "manufacturer",
                    "model"
                ],
                extrasaction="ignore"
            )
            writer.writeheader()
            writer.writerows(devices)

        with open(DOCS / "entities.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "entity_id",
                    "device_id",
                    "area_id",
                    "original_name",
                    "platform"
                ],
                extrasaction="ignore"
            )
            writer.writeheader()
            writer.writerows(entities)

        print(f"Areas   : {len(areas)}")
        print(f"Devices : {len(devices)}")
        print(f"Entities: {len(entities)}")

asyncio.run(export())
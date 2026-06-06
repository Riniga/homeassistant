#!/usr/bin/env python3
import csv
import json
import os
import ssl
from pathlib import Path
from dotenv import load_dotenv
import urllib.request
from pathlib import Path

env_file = Path(__file__).parent.parent / ".env"
load_dotenv()

HA_URL = os.getenv("HA_URL", "http://192.168.20.60:8123").rstrip("/")
HA_TOKEN = os.getenv("HA_TOKEN")

OUT = Path("docs")
OUT.mkdir(exist_ok=True)

if not HA_TOKEN:
    raise SystemExit("Sätt HA_TOKEN först, t.ex. export HA_TOKEN='din_long_lived_token'")

def rest(path):
    req = urllib.request.Request(
        f"{HA_URL}{path}",
        headers={
            "Authorization": f"Bearer {HA_TOKEN}",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, context=ssl._create_unverified_context()) as r:
        return json.loads(r.read().decode())

def write_csv(filename, rows, columns):
    with open(OUT / filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

# REST API: states/entities
states = rest("/api/states")

entities = []
for s in states:
    attr = s.get("attributes", {})
    entities.append({
        "entity_id": s.get("entity_id"),
        "domain": s.get("entity_id", "").split(".")[0],
        "friendly_name": attr.get("friendly_name"),
        "state": s.get("state"),
        "unit": attr.get("unit_of_measurement"),
        "device_class": attr.get("device_class"),
        "state_class": attr.get("state_class"),
    })

write_csv(
    "entities.csv",
    sorted(entities, key=lambda x: x["entity_id"] or ""),
    ["entity_id", "domain", "friendly_name", "state", "unit", "device_class", "state_class"],
)

with open(OUT / "entities.json", "w", encoding="utf-8") as f:
    json.dump(states, f, ensure_ascii=False, indent=2)

print(f"Exporterade {len(entities)} entities till docs/entities.csv")
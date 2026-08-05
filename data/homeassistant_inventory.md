# Home Assistant Inventory

Denna katalog innehåller export av Home Assistant-konfigurationen.

## Areas

* [areas.csv](areas.csv) – Förenklad lista över alla områden (rum och ytor).
* [areas.json](areas.json) – Fullständig information om områden.

## Devices

* [devices.csv](devices.csv) – Förenklad lista över alla enheter.
* [devices.json](devices.json) – Fullständig information om enheter.

## Entities

* [entities.csv](entities.csv) – Förenklad lista över alla entiteter och deras egenskaper.
* [entity_registry.json](entity_registry.json) – Fullständig registrering av entiteter inklusive kopplingar till enheter och områden.

## Relationer

Home Assistant organiserar information enligt:

```text
Area
 └─ Device
     └─ Entity
```

Exempel:

```text
Tvättstuga
 └─ Temperaturgivare
     └─ sensor.tvattstuga_temperatur
```

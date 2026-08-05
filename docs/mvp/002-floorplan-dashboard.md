# MVP 2 — Floorplan Dashboard

## Purpose

Give the household an at-a-glance visual dashboard of the ground floor: a floorplan image with live entity state overlaid directly on each room, so lighting, doors/windows, and climate can be read spatially instead of from a list.

## Scope

This MVP covers a new, standalone Lovelace dashboard for the ground floor (`floor_id: markplan`) only:

* A new dashboard (`dashboards/floorplan.yaml`), registered under `lovelace.dashboards` in `configuration.yaml`, built with Home Assistant's native `picture-elements` card — no new custom component or HACS dependency. See [ADR 0002](../architecture/decisions/0002-native-picture-elements-for-floorplan.md) for why this was chosen over the already-installed but unused `ha-floorplan` HACS card.
* Background image: `www/floorplan-ground.png`.
* Ground-floor areas covered (per `data/areas.csv`): Förrådet, Groventre, Hall, Kontor, Kök, Sovrum, TV-Rum, Utomhus, Vardagsrum.
* Entities placed on the floorplan, identified from `data/entities.csv` / `data/devices.csv` for these areas:
  * **Lights** — icon appearance changes when a light in that area is on, so the floorplan shows which rooms are illuminated.
  * **Doors/windows** — binary sensor icons reflect open/closed state.
  * **Temperature/humidity** — shown as small badges wherever a sensor exists for that area; ground-floor sensor coverage is expected to be partial.
* Exact icon/badge placement on the image is determined collaboratively during implementation: Rickard identifies room locations and confirms/adjusts x/y percentages against the running dashboard.
* `docs/dashboards.md` and `docs/roadmap.md` updated once the dashboard is built.

## Acceptance Criteria

- [x] `docs/plans/002-floorplan-dashboard.plan.md` exists, breaking implementation into reviewable phases.
- [ ] `dashboards/floorplan.yaml` exists as a `picture-elements` dashboard using `www/floorplan-ground.png`, registered in `configuration.yaml`, and visible in the HA sidebar.
- [ ] Every entity placed on the floorplan sits over the correct room, confirmed visually by Rickard in the running dashboard — not just reviewed as static YAML.
- [ ] Lights in ground-floor areas visibly change appearance on the floorplan when toggled, verified live against at least one real light.
- [ ] Door/window binary sensors in ground-floor areas visibly change appearance when opened/closed, verified live against at least one real sensor.
- [ ] Temperature/humidity is shown for every ground-floor area with a matching sensor; areas without one are simply omitted rather than shown as unavailable.
- [ ] `docs/dashboards.md` and `docs/roadmap.md` reflect the new dashboard.
- [ ] `ha core check` passes after the change, and the dashboard has been validated on the live Home Assistant Pi per `docs/standards/testing.md`.

## Status

Todo. Scope finalized 2026-08-05 (card technology, placement, and effects confirmed with Rickard). Implementation plan created (`docs/plans/002-floorplan-dashboard.plan.md`); Phase 1 not yet started.

## Out of Scope

* **Pinch/zoom** on the floorplan — deferred as a future nice-to-have. Native `picture-elements` has no built-in support, and adding it would pull in another card/dependency, which is its own decision.
* Presence, vacuum position, alarm state, or other automation-state overlays on the floorplan.
* Basement (`kallare`), attic (`vind`), or any non-ground-floor areas — a possible future MVP if this one proves useful.
* Removing the unused `ha-floorplan` HACS resource or the old `www/floorplan/` SVG/CSS assets left over from an earlier, abandoned attempt — unrelated to this change, left alone per CLAUDE.md's scope rules.

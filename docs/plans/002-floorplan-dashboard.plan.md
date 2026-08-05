# Plan 002 — Floorplan Dashboard

## Goal

Implement MVP 2 (`docs/mvp/002-floorplan-dashboard.md`): a native `picture-elements` Lovelace dashboard for the ground floor that overlays live light, door/window, and temperature/humidity state on top of `www/floorplan-ground.png`, registered in the HA sidebar — with no new custom-component or HACS dependency, per [ADR 0002](../architecture/decisions/0002-native-picture-elements-for-floorplan.md).

## Assumptions

* Only native `picture-elements` primitives are used (`state-icon`, `state-badge`, `conditional`, and per-element `style:` overrides for positioning/color) — no `card-mod` or other HACS resource, consistent with ADR 0002.
* Exact x/y placement of each element is agreed live with Rickard against the running dashboard, not pre-computed from the image file alone. Every phase that adds elements ends with a short visual check-and-adjust pass rather than a one-shot guess.
* Ground-floor entity coverage is uneven across the 9 areas. Based on `data/entities.csv` / `data/devices.csv` as of 2026-08-05:

  | Area | Light | Door/window | Ambient temp/humidity |
  | --- | --- | --- | --- |
  | Förrådet | — | — | — |
  | Groventre | — | `binary_sensor.groventre_dorr` | — |
  | Hall | `light.hall`, `light.hallampa` | `binary_sensor.entre_oppning`, `binary_sensor.finentre_oppning` | `sensor.hall_temperatur` (temp only) |
  | Kontor | `light.kontor`, `light.kontor2`, `light.kontorslampa` | — | — |
  | Kök | — | `binary_sensor.dorr_mediaskap_oppning` (cabinet, not a room door) | — (only fridge/freezer sensors, appliance-level) |
  | Sovrum | — | — | `sensor.sensor_sovrum_multisensor_temperatur` / `..._luftfuktighet` |
  | TV-Rum | `light.taklampa_2` | `binary_sensor.altandorr_tv_rum_oppning` | `sensor.tv_rum_temperatur` / `..._luftfuktighet` |
  | Utomhus | `light.ute`, `light.hue_ambiance_lamp_1`, `light.hue_ambiance_lamp_2` | — | `sensor.utetemp_temperatur` / `..._luftfuktighet` |
  | Vardagsrum | `light.vagguttag_vardagsrum_inspelning` (wall outlet, not a room light) | `binary_sensor.altandorr_vardagsrum_oppning` | `sensor.sensor_kontor_luftkvalitet_temperatur` / `..._luftfuktighet` (device is area-assigned to Vardagsrum despite its `kontor`-prefixed entity ID) |

  Förrådet has no entities assigned to it in the registry at all.
* This plan does not aim for uniform coverage across all 9 areas. Each phase places whatever real entities exist for that layer; per the MVP's acceptance criteria, an area without a matching entity is simply omitted, not shown as unavailable.
* Phase 5 (visual polish) is a design/taste task, not a mechanical one. Rickard's live visual sign-off is the acceptance test for it — per the plan's requirement to use "the correct AI model" for this task, prefer a higher-capability/creative model or reasoning effort for that phase specifically, rather than the default used for the mechanical YAML phases.
* `ha core check` and sidebar/visual verification require the live Home Assistant Pi; static YAML review alone cannot confirm functional correctness (per `docs/standards/testing.md`).

## Proposed File Changes

### New

* `dashboards/floorplan.yaml` — the picture-elements dashboard.

### Modified

* `configuration.yaml` — register a `floorplan-dashboard` entry under `lovelace.dashboards`.
* `docs/dashboards.md` — add an entry for the new dashboard, matching the existing "Dashboard N - Name / Fråga / Visar" format.
* `docs/roadmap.md` — reflect the floorplan dashboard as the active/completed work (the "Now" section currently still says Project Foundation, which is stale since MVP 1 finished).
* `docs/mvp/002-floorplan-dashboard.md` — acceptance criteria checked off and Status updated as phases complete.

**Not touched:** `automations.yaml`, `scenes.yaml`, `scripts.yaml`, `custom_components/`, `secrets.yaml`, any other dashboard file.

## Implementation Phases

### Phase 1 — Dashboard skeleton and registration

1. Create `dashboards/floorplan.yaml` with a single `picture-elements` card showing `www/floorplan-ground.png` and no elements yet.
2. Register it in `configuration.yaml` under `lovelace.dashboards` (new key, sidebar icon, Swedish title matching the style of `Hemmet` / `Klimat` / `Teknik` / `Säkerhet` — confirm exact title with Rickard).
3. Run `ha core check`.

**Verify:** dashboard appears in the sidebar, opens, and the image renders at a reasonable size on both a desktop and a phone-width browser window.

**Suggested commit:** `Add floorplan dashboard skeleton`

**Status: implemented and validated.** `dashboards/floorplan.yaml` created and `floorplan-dashboard` registered in `configuration.yaml`, matching the existing dashboards' indentation. `ha core check` passed on the Pi; a full `ha core restart` was required for the new sidebar entry to appear (registering a *new* dashboard, unlike editing an already-registered one, isn't picked up by a reload). Initial `masonry` view made the floorplan image too small to be usable — switched to `panel`, which is Home Assistant's native full-bleed single-card view, still no new dependency. Re-verification of the `panel` view on the live Pi is the one remaining check for this phase.

### Phase 2 — Lights layer

1. For each light entity in the table above, add a `state-icon` element positioned over its room, placement agreed live with Rickard.
2. Confirm the default on/off icon coloring for the `light` domain is enough to read as "illuminated" at a glance; only add extra styling if it isn't.

**Verify:** toggle at least one real light (e.g. `light.hall`) and confirm the icon visibly changes on the dashboard.

**Suggested commit:** `Add lights to floorplan dashboard`

### Phase 3 — Doors/windows layer

1. For each binary sensor in the table above, add a `state-icon` element positioned over its door/opening.
2. Label or note `binary_sensor.dorr_mediaskap_oppning` clearly as a cabinet, not a room entry door, if included, to avoid misreading the floorplan.

**Verify:** open/close at least one real door or window covered by a sensor (or toggle the sensor's state from Developer Tools → States if physically opening it isn't practical) and confirm the icon updates.

**Suggested commit:** `Add door and window sensors to floorplan dashboard`

### Phase 4 — Temperature/humidity badges

1. For each sensor pair in the table above, add `state-badge` (or equivalent) elements positioned over their room.
2. Leave Förrådet, Groventre, Kontor, and Kök without a badge — no ambient sensor exists for them.

**Verify:** badge values match the corresponding entity's current state in Developer Tools → States.

**Suggested commit:** `Add temperature and humidity badges to floorplan dashboard`

### Phase 5 — Visual design pass

1. Review icon sizing, spacing, and color choices for legibility against the background image.
2. Refine using native `style:` overrides only (position, color, size, opacity) — no new dependency.
3. Check readability at both desktop and phone widths (no pinch-zoom, per the MVP's Out of Scope).
4. Get Rickard's explicit visual sign-off — this phase's acceptance criterion is subjective and can't be checked automatically.

**Verify:** Rickard confirms the dashboard looks good and is readable on the devices he actually uses.

**Suggested commit:** `Polish floorplan dashboard visual design`

### Phase 6 — Documentation updates

1. Add the new dashboard to `docs/dashboards.md`, following the existing format.
2. Update `docs/roadmap.md`: move the floorplan dashboard out of unaddressed and reflect current status; correct the stale "Now — Repository Foundation" section now that MVP 1 is complete.
3. Update `docs/mvp/002-floorplan-dashboard.md`: check off completed acceptance criteria, update Status.

**Verify:** review rendered Markdown; confirm no information is duplicated across `docs/dashboards.md` and `docs/roadmap.md` (per `docs/standards/documentation.md`'s single-source-of-truth rule).

**Suggested commit:** `Update dashboard and roadmap docs for floorplan dashboard`

### Phase 7 — Final validation and MVP close-out

1. Run `ha core check` against the complete dashboard.
2. Walk through every MVP 2 acceptance criterion on the live Pi with Rickard.
3. Confirm no unrelated files changed across all phases.

**Verify:** all MVP 2 acceptance criteria pass on the running instance, not just in static YAML.

**Suggested commit:** none expected — this phase validates prior commits rather than introducing new changes, unless a fix is needed.

## Risks / Open Questions

* **Förrådet has no entities at all.** Confirm with Rickard whether it should appear on the floorplan as a plain label with no live data, or be left unmarked for now.
* **Partial sensor/light coverage** (see the Assumptions table) means the floorplan will look asymmetric — some rooms rich with data, others empty. Confirm this is acceptable for MVP 2, or whether a couple of gaps (e.g. no light for Kök) should be flagged for future hardware/entity work rather than silently left blank.
* **`binary_sensor.dorr_mediaskap_oppning`** is a cabinet door in the kitchen, not a room entry door — worth confirming it should be on the floorplan at all, or whether it belongs on the Security dashboard only.
* **Coordinates are tied to the current image.** If `www/floorplan-ground.png` is ever replaced or resized, all element positions will need re-checking.
* **Raster background, not SVG.** Aligning small icons precisely over a photo-like PNG may be fiddlier than an SVG floorplan would be; if this proves too imprecise in practice, ADR 0002 may need revisiting for a future MVP.
* **"Appealing visual design" is subjective** and only verifiable by Rickard looking at it — Phase 5 has no automated pass/fail check.

# 0002. Native picture-elements card for the floorplan dashboard

## Status

Accepted

## Context

`docs/mvp/002-floorplan-dashboard.md` needs a floorplan-style dashboard showing live entity state over a background image of the ground floor. Two real options existed:

1. Home Assistant's native `picture-elements` card — built into HA core, YAML-authored like every other dashboard in this repo, no extra dependency.
2. `ha-floorplan`, a HACS-installed custom Lovelace card already present in this installation (visible as `update.ha_floorplan_update` in `dashboards/tech.yaml`) but never wired into a dashboard. An earlier, abandoned attempt left SVG/CSS assets for it in `www/floorplan/` (`home.svg`, `home.css`, `light_on.svg`, `light_off.svg`), which don't match the PNG background (`www/floorplan-ground.png`) prepared for this MVP.

`ha-floorplan` offers richer effects (SVG-based glow/highlight on state change, more natural polygon zones) and renders well under pinch/zoom, at the cost of being a custom-component dependency that CLAUDE.md requires explicitly justifying, and would mean either redrawing the floorplan as SVG or adapting the card to a raster background.

## Decision

Use the native `picture-elements` card for the floorplan dashboard, working directly against the provided PNG (`www/floorplan-ground.png`) with `state-icon` / `state-badge` / `conditional` elements positioned by x/y percentage. Per CLAUDE.md's "prefer native Home Assistant functionality over custom code," this is the default unless `picture-elements` proves insufficient for a specific effect during implementation.

The existing `ha-floorplan` HACS resource and the old `www/floorplan/` SVG/CSS assets are left in place, untouched, as out-of-scope cleanup rather than removed as part of this decision.

## Consequences

* No new dependency to install, update, or explain — consistent with how every other dashboard in this repo (`home.yaml`, `climate.yaml`, `tech.yaml`, `security.yaml`) is already built.
* "Illumination" and other visual effects are approximated with `picture-elements`' more limited primitives (icon color/opacity by state, conditional elements) rather than true SVG glow/highlight.
* No native pinch/zoom — tracked as Out of Scope in MVP 2.
* `ha-floorplan` remains installed but unused. If a future MVP needs its richer effects, this decision should be revisited and superseded rather than silently reversed.

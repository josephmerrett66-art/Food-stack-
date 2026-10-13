# Food Van Shift

A one-screen companion app for **Food Van**, a two-player co-op memory and dexterity game played with the wooden food pieces and tweezers from Barbecubes.

## How a shift works

1. Pick a scenario (or a Random shift). The six foods are split randomly between Joe and Beth once, and each player keeps their three foods for the whole run.
2. Tap **Peek** to see the order: an isometric stack on the plate, numbered from the bottom up, with each piece shown **Flat** or **On long edge**.
3. When the peek runs out the order hides. No talking about the order. Build it with tweezers, piece 1 on the plate first.
4. Tap **Reveal order**, then tap any piece you got wrong.
5. Each wrong piece takes one second off the next peek. If the peek hits zero, you lose. Survive all six orders to clear the scenario and unlock the next.

## Scenarios

| Scenario | Stack heights | Starting peek |
|---|---|---|
| Lunch Rush | 5–7 | 5s |
| Market Day | 5–7 | 4s |
| Festival Friday | 6–8 | 4s |
| Late Night Queue | 6–8 | 3s |
| Nightmare Shift | 7–8 | 3s |
| Random shift | 5–8, random each order | 5s |

## Files

- `index.html` – the built app. Open it in any browser; it has no other dependencies.
- `src/app.html` – the app source, with a `/*SPRITES*/` placeholder for the piece art.
- `pieces/` – the 12 piece images (each food, flat and on long edge), cut from the cheat-sheet mockup.
- `build.py` – embeds the piece images into `src/app.html` to produce `index.html` (needs Pillow).

Scenario unlocks are saved in the browser's local storage on the device you play on.

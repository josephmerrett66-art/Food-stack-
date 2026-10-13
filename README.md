# Food Van Shift

A one-screen companion app for **Food Van**, a two-player co-op memory and dexterity game played with the wooden food pieces and tweezers from Barbecubes.

## How a shift works

1. Pick a mode. The six foods are split randomly between Joe and Beth once, and each player keeps their three foods for the whole run.
2. Tap **Peek** to see the order: an isometric stack on the plate, numbered from the bottom up, with each piece shown **Flat** or **On long edge**.
3. When the peek runs out the order hides. No talking about the order. Build it with tweezers, piece 1 on the plate first.
4. Tap **Reveal order**, then tap any piece you got wrong.
5. Every mode starts with a **6-second peek**. Each wrong piece takes one second off it for the rest of the run. If the peek hits zero, you lose. Survive all six orders to clear the mode.

## Modes

**The ladder** gets harder only by stack height. Clearing one unlocks the next.

| Mode | Stack heights |
|---|---|
| Lunch Rush | 4–5 |
| Market Day | 5–6 |
| Festival Friday | 5–7 |
| Late Night Queue | 6–8 |
| Nightmare Shift | 7–8 |

**Twists** are open from the start and sit at a similar difficulty, changing the shape of the orders instead.

| Mode | Stack heights | Twist |
|---|---|---|
| Flat Out | 5–7 | Every piece lies flat |
| Stand Tall | 5–7 | Every piece on its long edge |
| Ping Pong | 5–6 | Joe and Beth take strict turns |
| Doubles | 6 | Three foods, each one twice |

**Random shift** rolls a stack height from 4 to 8 for every order.

## Files

- `index.html` – the built app. Open it in any browser; it has no other dependencies.
- `src/app.html` – the app source, with a `/*SPRITES*/` placeholder for the piece art.
- `pieces/` – the 12 piece images (each food, flat and on long edge), cut from the cheat-sheet mockup.
- `build.py` – embeds the piece images into `src/app.html` to produce `index.html` (needs Pillow).

Scenario unlocks are saved in the browser's local storage on the device you play on.

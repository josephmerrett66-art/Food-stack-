# Food Van Shift

A one-screen companion app for **Food Van**, a two-player co-op memory and dexterity game played with the wooden food pieces and tweezers from Barbecubes.

## How a shift works

1. Pick a difficulty and a scenario (or a Random shift). The six foods are split randomly between Joe and Beth once, and each player keeps their three foods for the whole run.
2. Tap **Peek** to see the order: an isometric stack on the plate, numbered from the bottom up, with every piece lying flat.
3. When the peek runs out the order hides. No talking about the order. Build it with tweezers, piece 1 on the plate first, before the **build timer** runs out: 5 seconds plus 5 seconds per piece (30s for a 5-high order, 55s for 10-high).
4. Tap **Done · reveal order** when you've finished, or the order reveals itself when the timer hits zero (any piece you didn't place counts as wrong). Then tap any piece you got wrong.
5. Every mode starts with a **6-second peek**. Each wrong piece takes one second off it for the rest of the run. If the peek hits zero, you lose. Survive all six orders to clear the scenario.

## Difficulties and scenarios

Like Sky Team, you pick a difficulty and then one of six scenarios inside it. Every scenario starts with the same 6-second peek; difficulty comes only from stack height. Every order is split evenly between Joe and Beth (one extra for someone when the height is odd), in a shuffled order. A scenario keeps the same heights and the same who-goes-when every time you replay it; the actual foods follow that run's random split. All scenarios are open from the start.

Every scenario **ramps up**: the first order is short enough to feel easy, and the stacks climb gently, by one or two pieces, to the final order. The difficulty sets where the ramp starts and ends, and each of the six scenarios climbs its own way (steady, in steps, a plateau, a mid-shift spike, in pairs, or a late surge). The shrinking peek stacks on top: slip early and you face the tallest orders with the least time.

| Difficulty | Order 1 → Order 6 | Scenarios |
|---|---|---|
| Easy | 5 → 6 | Morning Coffee, School Pickup, Farmers Market, Beach Car Park, Sausage Sizzle, Sunday Brunch |
| Medium | 6 → 7 | Lunch Rush, Office Park, Rainy Day, Uni Open Day, Car Show, Twilight Cinema |
| Hard | 6 → 8 | Festival Friday, Night Market, Wedding Reception, Stadium Gates, Long Weekend, Heatwave |
| Expert | 7 → 9 | Late Night Queue, Grand Final Day, New Year's Eve, Music Festival, Food Truck Rally, Closing Time |
| Nightmare | 8 → 10 | Nightmare Shift, Health Inspection, Power Outage, Royal Visit, Double Booking, The Last Sausage |

**Random shift** rolls six random heights from 5 to 8 and plays them shortest first, with new orders every time.

## Files

- `index.html` – the built app, a full phone-ready page (served by GitHub Pages). On iPhone, use Share → Add to Home Screen to play it full screen without the Safari bars.
- `src/app.html` – the app source, with a `/*SPRITES*/` placeholder for the piece art.
- `pieces/` – the 12 piece images (each food, flat and on long edge), cut from the cheat-sheet mockup.
- `build.py` – embeds the piece images into `src/app.html` to produce `index.html`, plus `dist/artifact.html` for the Claude app (needs Pillow).

Cleared scenarios are saved in the browser's local storage on the device you play on.

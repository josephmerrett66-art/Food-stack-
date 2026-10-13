# Food Van Shift

A one-screen companion app for **Food Van**, a two-player co-op memory and dexterity game played with the wooden food pieces and tweezers from Barbecubes.

## How a shift works

1. Pick a difficulty and a scenario (or a Random shift). The six foods are split randomly between Joe and Beth once, and each player keeps their three foods for the whole run.
2. Tap **Peek** to see the order: an isometric stack on the plate, numbered from the bottom up, with each piece shown **Flat** or **On long edge**.
3. When the peek runs out the order hides. No talking about the order. Build it with tweezers, piece 1 on the plate first.
4. Tap **Reveal order**, then tap any piece you got wrong.
5. Every mode starts with a **6-second peek**. Each wrong piece takes one second off it for the rest of the run. If the peek hits zero, you lose. Survive all six orders to clear the scenario.

## Difficulties and scenarios

Like Sky Team, you pick a difficulty and then one of six scenarios inside it. Every scenario starts with the same 6-second peek; difficulty comes only from stack height. Each scenario always deals the same six orders, so you can replay it and learn it. All scenarios are open from the start.

| Difficulty | Stack heights | Scenarios |
|---|---|---|
| Easy | 4–5 | Morning Coffee, School Pickup, Farmers Market, Beach Car Park, Sausage Sizzle, Sunday Brunch |
| Medium | 5–6 | Lunch Rush, Office Park, Rainy Day, Uni Open Day, Car Show, Twilight Cinema |
| Hard | 5–7 | Festival Friday, Night Market, Wedding Reception, Stadium Gates, Long Weekend, Heatwave |
| Expert | 6–8 | Late Night Queue, Grand Final Day, New Year's Eve, Music Festival, Food Truck Rally, Closing Time |
| Nightmare | 7–8 | Nightmare Shift, Health Inspection, Power Outage, Royal Visit, Double Booking, The Last Sausage |

**Random shift** rolls a fresh stack height from 4 to 8 for every order, and new orders every time.

## Files

- `index.html` – the built app, a full phone-ready page (served by GitHub Pages). On iPhone, use Share → Add to Home Screen to play it full screen without the Safari bars.
- `src/app.html` – the app source, with a `/*SPRITES*/` placeholder for the piece art.
- `pieces/` – the 12 piece images (each food, flat and on long edge), cut from the cheat-sheet mockup.
- `build.py` – embeds the piece images into `src/app.html` to produce `index.html`, plus `dist/artifact.html` for the Claude app (needs Pillow).

Cleared scenarios are saved in the browser's local storage on the device you play on.

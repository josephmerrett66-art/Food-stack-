"""Build index.html from src/app.html by embedding the piece art in pieces/.

Usage: python3 build.py
"""
import base64, io, json, pathlib

ROOT = pathlib.Path(__file__).parent
FOODS = ["patty", "steak", "hotdog", "bacon", "fish", "drumstick"]

def main():
    from PIL import Image  # pip install pillow
    art = {}
    for food in FOODS:
        art[food] = {}
        for pose in ("flat", "edge"):
            im = Image.open(ROOT / "pieces" / f"{food}_{pose}.png")
            buf = io.BytesIO()
            im.save(buf, "PNG", optimize=True)
            uri = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
            art[food][pose] = [uri, im.size[0], im.size[1]]
    page = (ROOT / "src" / "app.html").read_text().replace("/*SPRITES*/", json.dumps(art))
    # bare version (the Claude artifact viewer wraps it in its own <html>/<head>)
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist" / "artifact.html").write_text(page)
    # full standalone page for GitHub Pages / Safari: needs the phone viewport meta
    split = page.index('<div class="app">')
    head, body = page[:split], page[split:]
    (ROOT / "index.html").write_text(
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n'
        '<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n'
        '<meta name="apple-mobile-web-app-title" content="Food Van">\n'
        '<meta name="theme-color" content="#1d2532">\n'
        + head + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')
    print("Built index.html and dist/artifact.html")

if __name__ == "__main__":
    main()

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
    src = (ROOT / "src" / "app.html").read_text()
    (ROOT / "index.html").write_text(src.replace("/*SPRITES*/", json.dumps(art)))
    print("Built index.html")

if __name__ == "__main__":
    main()

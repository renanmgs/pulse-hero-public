"""Resize game art into web-sized assets for the landing page.

Sources straight from the game repo, so this does not depend on a press kit
folder being checked out next to the site.
"""
from pathlib import Path
import shutil
from PIL import Image

GAME_IMAGES = Path("D:/GitRepos/fit_hero/app/assets/images")
ART = Path(__file__).resolve().parent.parent / "assets/art"

CLASSES = [
    "novice", "swordsman", "apprentice", "scout", "cleric", "duelist",
    "blademaster", "guardian", "paladin", "priest", "pyromancer",
    "arcanist", "trickster",
]
PROFESSIONS = [
    "miner", "botanist", "hunter", "armorsmith", "weaponsmith",
    "leatherworker", "tailor", "alchemist", "runecrafter",
]
# Picked to read well as silhouettes and to cover the whole library:
# barbell work, bodyweight, cardio, mobility and sport.
EXERCISES = [
    "squat", "pushup", "pullup", "bench_press", "romanian_deadlift",
    "overhead_press", "lunge", "plank", "dips", "jump_rope", "free_run",
    "long_run", "swim", "indoor_cycle", "rowing", "hike", "brisk_walk",
    "yoga_flow", "mobility_flow", "dance", "basketball", "soccer",
    "tennis", "climb",
]


def fit(src: Path, dst: Path, box: int, quality: int = 82, trim: bool = False):
    """Shrink to fit inside `box` on the long edge, keeping alpha.

    With `trim`, the transparent margin is cropped off and the art is recentred
    in a square. The source icons carry different amounts of padding, so
    without this they render at visibly different optical sizes in a grid.
    """
    dst.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(src).convert("RGBA")
    if trim:
        bbox = im.getchannel("A").getbbox()
        if bbox:
            im = im.crop(bbox)
        side = int(max(im.size) * 1.08)
        square = Image.new("RGBA", (side, side), (0, 0, 0, 0))
        square.paste(im, ((side - im.width) // 2, (side - im.height) // 2), im)
        im = square
    im.thumbnail((box, box), Image.LANCZOS)
    im.save(dst, "WEBP", quality=quality, method=6)
    return dst.stat().st_size


shutil.rmtree(ART, ignore_errors=True)
totals = {}

for name in CLASSES:
    totals.setdefault("crests", 0)
    totals["crests"] += fit(
        GAME_IMAGES / "class_crests_generated" / f"class_{name}.webp",
        ART / "crests" / f"{name}.webp", 240, trim=True)

for name in PROFESSIONS:
    totals.setdefault("professions", 0)
    totals["professions"] += fit(
        GAME_IMAGES / "profession_icons" / f"p_{name}.webp",
        ART / "professions" / f"{name}.webp", 200, trim=True)

for name in EXERCISES:
    totals.setdefault("exercises", 0)
    totals["exercises"] += fit(
        GAME_IMAGES / "exercises_generated" / f"ex_{name}.webp",
        ART / "exercises" / f"{name.replace('_', '-')}.webp", 300)

for k, v in totals.items():
    n = len(list((ART / k).glob("*.webp")))
    print(f"{k:12} {n:3} files  {v / 1024:6.0f} KB")
print(f"TOTAL {sum(totals.values()) / 1024:.0f} KB")

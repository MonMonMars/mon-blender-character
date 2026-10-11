#!/usr/bin/env python3
"""
Documentation-only example: batch render stills from a Blender file.

Mon's live script: D:\\Blender\\projects\\mon-character\\batch_preview.py
Run with:
  D:\\Blender\\5.2.0\\blender.exe --background --python batch_preview.example.py

Requires bpy (only available inside Blender's Python). Do not commit reference VRM/GLB.
"""

from __future__ import annotations

import os
from pathlib import Path

import bpy  # Run only inside Blender's Python (see scripts/README.md)

# --- Configure on D: (edit on PC; env vars optional) ---
BLEND_FILE = Path(
    os.environ.get(
        "MON_BLEND_FILE",
        r"D:\Blender\projects\mon-character\mon-character.blend",
    )
)
OUTPUT_DIR = Path(
    os.environ.get(
        "MON_PREVIEW_DIR",
        r"D:\Blender\projects\mon-character\previews",
    )
)
FRAME_START = int(os.environ.get("MON_FRAME_START", "1"))
FRAME_END = int(os.environ.get("MON_FRAME_END", "1"))
RESOLUTION_X = int(os.environ.get("MON_RES_X", "512"))
RESOLUTION_Y = int(os.environ.get("MON_RES_Y", "512"))


def main() -> None:
    if not BLEND_FILE.is_file():
        raise FileNotFoundError(f"Blend file not found: {BLEND_FILE}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    bpy.ops.wm.open_mainfile(filepath=str(BLEND_FILE))

    scene = bpy.context.scene
    scene.render.image_settings.file_format = "PNG"
    scene.render.resolution_x = RESOLUTION_X
    scene.render.resolution_y = RESOLUTION_Y
    scene.render.resolution_percentage = 100

    for frame in range(FRAME_START, FRAME_END + 1):
        scene.frame_set(frame)
        out_name = OUTPUT_DIR / f"preview_{frame:04d}.png"
        scene.render.filepath = str(out_name)
        bpy.ops.render.render(write_still=True)
        print(f"Wrote {out_name}")


if __name__ == "__main__":
    main()

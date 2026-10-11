# Scripts

This folder documents helper automation for Mon’s character project. Scripts here are **optional**; the authoritative preview batch script on Mon’s PC lives outside git.

## batch_preview.py (on PC)

**Location:** `D:\Blender\projects\mon-character\batch_preview.py`

Used to render thumbnail previews (e.g. the 68 images in `D:\Blender\projects\mon-character\previews\`) from local reference scenes. That script targets Mon’s machine layout and Blender 5.2 install.

- Run with Blender’s bundled Python, typically:

  `"D:\Blender\5.2.0\blender.exe" --background --python D:\Blender\projects\mon-character\batch_preview.py`

- Adjust paths inside the PC script if project root moves — always stay on **`D:`**.

**Do not** commit third-party `.vrm` / `.glb` sources into this repo when batching previews. Previews are reference-only; see root [README.md](../README.md).

## batch_preview.example.py (in repo)

[batch_preview.example.py](batch_preview.example.py) is a **cleaned, documentation-only** example showing how a batch render loop might:

1. Accept `BLEND_FILE`, `OUTPUT_DIR`, and camera/render settings via environment variables or constants at the top.
2. Open a `.blend` in background mode, set frame/output paths, and write PNGs.

Copy ideas from the example into the PC script; the example is not wired to amoji assets or copyrighted meshes.

## Adding new scripts here

Small, MIT-friendly utilities (path checkers, naming validators) may be committed. Keep them free of secrets, absolute `C:` paths, or embedded binary data.

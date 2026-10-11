# mon-blender-character

Original Blender character for **Mon** — human body, hat, armature, and facial expressions. Everything in the final `.blend` is designed and modeled from scratch in Blender.

## Project goal

Build a production-ready character rig at:

`D:\Blender\projects\mon-character\mon-character.blend`

The character includes:

- Human base mesh (original topology)
- Hat (separate object, rigged or parented as needed)
- Armature with sensible deformation
- Facial expression shape keys or bone-driven face setup

This repository holds **documentation, workflow notes, and small helper scripts only**. It does **not** store the main `.blend` file, exported game meshes, or third-party reference assets.

## Reference-only policy

Reference previews under `D:\Blender\projects\mon-character\previews\` (68 images rendered from **MonMonMars/amoji_engine_02** assets on Mon’s PC) are for **visual inspiration and proportion checks only**.

- Do **not** commit VRM, GLB, FBX, or other reference model binaries to this repo.
- Do **not** copy reference meshes, textures, or rig data into `mon-character.blend`.
- Final art and topology must be **original work** created in Blender.

## Local paths (Windows)

| Item | Path |
|------|------|
| Project root | `D:\Blender\projects\mon-character\` |
| Main blend file | `D:\Blender\projects\mon-character\mon-character.blend` |
| Reference previews | `D:\Blender\projects\mon-character\previews\` |
| Blender 5.2 | `D:\Blender\5.2.0\blender.exe` |
| Optional preview script (PC) | `D:\Blender\projects\mon-character\batch_preview.py` |

All project data lives on **`D:`** — avoid storing working files on `C:`. See [docs/PATHS.md](docs/PATHS.md) for the full list.

## MCP (Blender automation)

When using Cursor or other MCP clients with Blender:

- Add-on script: `D:\Blender\mcp\addon.py`
- Default MCP port: **9876**

Install/enable the add-on in Blender, start the MCP server from the add-on UI, then connect your client to `localhost:9876`. Details may vary by add-on version; treat paths above as the canonical locations on Mon’s machine.

## Repository contents

| Path | Purpose |
|------|---------|
| [docs/WORKFLOW.md](docs/WORKFLOW.md) | Pick refs → build character → export |
| [docs/PATHS.md](docs/PATHS.md) | D: drive path reference |
| [scripts/README.md](scripts/README.md) | Preview batch script notes |
| [scripts/batch_preview.example.py](scripts/batch_preview.example.py) | Documentation-only example (not required on PC) |

## Quick start

1. Open `D:\Blender\5.2.0\blender.exe` and load or create `mon-character.blend`.
2. Browse `previews\` and note poses, proportions, and style targets (reference only).
3. Follow [docs/WORKFLOW.md](docs/WORKFLOW.md) for modeling, rigging, and export.
4. Commit only docs/scripts from this git repo; keep binaries on `D:`.

## License / assets

Reference previews trace to external amoji_engine assets used **locally and privately** for reference. This repo intentionally excludes those binaries. The shipped character should be Mon’s original creation.

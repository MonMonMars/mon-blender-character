# Path reference (D: drive only)

Mon’s Blender character work is rooted on **`D:`**. Do not use `C:` for project saves, exports, caches, or reference binaries — keeps backups and git clean and avoids permission clutter on the system drive.

## Canonical paths

| Description | Path |
|-------------|------|
| Blender 5.2 executable | `D:\Blender\5.2.0\blender.exe` |
| Blender MCP add-on | `D:\Blender\mcp\addon.py` |
| MCP server port (default) | `9876` (localhost) |
| Character project root | `D:\Blender\projects\mon-character\` |
| Main blend file | `D:\Blender\projects\mon-character\mon-character.blend` |
| Reference preview images (68) | `D:\Blender\projects\mon-character\previews\` |
| Batch preview script (PC) | `D:\Blender\projects\mon-character\batch_preview.py` |

## Recommended (create on D: as needed)

These folders are not in git; create them locally when useful:

| Description | Suggested path |
|-------------|----------------|
| Export output | `D:\Blender\projects\mon-character\export\` |
| Render turntables / WIP | `D:\Blender\projects\mon-character\renders\` |
| Textures (original) | `D:\Blender\projects\mon-character\textures\` |
| Backup blends (optional) | `D:\Blender\projects\mon-character\backups\` |
| Local ref notes | `D:\Blender\projects\mon-character\notes\` |

## Git repository vs. disk

| Location | What lives there |
|----------|------------------|
| This git clone (any drive letter) | README, docs, small scripts |
| `D:\Blender\projects\mon-character\` | Working `.blend`, previews, exports, MCP-local tools |

Cloning the repo to `D:\Blender\projects\mon-character\repo\` (or similar) is fine; still keep `mon-character.blend` at the path above unless you deliberately relocate and update this doc.

## Reference asset source (local only, never commit)

Reference model packs used to **render** preview images may live outside this tree (e.g. amoji_engine_02 content on Mon’s PC). Those binaries must **not** be copied into this public repository. Only the PNG/JPEG previews under `previews\` are used on disk for look-dev — and preview images themselves are optional to commit; default is keep them local.

## Quick copy-paste block

```
D:\Blender\5.2.0\blender.exe
D:\Blender\mcp\addon.py
D:\Blender\projects\mon-character\mon-character.blend
D:\Blender\projects\mon-character\previews\
D:\Blender\projects\mon-character\batch_preview.py
```

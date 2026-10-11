# Character workflow

End-to-end flow for Mon’s original Blender character. Reference images inform design; they do not become source geometry.

## 1. Pick references from previews

1. Open `D:\Blender\projects\mon-character\previews\` in an image viewer or file browser.
2. Sort or tag favorites (outside git is fine — e.g. a local `refs-picks.txt` on `D:`).
3. For each pick, write **one line of intent**, not “copy this mesh”:
   - Silhouette (e.g. round hat, short limbs)
   - Expression range (smile, angry, surprised)
   - Color mood (keep palette notes separate from reference textures)
4. Do **not** import VRM/GLB from amoji_engine or other packs into the working blend.

## 2. Build the original character

Work in `D:\Blender\projects\mon-character\mon-character.blend` using Blender **5.2** (`D:\Blender\5.2.0\blender.exe`).

### Blockout

- Human-scale blockout (head, torso, limbs) with clean edge flow planned early.
- Hat as its own object; decide attach method (parent to head bone vs. separate rig chunk).

### Modeling

- Subdivision-friendly quads; avoid stolen topology from reference files.
- UVs laid out for hand-painted or procedural textures you create.
- Naming convention example: `MON_Body`, `MON_Hat`, `MON_Eyes`.

### Armature

- Meta-rig or manual bones: spine, limbs, neck, head, jaw (if needed).
- Weight painting pass; test extreme poses.
- Hat: either weighted to head/deformation bones or rigid parent to `Head`.

### Face / expressions

Choose one primary approach (or hybrid):

- **Shape keys** for phoneme-style or emoji-like expressions, or
- **Bone-driven** brows, cheeks, jaw with drivers.

Create a small test set: Neutral, Happy, Sad, Angry, Surprised. Save incrementally (`File → Save`, avoid relying on `.blend1` backups in git).

### Materials & look dev

- Simple viewport + one render engine setup (EEVEE or Cycles) for consistent turntables.
- No pasted albedo maps from reference packs.

### Validation

- Apply transforms before export tests.
- Check scale (1 Blender unit = 1 meter unless your target engine specifies otherwise).
- Pose library or action strips for expression previews.

## 3. Export

Export paths stay on **`D:`**, e.g. `D:\Blender\projects\mon-character\export\`.

Typical targets (choose what your pipeline needs):

| Format | Use case |
|--------|----------|
| FBX | Game engines, general DCC |
| glTF/GLB | Web/real-time (export **from your original blend**, not committed reference GLBs) |
| USD | Pipelines that prefer USD |

Checklist before export:

- [ ] Applied scale / rotation where required by exporter
- [ ] Armature is rest pose or defined export pose documented in a README on `D:`
- [ ] Shape keys or actions named consistently
- [ ] No accidental linked data from external copyrighted files

After export, smoke-test in the target app. Keep exported binaries **local on D:** unless a separate release repo policy applies.

## Optional: MCP-assisted steps

With `D:\Blender\mcp\addon.py` running on port **9876**, you can automate repetitive tasks (naming, batch renders, scene queries) from Cursor. MCP does not replace the reference-only rule — it is a convenience layer on top of the same blend file.

## Regenerating preview thumbnails

The live batch script on Mon’s PC:

`D:\Blender\projects\mon-character\batch_preview.py`

See [scripts/README.md](../scripts/README.md) and [scripts/batch_preview.example.py](../scripts/batch_preview.example.py) for a documented pattern. Regenerated previews stay in `previews\` and remain reference-only; do not commit third-party model sources.

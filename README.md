# duckcraft v1.0.0
duckcraft is a 3d raycaster game, soon it wil have placing and breaking logic

# controls
w a s d move  a/b look around

#stuff

you can open this project from: 
[duckcraft 1.0.0](https://omidomidvari.github.io/duckcraft-v1.0.0-underdev/ "duckcraft")

==================================================================================================================================

# Mod Authoring Guide (for Duckcraft)

This short guide shows how to make a mod package that Duckcraft accepts. Mods are distributed as .dcm files which contain a ZIP (or 7z) archive of your mod files. Keep mods data-only or follow the project's sandbox rules — unsafe code (eval, arbitrary network access, etc.) may be rejected.

## Required structure
Create a folder with this structure (minimum):
- manifest.json (required)
- mod/ (contains your mod code; entry file referenced in manifest)
- assets/ (images, sounds, optional)

Example:
```
my-mod/
├─ manifest.json
├─ mod/
│  └─ main.js
└─ assets/
   └─ sprite.png
```

## manifest.json (example)
```json
{
  "id": "duckcraft-duckvalley",
  "name": "Duck Valley",
  "version": "1.0.0",
  "author": "omod",
  "description": "A tiny example map mod",
  "type": "map",
  "entry": "mod/main.js",
  "game_version": "1.0.0",
  "permissions": [],
  "assets": [
    "assets/sprite.png"
  ],
  "license": "MIT"
}
```

Notes:
- `entry` is the path inside the archive to the main script that the runtime will load.
- `permissions` is an array of requested capabilities (e.g., `["render","spawn_entity"]`). The host will grant only approved permissions.
- Keep `id` unique (reverse-domain or slug style recommended).

## Example mod/main.js (minimal)
```javascript
// This file is executed inside the mod runtime (sandboxed). Use the host API provided in init().
export function init(hostApi) {
  hostApi.log('Duck Valley mod initialized');
  // Example: request the host to draw a sprite (host must implement drawSprite)
  // hostApi.drawSprite('duck', 100, 100);
}
```

API: The host provides a small, capability-limited API object (hostApi). Do not assume direct DOM or network access.

## Packaging into a .dcm
1. Create a ZIP of the mod folder (from inside the parent directory).

Linux / macOS:
```bash
zip -r duck-valley.zip manifest.json mod assets
mv duck-valley.zip duck-valley.dcm
```

Windows (PowerShell):
```powershell
Compress-Archive -Path .\manifest.json, .\mod\*, .\assets\* -DestinationPath .\duck-valley.zip
Rename-Item .\duck-valley.zip .\duck-valley.dcm
```

Using 7z (optional):
```bash
7z a duck-valley.7z manifest.json mod assets
mv duck-valley.7z duck-valley.dcm
```

2. Verify (optional)
Rename back to check contents:
```bash
mv duck-valley.dcm duck-valley.zip
unzip -l duck-valley.zip
```

## Allowed file types and limits (server-enforced — check server docs)
- Typical allowed extensions: .js, .json, .png, .jpg, .webp, .ogg, .mp3, .wasm (if allowed)
- Disallowed: executables (.exe, .dll), shell scripts, unknown binaries
- Size and file-count limits are enforced by the server; keep your mod compact (recommended < 50 MB).

## Security & best practices
- Avoid eval(), new Function(), or other dynamic-code constructs. These may trigger manual review or rejection.
- Do not include secrets or credentials.
- Use only the host API to interact with the game — do not access window.parent, cookies, or localStorage.
- Test mods locally in an isolated environment before packaging.
- Provide a clear description, version, and license in the manifest.

## Optional: Node helper (pack and rename)
If you prefer an automated script, the repository includes a small helper (create-dcm.js) to zip a folder and produce a .dcm file:
```bash
node create-dcm.js ./my-mod duck-valley
# produces duck-valley.dcm
```

## Upload & publish
- Upload your .dcm through the game's mod uploader (or web UI).
- After upload the mod will be scanned and validated. If it passes, it will be processed and become available for install.

If you want, include a link to a mod template repository and a local validator script to help authors check their package before upload.

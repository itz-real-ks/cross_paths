# <h1> cross_paths

**cross_paths** is a Python toolkit for **finding and safely isolating duplicate files** — especially in large media folders, project directories, and backup dumps.

Duplicates are detected using **content hashing**, and extra copies are **moved into `~/.cross_paths_trash`** instead of being deleted.  
You stay in control — no accidental data loss.

---

## Install

```bash
pip install cross_paths
```

## What it does

| Feature | Description |
| --- | --- |
| Detect Duplicates | Finds files with identical content |
| Safe Cleanup | Moves duplicates to `~/.cross_paths_trash` |
| Keeps Originals | Only the first matching file stays in place |
| Parallel Hashing | Speeds up hashing for large folders |
| Glob Patterns | e.g., `"**/*.jpg"`, `"**/*.mp4"` |
| CLI + Python | Usable in scripts or terminals |

## CLI — quick usage

```bash
# list duplicate groups (read-only)
cross_paths --duplicates "**/*.jpg"

# safely move duplicates to trash (not deleted)
cross_paths --rmdupes-safe "**/*.jpg"

# validate existence/readability of files
cross_paths file1.txt folder/photo.png
```

---

## Python usage

```python
from cross_paths import find_duplicates, delete_duplicates_trash

# see duplicates
print(find_duplicates("**/*.mp4"))

# move duplicates to trash
delete_duplicates_trash("**/*.mp4")
```

---

## Safety model

- no direct deletion  
- duplicates go to `~/.cross_paths_trash`
- you manually review/remove later
- symlinks are skipped for safety

---

## When it's useful

- cleaning messy photo/video folders
- organizing project assets
- deduping backup archives
- reducing storage without deleting blindly

## When it's not for you

- you need automatic destructive deletion
- you want cross-drive deduplication

---

## Notes

- wrap patterns in quotes to avoid shell expansion issues
- uses Python’s `hashlib` for hashing
- parallelization uses multiple CPU cores

---

## <a href="https://raw.githubusercontent.com/itz-real-ks/cross_paths/refs/heads/main/LICENSE">License</a>

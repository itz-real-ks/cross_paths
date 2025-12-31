<h1 style="color:#DB4437;">cross_paths</h1>

<p><strong style="color:#4285F4;">cross_paths</strong> is a Python toolkit for 
<strong style="color:#0F9D58;">finding and safely isolating duplicate files</strong> — especially in large media folders, 
project directories, and backup dumps.</p>

<p>Duplicates are detected using <strong>content hashing</strong>, and extra copies are 
<strong style="color:#F4B400;">moved</strong> into <code>~/.cross_paths_trash</code> instead of being deleted.  
You stay in control — no accidental data loss.</p>

<hr>

<h2><a href="https://cross-paths-docs.lovable.app" style="color:#0F9D58;">📚 Full Documentation & Usage Examples</a></h2>

<h2><a href="https://github.com/itz-real-ks/cross_paths/blob/main/installation.md" style="color:#4285F4;">⚙️ Install</a></h2>


<h2 style="color:#DB4437;">What it does</h2>

| Feature | Description |
| --- | --- |
| <span style="color:#4285F4;">Detect Duplicates</span> | Finds files with identical content |
| <span style="color:#0F9D58;">Safe Cleanup</span> | Moves duplicates to <code>~/.cross_paths_trash</code> |
| <span style="color:#DB4437;">Keeps Originals</span> | Only the first matching file stays in place |
| <span style="color:#EA4335;">Parallel Hashing</span> | Speeds up hashing for large folders |
| <span style="color:#F4B400;">Glob Patterns</span> | e.g., <code>"**/*.jpg"</code>, <code>"**/*.mp4"</code> |
| <span style="color:#AB47BC;">CLI + Python</span> | Usable in scripts or terminals |

---

<h2 style="color:#0F9D58;">CLI — quick usage</h2>

```bash
# list duplicate groups (read-only)
cross_paths --duplicates "**/*.jpg"

# safely move duplicates to trash (not deleted)
cross_paths --rmdupes-safe "**/*.jpg"

# validate existence/readability of files
cross_paths file1.txt folder/photo.png
````

---

<h2 style="color:#4285F4;">Python usage</h2>

```python
from cross_paths import find_duplicates, delete_duplicates_trash

# see duplicates
print(find_duplicates("**/*.mp4"))

# move duplicates to trash
delete_duplicates_trash("**/*.mp4")
```

---

<h2 style="color:#F4B400;">Safety model</h2>

* no direct deletion
* duplicates go to <code>~/.cross_paths_trash</code>
* you review & remove later
* symlinks skipped for safety

---

<h2 style="color:#DB4437;">When it's useful</h2>

* cleaning messy photo/video folders
* organizing project assets
* deduping backup archives
* reducing storage without deleting blindly

<h2 style="color:#EA4335;">When it's not for you</h2>

* you need automatic destructive deletion
* you want cross-drive deduplication

---

<h2 style="color:#AB47BC;">Notes</h2>

* wrap patterns in quotes to avoid shell expansion issues
* uses Python’s <code>hashlib</code> for hashing
* parallelization uses multiple CPU cores

---

<h2><a href="https://raw.githubusercontent.com/itz-real-ks/cross_paths/refs/heads/main/LICENSE" style="color:#DB4437;">📄 License</a></h2>


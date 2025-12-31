#!/usr/bin/env python3
"""
cross_paths: filesystem toolkit with safe duplicate removal support
"""
import os, sys, json, glob, mimetypes, hashlib, multiprocessing, shutil
from pathlib import Path
from datetime import datetime

def vfile(path_str, *, silent=False):
    p=Path(path_str)
    if not p.exists():
        if not silent: print("missing")
        return False
    if p.is_dir() or p.is_symlink() or not os.access(p, os.R_OK):
        if not silent: print("invalid")
        return False
    if not silent: print("ok")
    return True

def fext(p): return p.rsplit(".",1)[1] if "." in os.path.basename(p) else ""

def find_files(pattern): return glob.glob(pattern, recursive=True)

def tree_export(path):
    p=Path(path)
    if not p.exists(): return None
    def walk(d):
        node={"name":d.name,"children":[]}
        for e in sorted(d.iterdir(), key=lambda x:x.name.lower()):
            node["children"].append(walk(e) if e.is_dir() else {"name":e.name})
        return node
    return walk(p)

def guess_type(p):
    mime,_=mimetypes.guess_type(p)
    return {"mime":mime or "unknown","extension":fext(p)}

def stats(p):
    pp=Path(p)
    if not pp.exists(): return None
    st=pp.stat()
    return {"path":p,"size":st.st_size,"mtime":datetime.fromtimestamp(st.st_mtime).isoformat()}

def hash_file(p, algo="sha256"):
    if Path(p).is_symlink(): return None
    try: h=hashlib.new(algo)
    except: return None
    with open(p,"rb") as f:
        for c in iter(lambda:f.read(8192),b""): h.update(c)
    return h.hexdigest()

def _hash_task(args):
    p,algo=args
    return (p, hash_file(p,algo))

def bulk_hash_parallel(pattern, algo="sha256"):
    files=[f for f in find_files(pattern) if Path(f).is_file() and not Path(f).is_symlink()]
    with multiprocessing.Pool() as pool:
        results=pool.map(_hash_task, [(p,algo) for p in files])
    return {p:h for p,h in results if h}

def find_duplicates(pattern, algo="sha256"):
    hashes=bulk_hash_parallel(pattern,algo)
    rev={}
    for f,h in hashes.items():
        rev.setdefault(h,[]).append(f)
    return {k:v for k,v in rev.items() if len(v)>1}

def delete_duplicates_trash(pattern, algo="sha256"):
    dupes=find_duplicates(pattern,algo)
    trash_dir=Path.home()/".cross_paths_trash"
    trash_dir.mkdir(exist_ok=True)
    moved=[]
    for h,files in dupes.items():
        for f in files[1:]:
            src=Path(f)
            if src.exists():
                dst=trash_dir/src.name
                try:
                    shutil.move(str(src), str(dst))
                    moved.append(str(dst))
                except:
                    pass
    return {"moved":moved,"count":len(moved)}

def main():
    args=sys.argv[1:]
    if not args:
        print("usage")
        return
    if "--duplicates" in args:
        i=args.index("--duplicates"); pat=args[i+1]
        print(json.dumps(find_duplicates(pat), indent=2))
        return
    if "--rmdupes-safe" in args:
        i=args.index("--rmdupes-safe"); pat=args[i+1]
        print(json.dumps(delete_duplicates_trash(pat), indent=2))
        return
    # default: validation
    for t in args:
        vfile(t)

if __name__=="__main__":
    main()

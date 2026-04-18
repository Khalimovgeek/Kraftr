import os

def ensure_file(path):
    if not os.path.exists(path):
        open(path, "w").close()

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def append_to_file(path, content):
    with open(path, "a") as f:
        f.write("\n\n" + content)
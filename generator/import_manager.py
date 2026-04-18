def ensure_import(content, import_line):
    if import_line not in content:
        return import_line + "\n" + content
    return content
def ensure_import(content, import_line):
    if import_line not in content:
        return import_line + "\n" + content
    return content

def ensure_urlpatterns(content):
    if "urlpatterns" not in content:
        content += "\n\nurlpatterns = [\n]\n"
    return content

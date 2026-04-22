from generator.import_manager import ensure_import,ensure_urlpatterns
from generator.file_manager import ensure_file,read_file,write_file

import os

def add_url(function_name, app_path):
    file_path = os.path.join(app_path, "urls.py")

    # 1. Ensure file exists
    ensure_file(file_path)
    content = read_file(file_path)

    # 2. Avoid duplicate
    if f"views.{function_name})" in content:
        print("⚠ URL already exists")
        return

    # 3. Ensure imports
    content = ensure_import(content, "from django.urls import path")
    content = ensure_import(content, "from . import views")

    # 4. Ensure urlpatterns exists
    content = ensure_urlpatterns(content)

    # 5. Insert inside urlpatterns
    lines = content.splitlines()
    url_path = function_name.replace("_", "-")
    new_line = f'    path("{url_path}/", views.{function_name}, name="{url_path}"),'
    inserted = False
    for i, line in enumerate(lines):
        stripped = line.strip()

        # match both = and += cases
        if stripped.startswith("urlpatterns") and "[" in stripped:
            # find closing bracket
            for j in range(i + 1, len(lines)):
                if "]" in lines[j]:
                    lines.insert(j, new_line)
                    inserted = True
                    break
            break

    # fallback if nothing found
    if not inserted:
        lines.append("\nurlpatterns = [")
        lines.append(new_line)
        lines.append("]")

    # 6. Write back
    write_file(file_path, "\n".join(lines))

    print(f"✔ URL '/{function_name}/' added")
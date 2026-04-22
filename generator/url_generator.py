from generator.import_manager import ensure_import
from generator.file_manager import ensure_file,read_file

def add_url(function_name, app_path):
    file_path = f"{app_path}/urls.py"

    ensure_file(file_path)
    content = read_file(file_path)

    if f"views.{function_name}" in content:
        print("⚠ URL already exists")
        return

    # ensure imports
    content = ensure_import(content, "from django.urls import path")
    content = ensure_import(content, "from . import views")

    # ensure urlpatterns
    if "urlpatterns" not in content:
        content += "\n\nurlpatterns = []\n"

    # inject new path
    new_line = f'    path("{function_name}/", views.{function_name}),\n'

    content = content.replace(
        "urlpatterns = [",
        "urlpatterns = [\n" + new_line
    )

    with open(file_path, "w") as f:
        f.write(content)

    print(f"✔ URL added for {function_name}")
from generator.template_engine import render
from generator.file_manager import ensure_file, read_file, append_to_file
from generator.import_manager import ensure_import

def create_api(function_name, method, app_path):
    file_path = f"{app_path}/views.py"

    ensure_file(file_path)
    content = read_file(file_path)

    # if duplicate
    if f"def {function_name}(" in content:
        print("⚠ Function already exists")
        return

    # ensure import
    content = ensure_import(content, "from django.http import JsonResponse")

    # rewrite file with import fix
    with open(file_path, "w") as f:
        f.write(content)

    # generate function
    code = render(
        "django/api/view.py.j2",
        {
            "function_name": function_name,
            "method": method,
            "message": "success"
        }
    )

    append_to_file(file_path, code)

    print(f"✔ API '{function_name}' created in {file_path}")
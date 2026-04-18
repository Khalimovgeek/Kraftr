import sys
from generator.api_generator import create_api

def main():
    args = sys.argv

    if args[1] == "api":
        method = args[2]
        name = args[3]
        app = args[4]

        create_api(
            function_name=name,
            method=method,
            app_path=app
        )

if __name__ == "__main__":
    main()
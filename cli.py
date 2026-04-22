import sys
from generator.api_generator import create_api
from generator.url_generator import add_url


def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: kraftr <task>")
        return

    command = args[1]

    if command == "api":
        if len(args) < 5:
            print("Usage: kraftr api <method> <name> <app>")
            return

        method = args[2]
        name = args[3]
        app = args[4]

        create_api(
            function_name=name,
            method=method,
            app_path=app
        )
        flags = args[5:]

        if "--url" in flags:
            add_url(name, app)

    elif command == "url":
        if len(args) < 4:
            print("Usage: kraftr url <name> <app>")
            return

        name = args[2]
        app = args[3]

        add_url(
            function_name=name,
            app_path=app
        )
    
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
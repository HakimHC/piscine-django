import sys
import os
import re
from settings import *

template = """
<!DOCTYPE html>
<html>
    <head>
        <title> My CV </title>
    </head>
    <body>
    </body>
</html>
"""

def usage():
    print(f"usage: {sys.argv[0]} <template>", file=sys.stderr)
    exit(1)

def get_imported_vars():
    """
    This function returns an array of the imported variables
    """

    res = dict()

    for i, j in globals().items():
        if not i.startswith("__") and type(j).__name__ != "function" and type(j).__name__ != "module":
            res[i] = j
    return res
            


def main():
    if len(sys.argv) != 2:
        usage()

    extension = os.path.splitext(sys.argv[1])[1]
    file_name = os.path.splitext(sys.argv[1])[0]
    invalid = [ "template", ".template" ] # lazy error handling
    if extension != ".template" or sys.argv[1] in invalid:
        print("fatal: file extension must be '.template'", file=sys.stderr)
        exit(1)

    imported = get_imported_vars()

    template = ""
    try:
        with open(sys.argv[1], "r") as f:
            content = f.read()
            for i in imported:
                content = content.replace(f"{{{i}}}", f"{imported[i]}")
            template = f"""
<!DOCTYPE html>
<html>
    <head>
        <title> My CV </title>
    </head>
    <body>
        {content}
    </body>
</html>
"""
            print(content)

    except Exception as e:
        print(e)

    with open(f"{file_name}.html", "w") as f:
        f.write(template)
    
if __name__ == "__main__":
    main()
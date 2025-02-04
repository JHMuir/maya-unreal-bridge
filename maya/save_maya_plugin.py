# This script simply automates saving the maya plug-in to the devKit directory, saving a lot of time when debugging or making changes

import shutil
from pathlib import Path

try:
    source = Path(r"plug-in\py2MayaUnrealBridge.py")
    destination = Path(r"C:\Users\jorda\devkitBase\plug-ins\plug-ins")

    if not source.exists():
        print(f"Error: Source file '{source}' does not exist")
        raise

    if source.suffix != ".py":
        print(f"Error: Source file '{source}' is not a Python file")
        raise

    destination.mkdir(parents=True, exist_ok=True)

    destination_file = destination / source.name

    shutil.copy2(source, destination_file)
    print(f"Successfully copied {source.name} to {destination}")

except PermissionError:
    print(f"Error: Permission denied when accessing {source} or {destination}")
    raise
except Exception as e:
    print(f"Error: An unexpected error occurred: {str(e)}")
    raise

# import maya.cmds as cmds
# cmds.loadPlugin("py2MayaUnrealBridge.py")
# cmds.MayaUnrealBridge()
# cmds.unloadPlugin("py2MayaUnrealBridge.py")

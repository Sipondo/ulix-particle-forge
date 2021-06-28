import subprocess
from pathlib import Path

with open(Path("game_location.txt"), "r") as infile:
    block_location = infile.read().strip()


def run_nodes(parent):
    window = parent.mdiArea.activeSubWindow()
    if window:
        title = window.windowTitle().replace(".json", "").replace("*", "")
        subprocess.Popen(f'python game.py --particle "{title}"', cwd=block_location)

from libqtile.hook import subscribe
from os import path
import subprocess


@subscribe.startup_once
def autostart():
    """Hook to run autostart script"""
    script = path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])

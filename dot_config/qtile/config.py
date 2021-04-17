import subprocess
from os import path

from libqtile.hook import subscribe

import grayskull as style

settings = {}

for setting in dir(style):
    if not setting.startswith("_"):
        settings[setting] = getattr(style, setting)

globals().update(settings)


@subscribe.startup_once
def autostart():
    """Hook to run autostart script"""
    script = path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.run([script])

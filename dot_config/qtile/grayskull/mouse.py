from libqtile.config import Drag, Click
from libqtile.lazy import lazy

from grayskull.constants import MOD_KEY


mouse = [
    Drag(
        [MOD_KEY],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD_KEY],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([MOD_KEY], "Button2", lazy.window.bring_to_front()),
]
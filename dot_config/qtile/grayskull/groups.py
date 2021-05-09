from libqtile.dgroups import simple_key_binder
from libqtile.config import Group

from grayskull.constants import MOD_KEY


groupings = [
    Group("www"),
    Group("chat"),
    Group("editor"),
    Group("term"),
    Group("etc"),
]

bindings = simple_key_binder(MOD_KEY, "uiop7")

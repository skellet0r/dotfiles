import grayskull.groups as _groups
import grayskull.keys as _keys
import grayskull.layouts as _layouts
import grayskull.mouse as _mouse
import grayskull.screens as _screens

from grayskull.hooks import autostart

groups = _groups.groupings
keys = _keys.key_bindings
layouts = _layouts.layouts
mouse = _mouse.mouse
screens = _screens.screens

widget_defaults = _screens.widget_defaults

auto_fullscreen = True
bring_front_click = False
cursor_warp = False
dgroups_app_rules = []
dgroups_key_binder = _groups.bindings
extension_defaults = _screens.extension_defaults
floating_layout = _layouts.floating_layout
focus_on_window_activation = "smart"
follow_mouse_focus = True
main = None
wmname = "LG3D"

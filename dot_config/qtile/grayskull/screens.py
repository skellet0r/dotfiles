from libqtile.config import Screen
from libqtile import widget
from libqtile.bar import Bar

import psutil

widget_defaults = dict(font="sans", fontsize=14, padding=5)
extension_defaults = widget_defaults.copy()


def virt_memory_usage():
    """Get current memory usage"""
    return "{:.1%}".format(psutil.virtual_memory().percent / 100)


widgets = [
    widget.GroupBox(),
    widget.Spacer(),
    # Right portion of bar
    widget.Systray(),
    widget.Sep(),
    # Clock widget
    widget.Clock(format="%I:%M %p", update_interval=1),
    widget.TextBox("⏰ ", padding=0),
    widget.Sep(),
    # CPU widget
    widget.CPU(format="{load_percent:.1f}% 💪"),
    widget.Sep(),
    # Virtual Memory widget
    widget.GenPollText(func=virt_memory_usage, update_interval=1),
    widget.TextBox("🧠 ", padding=0),
    widget.Sep(),
    # Volume widget
    widget.Volume(),
    widget.TextBox("📻 ", padding=0),
    widget.Sep(),
    # Backlight widget
    widget.Backlight(backlight_name="intel_backlight"),
    widget.TextBox("☀️ ", padding=0),
    widget.Sep(),
    # Wireless lan widget
    widget.Wlan(disconnected_message="☠️ ", format="📡", interface="wlan0"),
    widget.Sep(),
    # Battery Widget
    widget.Battery(
        charge_char="⚡",
        discharge_char="🔋",
        format="{percent:.0%}{char}",
        notify_below=0.25,
        update_interval=60,
        hide_threshold=0.99,
    ),
]
bar = Bar(widgets, 30, opacity=1)
screens = [Screen(top=bar)]

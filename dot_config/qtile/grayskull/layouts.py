from libqtile import layout
from libqtile.config import Match

kwargs = dict(
    border_focus="#00ff00",
    border_width=1,
    margin=8,
)

layouts = [
    layout.MonadTall(**kwargs),
    layout.MonadWide(**kwargs),
    layout.Max(),
]


rules = [
    # Run the utility `xprop` to see the wm class and name of an X client.
    {"wm_class": "confirm"},
    {"wm_class": "dialog"},
    {"wm_class": "download"},
    {"wm_class": "error"},
    {"wm_class": "file_progress"},
    {"wm_class": "notification"},
    {"wm_class": "splash"},
    {"wm_class": "toolbar"},
    {"wm_class": "confirmreset"},  # gitk
    {"wm_class": "makebranch"},  # gitk
    {"wm_class": "maketag"},  # gitk
    {"title": "branchdialog"},  # gitk
    {"title": "pinentry"},  # GPG key password entry
    {"wm_class": "ssh-askpass"},  # ssh-askpass
    {"wm_class": "nm-connection-editor"},
    {"wm_class": "nitrogen"},
    {"wm_class": "pinentry-gtk-2"},
    {"wm_class": "lxpolkit"},
    {"wm_class": "blueman-manager"},
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        *[Match(**rule) for rule in rules],
    ]
)

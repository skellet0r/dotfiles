import grayskull as style

settings = {}

for setting in dir(style):
    if not setting.startswith("_"):
        settings[setting] = getattr(style, setting)

globals().update(settings)

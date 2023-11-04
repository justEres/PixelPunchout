import yaml


def getSettings():
    with open("settings.yaml", "r") as file:
        settings = yaml.safe_load(file)
        return settings


def setDefaultSettings():
    settings = {
        "FPS": 60,
        "WINDOWHEIGHT": 720,
        "WINDOWWIDTH": 1080,
        "FONT": "sprites/Retro Gaming.ttf"
    }
    with open("settings.yaml", "w") as file:
        yaml.safe_dump(settings, file)

setDefaultSettings()
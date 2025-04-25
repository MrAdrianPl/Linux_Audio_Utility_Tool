# Linux Audio Utility Tool(LAUT)

## About LAUT
LAUT is a gui set of tools that will allow easy configuration of Pipewire and in future most likely also wireplumber.

current version alows cofniguration of pipewire and all subservers that are avivable under it

this program is in its early stages of development so please understand it may be buggy

## Instalation
For standard user it will be easiest to download Appimage that is privded in the releases(https://github.com/MrAdrianPl/Linux_Audio_Utility_Tool/releases/latest)

## dependencies for development
LAUT uses those 3 packages bellow and few other that are builtin python libraries

``pip install pipewire_python``

``pip install PyQt6``

``pip install requests``

## Run from source
if you installed above dependency then you can simply start program using run_laut.sh.

note that this program waits for few responses from pw-top so it may take few seconds to start it up.

## Visuals
and here's how program looks right now

configuration tab:
![pipewire configuration](redme_images/LAUT%20pipewire%20config.png)

devices tab:
![pipewire devices properties](redme_images/LAUT%20devices.png)

I'm trying to provide as much information in simple manner as possible so if anyone have a idea where i can improve on design to make it more user friendly then let me know

## Current version of the program allows:
- Checking current devices properties
- Configuration of all pipewire settings

## Roadmap of planed features

### Implemented

- v0.7 Implementation of basic configurations for pipewire-pulse
- v0.6 Implementation of basic configurations for pipewire-jack
- v0.8 Implementation of basic configurations for clients
- v0.9 Various ui/ux improvements
- v0.10 Appimage version

### Main features

- v0.11 Implementation of application overrides for pipewire 
- v0.12 Implementation of application overrides for pipewire-pulse
- v0.13 Implementation of overrides for clients

### later development

- v0.14 Implementation of basic wireplumber settings
- v0.15 Implementation of pw-top wraper
- v0.16 General setings
- v0.17 Implementation of configuration presets
- v0.18 Configuration for app
- v0.19 rework of Devices tab
- v0.20 Further beautification of app GUI, addition of themes
 

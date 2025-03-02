# Linux Audio Utility Tool(LAUT)

## About LAUT
LAUT is a gui set of tools that will allow easy configuration of Pipewire and in future most likely also wireplumber.

current version dose not have options for configuring Pipewire-pulse, Pipewire-jack, or ALSA client settings

this program is in its early stages of development so please understand it may be buggy

## dependencies
to run program you'll need to install pipewire_python package

``pip install pipewire_python``

or 

``pip3 install pipewire_python``

after reaching stable satisfactory version i plan to make an Appimage version which will come without any additional requirements 

## Install/Run
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
- Configuration of pipewire basic settings

## Roadmap of planed features

### Main features
- v0.7 Implementation of basic configurations for pipewire-pulse
- v0.6 Implementation of basic configurations for pipewire-jack
- v0.8 Implementation of basic configurations for clients
- v0.9 Various ui/ux improvements
- v0.10 Appimage version

### later development
- v0.11 Implementation of application overrides for pipewire 
- v0.12 Implementation of application overrides for pipewire-pulse
- v0.13 Implementation of overrides for clients
- v0.14 Implementation of basic wireplumber settings

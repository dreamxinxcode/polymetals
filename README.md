# Getting Started



## Installation

- `$ pip3 install yahoo_fin`
- `$ cp polymetals.py ~/.config/polybar/scripts/`
- `$ chmod +x ~/.config/polybar/scripts/polymetals.py`

### ~/.config/polybar/config

```
[module/polysmetals]
type = custom/script
exec = ~/.config/polybar/scripts/polymetals.py --gold --silver --platinum --palladium --copper
tail = true
label = %output%
```

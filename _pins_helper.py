#!/usr/bin/env python3
"""
_pins_helper.py - Carica i PINS da gui_conf.json
Supporta sia Waveshare (KEY_UP_PIN) che nomi brevi (UP)
"""
import os, json

def load_pins():
    # Mapping nomi lunghi RaspyJack -> nomi brevi payload
    _map = {
        "KEY_UP_PIN":    "UP",
        "KEY_DOWN_PIN":  "DOWN",
        "KEY_LEFT_PIN":  "LEFT",
        "KEY_RIGHT_PIN": "RIGHT",
        "KEY_PRESS_PIN": "OK",
        "KEY1_PIN":      "KEY1",
        "KEY2_PIN":      "KEY2",
        "KEY3_PIN":      "KEY3",
    }
    defaults = {
        "UP": 6, "DOWN": 19, "LEFT": 5, "RIGHT": 26,
        "OK": 13, "KEY1": 21, "KEY2": 20, "KEY3": 16,
    }
    for path in [
        "/root/Raspyjack/gui_conf.json",
        os.path.join(os.path.dirname(__file__), "../../gui_conf.json"),
    ]:
        try:
            with open(path) as f:
                data = json.load(f)
            pins = data.get("PINS", {})
            result = {v: pins[k] for k, v in _map.items() if k in pins}
            if result:
                return result
        except Exception:
            pass
    return defaults
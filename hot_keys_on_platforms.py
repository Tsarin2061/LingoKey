import platform

hot_keys_on_platforms = {
    "Windows": {
        "translate": "ctrl+shift+t",
        "copy": "ctrl+c",
        "paste": "ctrl+v",
    },
    "Darwin": {
        "translate": "cmd+shift+t",
        "copy": "cmd+c",
        "paste": "cmd+v",
    }
}

hot_keys_on_platform = hot_keys_on_platforms.get(platform.system())
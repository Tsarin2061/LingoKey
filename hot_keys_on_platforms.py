import platform

hot_keys_on_platforms = {
    "Windows": {
        "translate": "ctrl+t",
        "copy": "ctrl+с",
        "paste": "ctrl+v",
    },
    "Darwin": {
        "translate": "cmd+j",
        "copy": "cmd+c",
        "paste": "cmd+v",
    },
}

hot_keys_on_platform = hot_keys_on_platforms.get(platform.system())

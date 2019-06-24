def toLowerCase(self, str: str) -> str:
    # Somehow this is faster than str.lower() but use same amount of memory.
    result = {
        "A":"a",
        "B":"b",
        "C":"c",
        "D":"d",
        "E":"e",
        "F":"f",
        "G":"g",
        "H":"h",
        "I":"i",
        "J":"j",
        "K":"k",
        "L":"l",
        "M":"m",
        "N":"n",
        "O":"o",
        "P":"p",
        "Q":"q",
        "R":"r",
        "S":"s",
        "T":"t",
        "U":"u",
        "V":"v",
        "W":"w",
        "X":"x",
        "Y":"y",
        "Z":"z"
    }
    k = ""
    for s in str:
        k += result.get(s, s)
    return k
import io


def readLRCC(text: str):
    result = {}
    for lines in text.split("\n"):
        if lines.startswith("#"):  # Comment line
            pass
        else:
            char = lines.split("\t")[0]
            first = lines.split("\t")[1]
            second = lines.split("\t")[2]
            locale = lines.split("\t")[3][2:]
            try:
                result[char][locale] = first + second
            except:
                result[char] = {}
                result[char][locale] = first + second
    return result


def getComponents(filelist: list[str]):
    result = {}
    for filename in [filename.replace(".png", "") for filename in filelist]:
        result[filename[0]] = {"Left": False, "Right": False, "Full": False}
        if filename.endswith(" (Left)"):
            result[filename[0]]["Left"] = True
        elif filename.endswith(" (Right)"):
            result[filename[0]]["Right"] = True
        else:
            result[filename[0]]["Full"] = True
    return result

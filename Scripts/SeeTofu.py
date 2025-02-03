def main():
    charsetFilename = "../Data/Charsets/Extremely Common Used Characters.txt"
    charset = ["u"+i
               for i in open(charsetFilename, encoding="utf-8").read().split("\n")]

    import os
    filenames = os.listdir("../Output/Glyphs")
    for filename in filenames:
        codepoint = filename.replace(".", " ").split(" ")[0]
        if codepoint in charset:
            charset.remove(codepoint)

    result = [chr(int(i[1:], base=16)) for i in charset]
    print("".join(result))


if __name__ == "__main__":
    main()

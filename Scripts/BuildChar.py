import logging
import LibHexin
import rich
import rich.logging
from PIL import Image, ImageDraw, ImageFont
import os
import time


def main():
    FORMAT = "%(message)s"
    logging.basicConfig(
        level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[rich.logging.RichHandler()]
    )

    log = logging.getLogger("rich")

    log.info("Reading LR Combined Chars data...")

    with open("../Data/LR Combined Chars.txt", encoding="utf-8") as f:
        text = f.read()
        log.debug("Processing data...")
        result = LibHexin.readLRCC(text)

    log.info("Generating component index...")
    componentIndex = LibHexin.getComponents(list(filter(lambda a: a.endswith(".png"),
                                                        os.listdir("../Data/Components"))))

    log.info("Processing chars...")
    for char in result:
        log.debug(f"Processing {char}...")

        def _generateImage(charData: str):
            image = Image.new("RGBA", (12, 8))
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype(
                "../Data/Fonts/Fallback Components.ttf", 8)
            ascent, descent = font.getmetrics()

            try:
                full = componentIndex[char]["Full"]
            except:
                full = False

            try:
                left = componentIndex[charData[0]]["Left"]
            except:
                left = False

            try:
                right = componentIndex[charData[1]]["Right"]
            except:
                right = False

            if full:
                componentImage = Image.open(
                    f"../Data/Components/{char}.png")
                image.paste(componentImage, (0, 0))
            else:
                if left:
                    componentImage = Image.open(
                        f"../Data/Components/{charData[0]} (Left).png")
                    image.paste(componentImage, (0, 0), componentImage)
                else:
                    draw.text((0, -descent),
                              charData[0], font=font, fill="#000000FF")
                if right:
                    componentImage = Image.open(
                        f"../Data/Components/{charData[1]} (Right).png")
                    image.paste(componentImage, (0, 0), componentImage)
                else:
                    draw.text((4, -descent),
                              charData[1], font=font, fill="#000000FF")
            image.save(targetFilename)
        if len(result[char]) > 1:
            log.warning(f"{char} has more than one locale!")
            for locale in result[char]:
                targetFilename = f"../Output/Glyphs/u{
                    ("%04X" % ord(char))} ({locale}).png"
                log.debug(f"Generating {targetFilename}...")
                _generateImage(result[char][locale])
        else:
            targetFilename = f"../Output/Glyphs/u{
                ("%04X" % ord(char))}.png"
            locale = list(result[char])[0]
            log.debug(f"Generating {targetFilename}...")
            _generateImage(result[char][locale])


if __name__ == '__main__':
    main()

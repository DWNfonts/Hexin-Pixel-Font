import xml.dom.minidom
from PIL import Image, ImageDraw, ImageFont
import logging
import rich.logging


def main():
    FORMAT = "%(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[rich.logging.RichHandler()],
    )

    log = logging.getLogger("rich")

    charset = []
    log.info("Reading charset...")
    with open("Data/Fonts/k12x8 with GB Symbols.kbitx") as f:
        doc = xml.dom.minidom.parse(f)
        for glyphs in doc.getElementsByTagName("kbits")[0].getElementsByTagName("g"):
            if glyphs.hasAttribute("u"):
                charset.append(chr(int(glyphs.getAttribute("u"))))

    log.info("Building glyphs...")
    for char in charset:
        log.debug("Building glyph for %s" % char)
        image = Image.new("RGBA", (12, 8))
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("Data/Fonts/k12x8 with GB Symbols.ttf", 8)
        ascent, descent = font.getmetrics()
        draw.text((0, 0), char, font=font, fill="#000000FF")
        try:
            image.save(f"Output/Glyphs/u{("%04X" % ord(char))}.png")
        except:
            log.warning("%s is invaild in this environment, skip" % char)


if __name__ == "__main__":
    main()

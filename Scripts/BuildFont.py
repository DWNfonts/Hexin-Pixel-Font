from git import exc
from pixel_font_builder import glyph


def main():
    import pixel_font_builder
    from pixel_font_builder.glyph import Glyph
    import logging
    import rich.logging
    from pixel_font_builder import opentype

    FORMAT = "%(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=FORMAT,
        datefmt="[%X]",
        handlers=[rich.logging.RichHandler()],
    )

    log = logging.getLogger("rich")

    def _create_builder(outlineStyle=None):

        def _getGlyphName(filename: str):
            if "(" in filename:  # Multi locales
                import re

                m = re.findall("\\([^ ]*\\)", filename)
                try:
                    if m != None:
                        locale = m[0][1:-1].lower()
                    else:
                        locale = ""
                except:
                    locale = ""
                if locale == "":
                    glyphname = "%s" % filename.replace(".", " ").split(" ")[0]
                else:
                    glyphname = "%s.%s" % (
                        filename.replace(".", " ").split(" ")[0],
                        locale,
                    )
            else:
                locale, glyphname = "", "%s" % filename.replace(".", " ").split(" ")[0]
            return locale, glyphname

        log.debug("Generating font metadata...")

        builder = pixel_font_builder.FontBuilder()

        builder.font_metric.font_size = 8

        builder.font_metric.horizontal_layout.ascent = 7
        builder.font_metric.horizontal_layout.descent = -1

        # TODO: Add support for vertical layout
        builder.font_metric.vertical_layout.ascent = 7
        builder.font_metric.vertical_layout.descent = -1

        # Copies the BDF version of k12x8, is it wrong?
        builder.font_metric.x_height = 0
        builder.font_metric.cap_height = 0

        import git

        repo = git.Repo(search_parent_directories=True)
        commits = list(repo.iter_commits("HEAD"))
        revision = "r" + str(len(commits))

        import json

        with open("../Data/Metadata.json") as f:
            metadata = json.load(f)

        import datetime

        modifiedTimeInTimestamp = repo.head.object.committed_date

        createdTime = datetime.datetime.fromtimestamp(modifiedTimeInTimestamp)

        builder.meta_info.created_time = createdTime

        builder.meta_info.modified_time = datetime.datetime.now()

        modifiedTimeInText = datetime.datetime.now().strftime("%y%m%d-%H%M")

        match outlineStyle:
            case "Square Dot":
                builder.meta_info.family_name = "Hexin Pixel Font, Square Dot"
                shortCode = "square"
            case "Circle Dot":
                builder.meta_info.family_name = "Hexin Pixel Font, Circle Dot"
                shortCode = "circle"
            case _:
                builder.meta_info.family_name = "Hexin Pixel Font"
                shortCode = "normal"

        builder.meta_info.version = ".".join(
            (
                metadata["version"],
                revision,
                shortCode,
                repo.active_branch.name,
                modifiedTimeInText,
            )
        )

        builder.meta_info.weight_name = pixel_font_builder.WeightName.REGULAR
        builder.meta_info.serif_style = pixel_font_builder.SerifStyle.SANS_SERIF
        builder.meta_info.slant_style = pixel_font_builder.SlantStyle.NORMAL
        builder.meta_info.width_style = pixel_font_builder.WidthStyle.MONOSPACED

        builder.meta_info.manufacturer = "DWNfonts"
        builder.meta_info.designer = "Num Kadoma, DWN"
        builder.meta_info.description = (
            "a 12x8 pixel (bitmap) font for mainly Simplified Chinese & Japanese"
        )
        builder.meta_info.copyright_info = (
            "Copyright (c) 2021 Num Kadoma, 2022, 2025 DWN"
        )
        builder.meta_info.license_info = (
            "Licensed under SIL Open Font License, version 1.1"
        )

        builder.meta_info.vendor_url = "https://dwnfonts.cc/@DWNfonts"
        builder.meta_info.designer_url = "https://dwnfonts.cc/@dwn"
        builder.meta_info.license_url = "https://openfontlicense.org"

        builder.meta_info.sample_text = (
            "远芳侵古道，晴翠接荒城。又送王孙去，萋萋满别情。"
        )

        import os

        filelist = os.listdir("../Output/Glyphs")

        builder.glyphs.append(
            Glyph(
                name=".notdef",
                horizontal_origin=(0, -1),
                advance_width=12,
                vertical_origin=(-1, 0),
                advance_height=8,
                bitmap=[
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                    [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0],
                    [1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                ],
            )
        )

        mapping = {}

        for file in filelist:
            log.debug(f"Processing {file}")
            if file.endswith(".png"):
                locale, glyphname = _getGlyphName(file)
                isJSource = "j" in locale
                if isJSource:
                    mapping[int(glyphname.split(".")[0][1:], base=16)] = glyphname
                else:
                    pass  # TODO: Multi-locale support, mostly unnecessary
                log.debug(
                    f"Glyph {glyphname}, {
                    "is" if isJSource else "not"} J Source"
                )

                from PIL import Image

                image = Image.open("../Output/Glyphs/" + file)
                width, height = image.size
                px = image.load()
                glyphData = []
                for y in range(height):
                    lineData = []
                    for x in range(width):
                        if px != None:
                            if px[x, y][3] > 127:
                                lineData.append(1)
                            else:
                                lineData.append(0)
                    glyphData.append(lineData)

                FULLWIDTH_CHAR = list(range(0x00, 0x80)) + list(
                    range(0xFF65, 0xFFA0)
                )  # ASCII + Half-width Kana

                width = (
                    6
                    if (int(glyphname.split(".")[0][1:], base=16) in range(0x00, 0x80))
                    else 12
                )

                if width == 6:
                    log.warning(f"Half-width char {glyphname}")

                builder.glyphs.append(
                    Glyph(
                        name=glyphname,
                        horizontal_origin=(0, -1),
                        advance_width=width,
                        vertical_origin=(-1, 0),
                        advance_height=8,
                        bitmap=glyphData,
                    )
                )

                match outlineStyle:
                    case "Square Dot":
                        builder.opentype_config.outlines_painter = (
                            opentype.SquareDotOutlinesPainter()
                        )
                    case "Circle Dot":
                        builder.opentype_config.outlines_painter = (
                            opentype.CircleDotOutlinesPainter()
                        )
                    case _:
                        pass

        # Here we'd better fix some mappings of characters that in the G source but not in J source.
        # These chars' mappings are set to G source's.

        for file in filelist:
            log.debug("Finding unencoded glyphs...")
            if file.endswith(".png"):
                locale, glyphname = _getGlyphName(file)
                isGSource = "g" in locale
                try:
                    mapping[int(glyphname.split(".")[0][1:], base=16)]
                except:
                    mapping[int(glyphname.split(".")[0][1:], base=16)] = glyphname

        builder.character_mapping.update(mapping)

        return builder

    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "fun":
            outlineStyles = [None, "Square Dot", "Circle Dot"]
        else:
            outlineStyles = [None]
    else:
        outlineStyles = [None]

    for currentOutlineStyle in outlineStyles:
        log.info(
            f"Current outline style: {
                 currentOutlineStyle}, creating builder..."
        )
        builder = _create_builder(currentOutlineStyle)
        if builder != None:
            if currentOutlineStyle != None:
                log.info(
                    f"Building font with {
                         currentOutlineStyle} outline style (OTF)..."
                )
                builder.save_otf(
                    f"../Output/Hexin Pixel Font, {currentOutlineStyle}.otf"
                )
            else:
                log.info("Building font (OTF)...")
                builder.save_otf("../Output/Hexin Pixel Font.otf")
                log.info("Building font (WOFF2)...")
                builder.save_otf(
                    "../Output/Hexin Pixel Font.woff2", flavor=opentype.Flavor.WOFF2
                )
                log.info("Building font (TTF)...")
                builder.save_ttf("../Output/Hexin Pixel Font.ttf")
                log.info("Building font (BDF)...")
                builder.save_bdf("../Output/Hexin Pixel Font.bdf")
                log.info("Building font (PCF)...")
                builder.save_pcf("../Output/Hexin Pixel Font.pcf")


if __name__ == "__main__":
    main()

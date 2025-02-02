def main():
    import pixel_font_builder
    from pixel_font_builder.glyph import Glyph
    import logging
    import rich.logging

    FORMAT = "%(message)s"
    logging.basicConfig(
        level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[rich.logging.RichHandler()]
    )

    log = logging.getLogger("rich")

    def _create_builder():
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
        sha = repo.head.object.hexsha

        import json
        metadata = json.loads("../Output/metadata.json")

        builder.meta_info.version = metadata["version"] + "." + sha

        import datetime
        modifiedTime = repo.head.object.committed_date
        builder.meta_info.created_time = datetime.datetime.fromtimestamp(1738226737)
        builder.meta_info.modified_time = datetime.datetime.fromtimestamp(modifiedTime)
        builder.meta_info.family_name = "Hexin Pixel Font"
        builder.meta_info.weight_name = pixel_font_builder.WeightName.REGULAR
        builder.meta_info.serif_style = pixel_font_builder.SerifStyle.SANS_SERIF
        builder.meta_info.slant_style = pixel_font_builder.SlantStyle.NORMAL
        builder.meta_info.width_style = pixel_font_builder.WidthStyle.MONOSPACED

        builder.meta_info.manufacturer = "DWNfonts"
        builder.meta_info.designer = "Num Kadoma, DWN"
        builder.meta_info.description = "a 12x8 pixel (bitmap) font for mainly Simplified Chinese & Japanese"
        builder.meta_info.copyright_info = "Copyright (c) 2021 Num Kadoma, 2022, 2025 DWN"
        builder.meta_info.license_info = "Licensed under SIL Open Font License, version 1.1"

        builder.meta_info.vendor_url = "https://dwnfonts.cc/@DWNfonts"
        builder.meta_info.designer_url = "https://dwnfonts.cc/@dwn"
        builder.meta_info.license_url = "https://openfontlicense.org"

        builder.meta_info.sample_text = '远芳侵古道，晴翠接荒城。又送王孙去，萋萋满别情。'

        import os
        filelist = os.listdir("../Output/Glyphs")

        builder.glyphs.append(Glyph(
            name=".notdef",
            horizontal_origin=(0, -1),
            advance_width=12,
            vertical_origin=(-1, 0),
            advance_height=8,
            bitmap=[
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ))

        mapping = {}

        for file in filelist:
            log.debug(f"Processing {file}")
            if file.endswith(".png"):
                if "(" in file:  # Multi locales
                    import re
                    m = re.findall("\\([^ ]*\\)", file)
                    try:
                        if m != None:
                            locale = m[0][1:-1].lower()
                        else:
                            locale = ""
                    except:
                        locale = ""
                    if locale == "":
                        glyphname = "%s" % file.replace(".", " ").split(" ")[0]
                    else:
                        glyphname = "%s.%s" % (file.replace(
                            ".", " ").split(" ")[0], locale)
                else:
                    glyphname = "%s" % file.replace(".", " ").split(" ")[0]
                isGSource = (
                    "." in glyphname and "g" in glyphname) or "." not in glyphname
                if isGSource:
                    mapping[int(glyphname.split(".")[0]
                                [1:], base=16)] = glyphname
                else:
                    pass  # TODO: Multi-locale support, mostly unnecessary
                log.debug(f"Glyph {glyphname}, {
                    "is" if isGSource else "not"} G Source")

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

                width = 6 if (int(glyphname.split(
                    ".")[0][1:], base=16) in range(0x00, 0x80)) else 12

                if width == 6:
                    log.warning(f"Half-width char {glyphname}")

                builder.glyphs.append(Glyph(
                    name=glyphname,
                    horizontal_origin=(0, -1),
                    advance_width=width,
                    vertical_origin=(-1, 0),
                    advance_height=8,
                    bitmap=glyphData
                ))

        builder.character_mapping.update(mapping)

        return builder

    builder = _create_builder()
    if builder != None:
        builder.save_otf("../Output/HexinPixelFont.otf")


if __name__ == '__main__':
    main()

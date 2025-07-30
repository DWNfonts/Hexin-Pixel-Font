import sys


def clean():
    import os, shutil

    try: shutil.rmtree("Output")
    except: pass


def build():
    import os
    os.makedirs("Output/Glyphs", exist_ok=True)

    import hexin_pixel_font.BuildChar as bg
    import hexin_pixel_font.FetchGlyphs as fg
    import hexin_pixel_font.FetchCCB as fc
    import hexin_pixel_font.BuildFont as bf

    bg.main()
    fg.main()
    fc.main()
    bf.main(True)


if __name__ == "__main__":
    if sys.argv[1].lower() == "clean":
        clean()
    elif sys.argv[1].lower() == "build":
        clean()
        build()
    else:
        raise ValueError("Invaild argument - use clean / build")

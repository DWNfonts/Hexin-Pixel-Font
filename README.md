# Hexin Pixel Font

> In other languages (not maintained actively)
>
> [简体中文](README.zh.md)

[QQ Group (619164913)](https://qm.qq.com/q/m1cy05q7lg) - [Discord](https://discord.gg/bq5xXTytG8)

Hexin Pixel Font (核心像素体) is a 12x8 pixel (bitmap) font for mainly Simplified Chinese. This repo contains the source of the font, along with some building scripts. The pre-built font files is released at [the Releases page](https://codeberg.org/DWNfonts/Hexin-Pixel-Font/releases).

The word "Hexin" goes to a supervillain's name in a Chinese TV series called 开心超人联盟.

Hexin Pixel Font's glyphs is based on Num Kadoma's [k12x8](https://littlelimit.net/k12x8.htm), which is licensed under the old, public-domain-equivalent M+ license.

The font is under the SIL OFL 1.1, the scripts are under the 3-Clause BSD license. See [LICENSE.md](LICENSE.md) for more details.

> **Under construction:** some chars are auto-generated and look ugly (or incorrect). You can create a [Codeberg issue] or discuss on itch.io (coming soon) to let me know!

## Building

To build it you should have the latest version of Powershell & Python installed. Then, run the following command:

```powershell
pip install -r requirements.txt
```

(It's recommended to use a virtual environment.)

Then run `Scripts/Build.ps1` to compile the font, run `Scripts/Clean.ps1` to clean them. 

## Credits

Thanks the original project [k12x8](https://littlelimit.net/k12x8.htm) and its author [Num Kadoma](https://littlelimit.net/).

Thanks [@TakWolf on GitHub](https://github.com/TakWolf), which developed the [`pixel_font_builder` library](https://github.com/TakWolf/pixel-font-builder) (used for generating fonts), and [Fusion Pixel Font](https://github.com/TakWolf/fusion-pixel-font) (the reference of the glyphs' style).

I will also credit [BMC](https://codeberg.org/DWNfonts/BillionsMustComplete), which is a specific 8x8 OFL-licensed pixel font.
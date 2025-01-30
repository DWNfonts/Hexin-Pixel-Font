# Hexin Pixel Font

[QQ Group](https://qm.qq.com/q/m1cy05q7lg) - [Discord](https://discord.gg/bq5xXTytG8)

Hexin Pixel Font (核心像素体) is a 12x8 pixel (bitmap) font for mainly Simplified Chinese & Japanese. This repo contains the source of the font, along with some building scripts. The pre-built font files is released at [the Releases page](https://codeberg.org/DWNfonts/Hexin-Pixel-Font/releases).

The word "Hexin" goes to a supervillain's name.

Hexin Pixel Font is a fork of Num Kadoma's [k12x8](https://littlelimit.net/k12x8.htm).

The font is under the [SIL OFL 1.1](LICENSE.md) license.

(under construction)

## Building

To build it you should have the latest version of Powershell & Python installed. Then, run the following command:

```powershell
pip install -r requirements.txt
```

(It's recommended to use a virtual environment.)

Then run `Scripts/Build.ps1`, and following the instructions, run `Scripts/Clean.ps1` to clean them. At that time, the script only generate characters' glyph image, not the font itself.
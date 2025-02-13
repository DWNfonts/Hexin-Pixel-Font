# 核心像素体

> [English](README.md)

[QQ群（619164913）](https://qm.qq.com/q/m1cy05q7lg)-[Discord](https://discord.gg/bq5xXTytG8)

核心像素体（Hexin Pixel Font）是个宽十二高八像素的像素（点阵）主打简中的字体。此仓库包含字体源代码，又带一些构建脚本。预构建字体文件于[版本发布页](https://codeberg.org/DWNfonts/Hexin-Pixel-Font/releases)释出。

词“核心”指的是中国动画《开心超人联盟》中的一个反派名。

核心像素体的字形基于门真奈武的[k12x8](https://littlelimit.net/k12x8.htm)，后者以公有领域等价的老M+协议释出。

这字体以SIL OFL 1.1释出，脚本以3句BSD协议释出。详见[LICENSE.md](LICENSE.md)。

（未完工）

## 构建

要构建他你必须安装最新版的PowerShell和Python。接着运行下列脚本：

```powershell
pip install -r requirements.txt
```

（建议使用虚拟环境。）

然后运行`Scripts/Build.ps1`去编译字体，运行`Scripts/Clean.ps1`来清除。

## 鸣谢

感谢原作[k12x8](https://littlelimit.net/k12x8.htm)及作者[门真奈武](https://littlelimit.net/)。

感谢[GitHub上的@TakWolf](https://github.com/TakWolf)，他开发了[`pixel_font_builder`库](https://github.com/TakWolf/pixel-font-builder)（用来生成字体）及[缝合像素字体](https://github.com/TakWolf/fusion-pixel-font)（字形风格参考）。
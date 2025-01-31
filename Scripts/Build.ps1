Set-Location $PSScriptRoot
Remove-Item ../Output/HexinPixelFont.otf -Force # bug?
New-Item ../Output/Glyphs -ItemType Directory -Force
python FetchGlyphs.py
python BuildChar.py
python BuildFont.py
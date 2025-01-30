Set-Location $PSScriptRoot
New-Item ../Output/Glyphs -ItemType Directory -Force
python BuildChar.py
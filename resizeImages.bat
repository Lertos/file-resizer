@echo off

rem You can change "128x128" to whatever width/height you want to resize to
for /F "tokens=*" %%A in (filesToResize.txt) do magick mogrify -resize 128x128 "%%A"

rem magick mogrify -resize 256x256 "C:\Users\Dylan\Desktop\Projects\FlaskSimpleRPG\badge.PNG"

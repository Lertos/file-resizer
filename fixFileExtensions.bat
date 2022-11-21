@echo off

rem This is meant to fix any file extensions that have capitals
FOR /D /r %%G in (*) DO rename "%%~fG\*.PNG" "*.png"

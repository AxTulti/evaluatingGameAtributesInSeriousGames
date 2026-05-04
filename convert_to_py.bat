@echo off

jupyter nbconvert --to script --no-prompt %1
pause
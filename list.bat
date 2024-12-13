@echo off
:: Creează fișierul text care va conține structura de directoare și fișiere
set output_file=structura_directoare.txt

:: Afișează structura directorului curent și a subdirectorilor într-un fișier
tree /F /A > "%output_file%"

:: Mesaj de confirmare
echo Structura folderelor si fisierelor a fost scrisa in %output_file%
pause

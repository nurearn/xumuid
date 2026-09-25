@echo off
title Push ke GitHub - xumuid
cd /d "%~dp0"
echo ===================================================
echo Mengirim pembaruan ke https://github.com/nurearn/xumuid...
echo ===================================================
echo.
git push origin main
echo.
if %errorlevel% equ 0 (
    echo [SUKSES] Berhasil di-push ke GitHub!
) else (
    echo [GAGAL] Terjadi kendala saat push. Silakan cek pesan di atas.
)
echo.
pause

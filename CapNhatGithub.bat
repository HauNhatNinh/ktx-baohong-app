@echo off
color 0A
echo ====================================================================
echo        TU DONG DONG BO CODE LEN GITHUB CHO DO AN KTX
echo ====================================================================
echo.

set GIT_PATH=D:\TTCN_BaoHongKTX\PortableGit\bin\git.exe
if not exist "%GIT_PATH%" (
    set GIT_PATH=git
)

:: Khoi tao git neu chua co
if not exist ".git" (
    echo [0/3] Lan dau tien chay: Khoi tao du lieu Github...
    "%GIT_PATH%" init
    "%GIT_PATH%" remote add origin https://github.com/HauNhatNinh/ktx-baohong-app.git
    "%GIT_PATH%" branch -M main
    "%GIT_PATH%" config user.email "hn.ninh03@gmail.com"
    "%GIT_PATH%" config user.name "Hau Nhat Ninh"
)

echo [1/3] Dang thong ke cac file ban vua sua chua toi luc nay...
"%GIT_PATH%" add .

echo [2/3] Dang tien hanh luu buoc phat trien vao lich su...
"%GIT_PATH%" commit -m "Auto Update: Day tap tin moi len Github"

echo [3/3] Dang tai code xuyen vu tru len GITHUB (Render se tu cap nhat)...
"%GIT_PATH%" push -u origin main --force

if %ERRORLEVEL% neq 0 (
    echo.
    echo ====================================================================
    color 0C
    echo [LOI] CO LOI XAY RA KHI DAY DU LIEU!
    echo Vui long dac biet nho: Ban phai dang nhap bang "Sign in with your browser"! Giao dien dang nhap se hien len, hay check no nhe.
) else (
    echo.
    echo ====================================================================
    color 0A
    echo [THANH CONG] RUC RO!!!
    echo Website tren Render.com cua ban dang tu dong nhan file moi tu Github. Ban vao xem ket qua sau 2 phut nua nhe!
)
echo.
pause

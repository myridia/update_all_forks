#!/bin/sh
#rm dist build -Rf

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo $OSTYPE
    pyinstaller main.py --onefile --path env/lib/site-packages --name=uaf_linux    
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo $OSTYPE
    pyinstaller main.py --onefile --path env/lib/site-packages --name=uaf_macos
elif [[ "$OSTYPE" == "cygwin" ]]; then
    pyinstaller main.py --onefile --path env/lib/site-packages --name=uaf_cygwin        
elif [[ "$OSTYPE" == "msys" ]]; then
    echo $OSTYPE
        pyinstaller main.py --onefile --path env/lib/site-packages --name=uaf_win64
elif [[ "$OSTYPE" == "win32" ]]; then
    echo $OSTYPE
    pyinstaller main.py --onefile --path env/lib/site-packages --name=uaf_win32
elif [[ "$OSTYPE" == "freebsd"* ]]; then
    echo $OSTYPE
    pyinstaller main.py --onefile --path env/lib/site-packages --name=uaf_freebsd
else
    echo $OSTYPE
    pyinstaller main.py --onefile --path env/lib/site-packages --name=uaf_linux       
fi








#!/bin/sh

rm dist build -Rf
pyinstaller    main.py --onefile --path env/lib/site-packages --name=update_all_forks

#docker run -v "$(pwd):/src/" engineervix/pyinstaller-linux "pyinstaller -F main.py"
#docker run -v "$(pwd):/src/" engineervix/pyinstaller-linux

#sudo cp config.ini dist/linux

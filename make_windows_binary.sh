docker run -v "$(pwd):/src/" engineervix/pyinstaller-linux "pyinstaller -F main.py"
docker run -v "$(pwd):/src/" engineervix/pyinstaller-linux
sudo cp config.ini dist/windows/


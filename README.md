# update-all-git-forks
Update all my Github Forks via a Python Script

## Install Git Source
```
git clone  https://github.com/myridia/update_all_forks.git
cd update_all_forks
```

## Make the Virtual Environment for Python
In this example, I use Python version3.12
```console
python3.12 -m venv env 
. env/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```


## Configure the config.toml file
First copy default to the config.tool file what	can be loaded by the script
```console
cp config_default.ini config.ini
```

## Get your GitHub token and fill it to the config.toml file
* Help Page how to get your token https://iamnaran.medium.com/fixed-support-for-password-authentication-was-removed-628faf76057


## Start the Script 
```
python main.py
```

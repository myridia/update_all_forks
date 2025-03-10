# update_all_forks
Update all my Github Forks via a Python Script

## First you need to get your GitHub token 
* Help Page how to get your token https://iamnaran.medium.com/fixed-support-for-password-authentication-was-removed-628faf76057


## For Linux downlaod a release 
```console
wget https://github.com/myridia/update_all_forks/releases/download/main/update_all_forks
chmod +x update_all_forks
```

## Run with one paramenter token
```console
./update_all_forks --token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```


## Install Git Source
```console
git clone  https://github.com/myridia/update_all_forks.git
cd update_all_forks
```

## Run from source
In this example, I use Python version3.12

```console
python3.12 -m venv env 
. env/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
./main.py --token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```









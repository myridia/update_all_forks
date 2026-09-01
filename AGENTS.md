# AGENTS.md — update_all_forks

## What this is
A Python CLI tool that updates all your GitHub forks by syncing them with their upstream repositories, using a GitHub personal access token.

## Stack
- Python 3.12+
- PyGithub / GitHub API

## Build
```bash
python3.12 -m venv env
. env/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
```

## Run
```bash
./main.py --token=<YOUR_GITHUB_TOKEN>
```
Or download a pre-built release binary.

## Structure
- `main.py` — entry point
- `requirements.txt` — Python dependencies

## Conventions
- No comments in code unless asked.
- Never commit tokens or credentials.
- Verify: `python3 -m py_compile main.py`

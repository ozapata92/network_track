# Network tracker

## Create venv and active

`python -m venv env`

To activate in windows using powershell `.\env\Scripts\Activate.ps1`

## Install dependencies

`pip install -r requirements.txt`

## Network task analize

Scan all remote connections and show details about the origin
`python network_task_analize.py`

## Network scan

Scan all hosts in your target, collect all open ports and scan vulnerabilities working behind the services
`python network_scan.py`

## Screenshots

![App Screenshot](https://imgur.com/NIBOcHg.jpg)

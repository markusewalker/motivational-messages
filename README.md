# Motivational Messages

| Standup Reminder | Break Reminder | Lunch Reminder | End of Day Reminder | Tests |
|:----------------:|:--------------:|:--------------:|:-------------------:|:-----:|
| [![Standup](https://github.com/markusewalker/motivational-messages/actions/workflows/standup.yml/badge.svg?branch=main)](https://github.com/markusewalker/motivational-messages/actions/workflows/standup.yml) | [![Break](https://github.com/markusewalker/motivational-messages/actions/workflows/break.yml/badge.svg?branch=main)](https://github.com/markusewalker/motivational-messages/actions/workflows/break.yml) | [![Lunch](https://github.com/markusewalker/motivational-messages/actions/workflows/lunch.yml/badge.svg?branch=main)](https://github.com/markusewalker/motivational-messages/actions/workflows/lunch.yml) | [![End of Day](https://github.com/markusewalker/motivational-messages/actions/workflows/eod.yml/badge.svg?branch=main)](https://github.com/markusewalker/motivational-messages/actions/workflows/eod.yml) | [![Tests](https://github.com/markusewalker/motivational-messages/actions/workflows/run-tests.yml/badge.svg?branch=main)](https://github.com/markusewalker/motivational-messages/actions/workflows/run-tests.yml) |

This is a Github Actions based framework that is meant to send motivational messages via the Pushover app for the typical work day! However, if you want to try running this locally, continue reading on to see how.

This project utilizes Pipedream along with cron-job.org to use an external scheduler for each of the reminders. Therefore, you will not see the scheduled times in the workflows despite them routinely running.

## Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Getting Started](#Getting-Started)
3. [Running Program](#Running-Program)

## Prerequisites
In order to properly run this, you will need the following installed on your client machine:

- `python3`
- `pip3`
- `venv` (need `pip3` before installing)
- Pushover app installed on your device

## Getting Started
Once you have followed the prerequisites and installed all the needed dependencies, run the following commands:

```
python3 -m venv env
source env/bin/activate
pip3 install -r required_libraries.txt
```

Once done, create an `.env` file that has the following filled out:

```
PUSHOVER_USER_KEY   = ""
PUSHOVER_API_TOKEN  = ""
```

## Running Program
To run the actual program, there are a few options you can do as indicated by `python3 main.py -h`. Here is the that output for your convenience:

```
 python3 main.py -h
usage: pushover.py [-h] [--type {default,standup,break,lunch,end_work_day}] [--list-types]

Send a motivational message via Pushover

options:
  -h, --help            show this help message and exit
  --type, -t {default,standup,break,lunch,end_work_day}
                        Type of message to send
  --list-types, -l      List available message types
```

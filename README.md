# Motivational Messages
This is a Github Actions based framework that is meant to send motivational messages via email-to-SMS gateway! However, if you want to try running this locally, continue reading on to see how.

## Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Getting Started](#Getting-Started)
3. [Running Program](#Running-Program)

## Prerequisites
In order to properly run this, you will need the following installed on your client machine:

- `python3`
- `pip3`
- `venv` (need `pip3` before installing)

## Getting Started
Once you have followed the prerequisites and installed all the needed dependencies, run the following commands:

```
python3 -m venv env
source env/bin/activate
pip3 install -r required_libraries.txt
```

Once done, create an `.env` file that has the following filled out:

```
EMAIL=""
PASSWORD=""     # Must not include any spaces or dashes
PHONE_NUMBER=""
CARRIER=""
```

## Running Program
To run the actual program, you will need to do run the following command:

`python3 standup.py`
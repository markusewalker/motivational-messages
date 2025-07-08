# Motivational Messages
This is a Github Actions based framework that is meant to send motivational messages via email-to-SMS gateway for the typical work day! However, if you want to try running this locally, continue reading on to see how.

## Table of Contents
1. [Prerequisites](#Prerequisites)
2. [Getting Started](#Getting-Started)
3. [Running Program](#Running-Program)
4. [Testing](#Testing)

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
APP_PASSWORD=""
PHONE_NUMBER=""     # Must not include any spaces or dashes
CARRIER=""
```

## Running Program
To run the actual program, there are a few options you can do as indicated by `python3 sms.py -h`. Here is the that output for your convenience:

```
$ python3 sms.py -h
usage: sms.py [-h] [--type {standup,break,lunch,end_work_day}] [--list-types]

Send motivational SMS messages

options:
  -h, --help            show this help message and exit
  --type, -t {standup,break,lunch,end_work_day}
                        Type of message to send
  --list-types, -l      List available message types
```

## Testing
`pytest` has been used to properly test this program in completeness. You can use the following command to test as an example:

```
 pytest -m "unit or integration" -v
========================================================= test session starts ==========================================================
platform darwin -- Python 3.13.0, pytest-8.4.1, pluggy-1.6.0 -- /path/to/python
cachedir: .pytest_cache
rootdir: /path/to/github.com/motivational-messages
configfile: pyproject.toml
collected 9 items                                                                                                                      

test_standup.py::test_simple_dummy_message_send PASSED                                                                           [ 11%]
test_standup.py::test_get_message_default PASSED                                                                                 [ 22%]
test_standup.py::test_get_message_standup PASSED                                                                                 [ 33%]
test_standup.py::test_get_message_invalid_type PASSED                                                                            [ 44%]
test_standup.py::test_list_types_short_command PASSED                                                                            [ 55%]
test_standup.py::test_list_types_long_command PASSED                                                                             [ 66%]
test_standup.py::test_standup_message_command PASSED                                                                             [ 77%]
test_standup.py::test_sms_script_list_types PASSED                                                                               [ 88%]
test_standup.py::test_sms_script_standup_type PASSED                                                                             [100%]

========================================================== 9 passed in 0.18s ===========================================================
```
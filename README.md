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

In order to properly run this, you will need the following installed on your client machine:

- Go (1.25+)
- Pushover app installed on your device

## Getting Started
To get going, there are two options.
1. Directly running `go run main.go <motivational message>`
2. Downloading the relevant binary in the Releases pages

### Option 1

Here is the usage of the CLI tool:

```
$ go run main.go 
Motivational Messages is a CLI application that sends motivational messages at
specified times throughout the typical 9-5 workday

Usage:
  gomotivate [command]

Available Commands:
  break       Sends a break time reminder notification
  completion  Generate the autocompletion script for the specified shell
  eod         Sends an end of day reminder notification
  help        Help about any command
  lunch       Sends a lunch time reminder notification
  standup     Sends a stand-up reminder notification

Flags:
  -h, --help   help for gomotivate
```

### Option 2
If you download the binary, ensure that you download the asset specific to your OS and architecture. When unzipping, you can customize the name however you see fit. By default, `gomotivate` is the name used in the usage.
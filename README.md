# eva

Demo Project to manage AWS instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots

## Configure

Create the aws profile for eva
`aws configure --profile eva`

Navigate to project directory and install dependencies
`pipenv install`

Install development dependencies
`pipenv install -d`


## Running
`pipenv run python boto/boto.py <command> <subcommand> <--project=Project>`

*command* is instances, volumes, snapshots
*subcommand* - depends on  command
*project* is optional

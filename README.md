# Fairwinds EC2 Creation Automation Project

## Description
A script to automate the creation of a new AWS EC2 instance running a base Django app.

## Installation Requirements
On your local machine you need to install the following:
* Python 3.7
  * [View Installation Instructions](https://www.python.org/downloads/)
* AWS CLI
  * [View Installation Instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

## Packages
A complete requirements list is found in the `requirements.txt` file. This script relies on two key packages:
* [Paramiko (for SSH)](http://www.paramiko.org/)
* [Boto3 (for AWS control)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Usage
Before using the script, you must configure your AWS CLI instance by running the command:
```
aws configure
```
Enter the correct information provided from AWS. The AWS CLI requires an AccessKeyId, SecretAccessKey, and Region. 

Once aws has been configured, install the required python packages from the requirement.txt file using pip:

```
pip install -r requirements.txt
```

To use this script, run in a blank directory using
```
python aws_ec2.py
```

## Process & Write Up
I started this project with a requirements-lite mindset. My original plan was to create a bash script that utilized `curl` and the AWS REST API to create the required resources, then use the built in SSH commands in terminal to facilitate setting up a Django web app on the remote machine. When I began combing the documentation, I realized two things: the REST API was non-intuitive (learning would put me over the deadline) and that as-is the bash script would be system exclusive. With this in mind, I turned to building a Python script using boto3 and paramiko. I am well versed in Python and familiar with boto3. After searching the boto3, paramiko, and EC2 documentation, I began writing the script to auto-generate any requirements for an EC2 instance to launch. Once in place, creating the EC2 instance itself was a matter of calling a function and passing the correct parameters in-line with the defaults created earlier in the script. SSH with paramiko took me the longest to parse through. I ran into an issue where the SSH connection wasn't getting established even after the instance had fully launched. Research informed me there is a small window where an EC2 instance does not allow SSH connections, so I implemented a re-connect loop with five maximum tries and a ten second wait between each try. This proved to establish a connection after 1-2 tries. I ran out of time implementing the web app on the EC2 instance, though the method to do so is staged in the existing codebase. I included a bash script which gets read line-by-line in the main Python script and feeds the commands into the SSH console. This allows for finer-grain control over debugging and output checking from the remote EC2 instance. 

Future work includes fully implementing the Django setup script and creating test conditions to run against. Local logging and command line arguments for instance names are nice-to-haves that could be implemented as well. 

## License
Copyright 2020 Max Miller

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

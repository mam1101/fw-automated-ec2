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
A complete list of requirements is in the `requirements.txt` file. This script relies on two key packages:
* [Paramiko (for SSH)](http://www.paramiko.org/)
* [Boto3 (for AWS control)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

## Usage
Before using the script, you must configure your AWS CLI instance by running the command:
```
aws configure
```
Enter the correct information provided from AWS. The AWS CLI requires an AccessKeyId, SecretAccessKey, and Region. Once entered, run a python
package installation on the requirement.txt file using pip:

```
pip install -r requirements.txt
```

To use this script, run in a blank directory using
```
python3 aws_ec2.py.
```

## License
Copyright 2020 Max Miller

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

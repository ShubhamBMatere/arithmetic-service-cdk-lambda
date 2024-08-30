
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
---------------------------------------------------------------------------------------------------------------------------------------------------

# AWS Lambda Arithmetic Service

This project implements a basic arithmetic service using AWS Lambda and AWS CDK. The service exposes a RESTful API with endpoints for addition, subtraction, multiplication, and division.

## Requirements
* `AWS CLI`
* `AWS CDK`
* `Python 3.x`

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
----------------------------------------------------------------------------------------------------------------------------------------------------
2. **Install Dependencies**

Set up a Python virtual environment and install dependencies:
`python -m venv .env`
`source .env/bin/activate`
# On Windows, use `.env\Scripts\activate`
`pip install -r requirements.txt`

----------------------------------------------------------------------------------------------------------------------------------------------------
3. **API Endpoints**

Addition: /v1/add?numbers=2,3
Subtraction: /v1/subtract?numbers=5,2
Multiplication: /v1/multiply?numbers=2,3
Division: /v1/divide?numbers=6,2

--------------------------------------------------------------------------------------------------------------------------------------------------
4. **Testing**
Use tools like curl or Postman to test the API endpoints. Example curl commands:
`curl "https://your-api-id.execute-api.your-region.amazonaws.com/prod/v1/add?numbers=2,3"`



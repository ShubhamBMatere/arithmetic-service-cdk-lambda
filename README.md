
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
On Windows, use `.env/Scripts/activate`

`pip install -r requirements.txt`

----------------------------------------------------------------------------------------------------------------------------------------------------
3. **Testing the Deployed Arithmetic ServiceAPI Endpoints**

1. Locate the API Endpoint
* Find the API Gateway URL:
* Log in to the AWS Management Console.
* Navigate to the API Gateway service.
* Find the API that you deployed. It should have the name you specified in your CDK stack (e.g. in my case, ArithmeticAPI).
![image](https://github.com/user-attachments/assets/db34e0af-ce6f-4dfb-a789-98af5d19b1cc)

* Click on the API name and find the Invoke URL in the Stages section. This URL will look something like 
`https://your-api-id.execute-api.your-region.amazonaws.com/prod.`
![image](https://github.com/user-attachments/assets/5530730d-b10a-400d-b917-de227e42c0b5)


 *Testing the API Endpoints*

 You can test the API endpoints using tools like curl, Postman, or a web browser. Below are examples using curl and Postman or browser.
 I am using browser to test, also I am attaching screenshot for the some scenarios mentioned.
 
* `Addition:`
* `curl "https://your-api-id.execute-api.your-region.amazonaws.com/prod/v1/add?numbers=2,3"`
  
![image](https://github.com/user-attachments/assets/bd7f2a50-d169-47da-983e-bea28468524c)

* `Subtraction:`
*  `curl "https://your-api-id.execute-api.your-region.amazonaws.com/prod/v1/subtract?numbers=5,2"`
  ![image](https://github.com/user-attachments/assets/ea27a8d9-a2be-4e94-b906-57424643216c)

* `Multiplication:`
* `curl "https://your-api-id.execute-api.your-region.amazonaws.com/prod/v1/multiply?numbers=2,3"`
  
  ![image](https://github.com/user-attachments/assets/b678ec8d-fd9a-4c83-ba11-0efaa9d1239b)

* `Division:`
* `curl "https://your-api-id.execute-api.your-region.amazonaws.com/prod/v1/divide?numbers=6,2"`
  
  ![image](https://github.com/user-attachments/assets/3063ed3b-dd9c-412f-bd3f-85c31ba3e4c6)

* `Error Case1: When Division by zero error`
  
  ![image](https://github.com/user-attachments/assets/c69b1c83-781b-4c10-8a5b-49a839108fc3)

* `Error Case2: When numeric values are not provided.`
  ![image](https://github.com/user-attachments/assets/c8d797b9-56ea-40b1-ac6d-9946e6515e58)

* `Error Case3: When no query parameters provided or 'numbers' parameter missing.`
  ![image](https://github.com/user-attachments/assets/15dc9b13-021d-484a-a73a-d4b3d13a05b1)

* `Using Postman:`
* If you want to test it through Postman, follow the steps:
* 
Open Postman:
* Create a New Request:

* Click on the New button and select Request.
Set Up the Request:

Method: Select GET.
URL: Enter the API endpoint URL, for example, https://your-api-id.execute-api.your-region.amazonaws.com/prod/v1/add?numbers=2,3.
Send the Request:

Click Send.
Check the Response:

You should see the JSON response in the response body section.






--------------------------------------------------------------------------------------------------------------------------------------------------
4. **Instructions on How to Deploy and Test the Service**

Deployment Instructions:

i. Clone the Repository: 
`git clone https://github.com/your-username/your-repository-name.git`
`cd your-repository-name`

ii. Set Up Your Python Environment:

`python -m venv .env`
`source .env/bin/activate`
On Windows, use 
`.env\Scripts\activate`

iii. Install Dependencies:
`python -m pip install -r requirements.txt`

iv. Bootstrap Your CDK Environment:
`cdk bootstrap`

v. Deploy all stacks:
`cdk deploy --all --require-approval never --profile`

-----------------------------------------------------------------------------------------------------------------------------------------------------

# Brief Explanation of Design Decisions and Assumptions
Design Decisions:

CDK for Infrastructure as Code (IaC): AWS CDK was chosen to manage the infrastructure because it allows for a code-first approach to define AWS resources. This provides more flexibility and reusability compared to manual setup or template-based IaC tools like CloudFormation.

AWS Lambda: AWS Lambda was selected as the compute service to host the arithmetic service due to its scalability and cost-efficiency for a stateless service.

API Gateway: API Gateway was used to expose the Lambda function as a RESTful API, providing a simple and secure interface for the arithmetic operations.

Python for Lambda: Python was chosen as the programming language due to its simplicity, readability, and the availability of necessary libraries for the arithmetic operations.

Assumptions:

Stateless Service: The service does not require persistent storage, so there is no need for a database or caching layer.

Sequential Operations: The arithmetic operations are performed sequentially from left to right, as specified in the requirements.

Error Handling: Basic error handling was implemented to manage edge cases like division by zero or invalid inputs, ensuring robustness and reliability.







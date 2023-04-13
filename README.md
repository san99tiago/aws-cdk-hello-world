# :trumpet: AWS CDK HELLO WORLD :trumpet:

<img src="assets/HelloWorldLambdaArchitecture.png" width=90%> <br>

This is a simple custom `Hello-world` project deployed on AWS with the following specifications:

- Infrastructure as Code with [AWS CDK-Python](https://aws.amazon.com/cdk/)
- Source Code with [AWS Lambda Functions](https://aws.amazon.com/lambda/) built with [Python Runtime](https://www.python.org)
- Tests with [UnitTest Python Framework](https://docs.python.org/3/library/unittest.html)

This project was inspired by the following videos:

- [Werner Vogels on the AWS Cloud Development Kit (AWS CDK)](https://youtu.be/AYYTrDaEwLs)

The information of this repository is based on many online resources, so feel free to use it as a guide for your future projects!. <br>

## How to run this project? :dizzy:

All projects are well commented (even over-commented sometimes for clarity). <br>

The necessary commands to deploy/destroy the solution can be found at:

- [`important_commands.sh`](important_commands.sh)

> Note: please update the commands based on your needs (account, region, etc...)

## AWS CDK :cloud:

[AWS Cloud Development Kit](https://aws.amazon.com/cdk/) is an amazing open-source software development framework to programmatically define cloud-based applications with familiar languages. <br>

My personal opinion is that you should learn about CDK when you feel comfortable with cloud-based solutions with IaC on top of [AWS Cloudformation](https://aws.amazon.com/cloudformation/). At that moment, I suggest that if you need to enhance your architectures, it's a good moment to use these advanced approaches. <br>

The best way to start is from the [Official AWS Cloud Development Kit (AWS CDK) v2 Documentation](https://docs.aws.amazon.com/cdk/v2/guide/home.html). <br>

## Dependencies :vertical_traffic_light:

The dependencies are explained in detail for each project, but the most important ones are Node, Python and the AWS-CDK libraries. <br>

My advice is to primary understand the basics on how CDK works, and then, develop amazing projects with this incredible AWS tool!. <br>

### Software dependencies (based on project)

- [Visual Studio Code](https://code.visualstudio.com/) <br>
  Visual Studio Code is my main code editor for high-level programming. This is not absolutely necessary, but from my experience, it gives us a great performance and outstanding extensions to level-up our software development. <br>

- [NodeJs](https://nodejs.org/en/) <br>
  NodeJs is a JavaScript runtime built on Chrome's V8 JavaScript engine programming language. The community is amazing and lets us handle async functionalities in elegant ways. In this case, we need it for the main "CDK" library, that is built on top of NodeJS.<br>

- [Python](https://www.python.org/) <br>
  Python is an amazing dynamic programming language that allow us to work fast, with easy and powerful integration with different software solutions. We will use the Python CDK libraries.<br>

### Libraries and Package dependencies (depending on the scenario)

- [CDK CLI (Toolkit)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) <br>
  To work with the CDK, it is important to install the main toolkit as a NodeJs global dependency. Then, feel free to install the specific language AWS-CDK library (for example: [aws-cdk.core](https://pypi.org/project/aws-cdk.core/)). <br>

- [AWS CLI](https://aws.amazon.com/cli/) <br>
  The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services. We will use it for connecting to our AWS account from the terminal (authentication and authorization towards AWS). <br>

## Special thanks :gift:

- Thanks to all contributors of the great OpenSource projects that I am using. <br>

## Author :musical_keyboard:

### Santiago Garcia Arango

<table border="1">
    <tr>
        <td>
            <p align="center">Senior DevOps Engineer passionate about advanced cloud-based solutions and deployments in AWS. I am convinced that today's greatest challenges must be solved by people that love what they do.</p>
        </td>
        <td>
            <p align="center"><img src="assets/SantiagoGarciaArangoCDK.png" width=80%></p>
        </td>
    </tr>
</table>

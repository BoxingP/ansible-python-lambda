ansible-python-lambda
=====================

Deploying [AWS Lambda][lambda] functions with [Ansible][ansible],
forked from GitHub repo [ansible-python-lambda][github].

Requirements
------------

* Python 3.0+
* Ansible 2.10+

Usage
-----

1. Run `ansible-galaxy install -r requirements.yml`. It will install roles included in `requirements.yml`.

1. Run `ansible-playbook playbook.yml`. It will create a Cloudformation stack
   in your AWS account called `my-lambda-function` that runs the example Lambda
   function.

[lambda]: https://aws.amazon.com/lambda/
[ansible]: https://www.ansible.com/
[github]: https://github.com/YPlan/ansible-python-lambda

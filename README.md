ansible-python-lambda
=====================

Deploying [AWS Lambda][lambda] functions with [Ansible][ansible].

For example, we use it combines with this [function][function] to stop and start AWS instances.

Requirements
------------

* Python 3.0+
* Ansible 2.10+

Usage
-----

1. Run `ansible-galaxy install -r requirements.yaml`. It will install roles included in `requirements.yaml`.

1. Run `ansible-playbook playbook.yaml`. It will create a Cloudformation stack
   in your AWS account called `my-lambda-function` that runs the example Lambda
   function.

Reference
---

1. [How do I stop and start Amazon EC2 instances at regular intervals using Lambda?
][aws]

1. GitHub repo [ansible-python-lambda][github]

1. GitHub repo [aws-lambda-instance-schedule][example]

[aws]: https://aws.amazon.com/premiumsupport/knowledge-center/start-stop-lambda-cloudwatch/
[lambda]: https://aws.amazon.com/lambda/
[ansible]: https://www.ansible.com/
[github]: https://github.com/YPlan/ansible-python-lambda
[example]: https://github.com/1Strategy/aws-lambda-instance-schedule
[function]: https://github.com/BoxingP/aws-lambda-python-function

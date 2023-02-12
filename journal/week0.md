# Week 0 — Billing and Architecture

## Install AWS CLI

Run following commands on CLI to install AWS CLI

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version
```

Persist AWS CLI configuration variables in gitpod using following instructions

```
gp env AWS_ACCESS_KEY_ID=<Value>
gp env AWS_SECRET_ACCESS_KEY=<Value>
gp env AWS_DEFAULT_REGION=<value>

```
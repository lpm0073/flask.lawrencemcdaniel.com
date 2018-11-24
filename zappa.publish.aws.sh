#!/bin/sh
# McDaniel
# Nov 2018
#
# Usage:     Push current codebase to AWS API Gateway & Lambda
#
# Reference: https://blog.apcelent.com/deploy-flask-aws-lambda.html
#            https://github.com/Miserlou/Zappa
#---------------------------------------------------------
zappa update dev

#!/usr/bin/env python3

from aws_cdk import core

from bootcamp_data_engineering.bootcamp_data_engineering_stack import BootcampDataEngineeringStack


app = core.App()
BootcampDataEngineeringStack(app, "bootcamp-data-engineering")

app.synth()

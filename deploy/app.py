#!/usr/bin/env python3

from aws_cdk import core

from sample_prj.frontend import FrontendStack
from sample_prj.networking import NetworkingAndDBStack

app = core.App()
FrontendStack(app, "sample_prj-frontend")
NetworkingAndDBStack(app, "sample_prj-networking-db")

app.synth()

#!/bin/bash
# this script shows the body size
curl -sI $1 | grep Length | cut -d " " -f2

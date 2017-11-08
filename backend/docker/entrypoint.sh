#!/usr/bin/env bash

cd /opt/app || exit 1

/usr/bin/dumb-init -- make run

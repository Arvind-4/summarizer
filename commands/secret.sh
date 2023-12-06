#!/bin/bash

SECRET=32

python3 -c 'import secrets; print(secrets.token_urlsafe(int('$SECRET')))'
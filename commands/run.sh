#!/bin/bash

gunicorn src.main:app --reload --bind 0.0.0.0:8000
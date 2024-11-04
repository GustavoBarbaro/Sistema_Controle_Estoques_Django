#!/bin/bash
# python manage.py runserver 0.0.0.0:8000
daphne -b 0.0.0.0 -p 8000 core.asgi:application


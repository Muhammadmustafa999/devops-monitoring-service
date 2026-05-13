# DevOps Monitoring Service

Lightweight service health monitoring and alerting platform
for internal DevOps teams.

## Features
- Real-time health checks on registered service endpoints
- CPU, memory, and disk usage monitoring
- Automated alerting via email, webhook, or Slack
- Deployment event tracking and correlation
- 90-day metrics retention
- REST API for dashboard integration

## Tech Stack
- Django 4.1 (REST API)
- Redis (metrics storage and caching)
- PostgreSQL (persistent alert history)

## Quick Start
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Security Scanning
This repository is monitored by ExposureIQ for
CVE vulnerabilities and secure coding violations.

"""
DevOps Monitoring Service — Configuration
Internal service for tracking deployment health
"""
from datetime import timedelta

# Service configuration
SERVICE_NAME = "devops-monitoring-service"
SERVICE_VERSION = "1.3.0"
SERVICE_PORT = 8080

# Monitoring intervals
HEALTH_CHECK_INTERVAL = timedelta(seconds=30)
ALERT_COOLDOWN = timedelta(minutes=5)
METRICS_RETENTION_DAYS = 90

# SEC DJANGO-001: DEBUG=True left in config
# Should use environment variable: DEBUG = os.environ.get('DEBUG', False)
DEBUG = True

# Alert thresholds
CPU_ALERT_THRESHOLD = 85      # percent
MEMORY_ALERT_THRESHOLD = 90   # percent
DISK_ALERT_THRESHOLD = 80     # percent
RESPONSE_TIME_THRESHOLD = 2.0 # seconds

# Supported notification channels
NOTIFICATION_CHANNELS = ['email', 'webhook', 'slack']

# Metrics storage
METRICS_BACKEND = 'redis'
METRICS_PREFIX = 'devops_monitor'

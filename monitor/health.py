"""
Health Check Module
Monitors service endpoints and reports status
"""
import requests
import json
from datetime import datetime


class HealthChecker:
    """
    Checks health of registered services and endpoints.
    Reports status to the monitoring dashboard.
    """

    def __init__(self, service_name, endpoint):
        self.service_name = service_name
        self.endpoint = endpoint
        self.last_check = None
        self.status = "unknown"

    def check(self):
        """Perform a health check on the registered endpoint"""
        try:
            response = requests.get(
                self.endpoint,
                timeout=5,
                verify=True  # SSL verification enabled — good practice
            )
            self.status = "healthy" if response.status_code == 200 else "degraded"
            self.last_check = datetime.now()
            return {
                "service": self.service_name,
                "status": self.status,
                "response_time_ms": response.elapsed.total_seconds() * 1000,
                "checked_at": self.last_check.isoformat()
            }
        except requests.exceptions.Timeout:
            self.status = "timeout"
        except requests.exceptions.ConnectionError:
            self.status = "unreachable"
        return {"service": self.service_name, "status": self.status}


# SEC INFRA-005: HTTP URL — should be HTTPS
# Metrics reporting endpoint uses plain HTTP
METRICS_ENDPOINT = "http://internal-metrics.devops.company.com/push"


def push_metrics(metrics_data):
    """Push collected metrics to central aggregator"""
    # SEC: Sending metrics over unencrypted HTTP
    response = requests.post(
        METRICS_ENDPOINT,
        json=metrics_data,
        timeout=10
    )
    return response.status_code == 200


class ServiceRegistry:
    """Registry of all monitored services"""

    def __init__(self):
        self.services = {}

    def register(self, name, endpoint, check_interval=30):
        """Register a service for monitoring"""
        self.services[name] = {
            "endpoint": endpoint,
            "interval": check_interval,
            "checker": HealthChecker(name, endpoint)
        }

    def check_all(self):
        """Run health checks on all registered services"""
        results = []
        for name, config in self.services.items():
            result = config["checker"].check()
            results.append(result)
        return results

    def get_status_summary(self):
        """Get overall platform health summary"""
        all_results = self.check_all()
        healthy = sum(1 for r in all_results if r.get("status") == "healthy")
        total = len(all_results)
        return {
            "healthy": healthy,
            "total": total,
            "percentage": round((healthy / total * 100) if total > 0 else 0, 1)
        }

"""
Monitoring Data Models
Stores health check results and alert history
"""


class ServiceStatus:
    """Represents current status of a monitored service"""
    service_id: str
    service_name: str
    endpoint_url: str
    current_status: str   # healthy, degraded, timeout, unreachable
    last_checked: str
    uptime_percentage: float
    avg_response_time_ms: float
    environment: str      # production, staging, development


class Alert:
    """Alert generated when service crosses threshold"""
    alert_id: str
    service_id: str
    alert_type: str       # cpu_high, memory_high, service_down, slow_response
    severity: str         # critical, high, medium, low
    message: str
    triggered_at: str
    resolved_at: str
    is_resolved: bool
    notified_channels: list


class DeploymentEvent:
    """Records deployment events for correlation with issues"""
    event_id: str
    service_name: str
    version: str
    deployed_by: str
    deployed_at: str
    environment: str
    git_commit: str
    deployment_status: str  # success, failed, rolled_back
    notes: str

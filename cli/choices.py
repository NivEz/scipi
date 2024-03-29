CHOICES = {
    'portainer': {
        'display_value': 'Portainer',
        'short_name': 'Portainer',
        'directory': 'portainer',
        'script': './install.sh'
    },
    'twingate': {
        'display_value': 'Twingate (Zero Trust)',
        'short_name': 'Twingate',
        'directory': 'twingate',
        'script': './setup.sh'
    },
    'pihole': {
        'display_value': 'Pi-hole',
        'short_name': 'Pi-hole',
        'directory': 'pi-hole',
        'script': './install.sh'
    },
    'nginx_proxy_manager': {
        'display_value': 'Nginx Proxy Manager',
        'short_name': 'Nginx Proxy Manager',
        'directory': 'nginx-proxy-manager',
        'script': './install.sh'
    },
    'shut_down_container': {
        'display_value': 'Remote shut down container (not implemented yet)',
        'short_name': 'Shut down container',
        'directory': 'manager',
        'script': ''
    },
    'monitoring': {
        'display_value': 'Monitoring tools (Prometheus + Grafana) (not implemented yet)',
        'short_name': 'Monitoring tools',
        'directory': 'monitoring',
        'script': ''
    }
}

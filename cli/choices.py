CHOICES = {
    'portainer': {
        'display_value': 'Portainer',
        'short_name': 'Portainer',
        'directory': 'portainer',
        'script': './install.sh'
    },
    'pihole': {
        'display_value': 'Pi-hole',
        'short_name': 'Pi-hole',
        'directory': 'pi-hole',
        'script': './install.sh'
    },
    'twingate': {
        'display_value': 'Twingate (Zero Trust)',
        'short_name': 'Twingate',
        'directory': 'terraform',
        'script': './setup.sh'
    },
    'shut_down_container': {
        'display_value': 'Remote shut down container',
        'short_name': 'Shut down container',
        'directory': 'manager',
        'script': ''
    },
    'monitoring': {
        'display_value': 'Monitoring tools (Prometheus + Grafana)',
        'short_name': 'Monitoring tools',
        'directory': 'monitoring',
        'script': ''
    }
}

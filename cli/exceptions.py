class DockerInstallFailed(Exception):
    def __init__(self, message="Docker installation failed"):
        self.message = message
        super().__init__(self.message)


class InvalidIpAddress(Exception):
    def __init__(self, ip):
        message = f"Invalid IP address: {ip}"
        super().__init__(message)


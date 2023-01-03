class DockerInstallFailed(Exception):
    def __init__(self, message="Docker installation failed"):
        self.message = message
        super().__init__(self.message)

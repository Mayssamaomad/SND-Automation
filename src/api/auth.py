class AuthHandler:
    def __init__(self, config: dict):
        self.token = config.get("token")
        self.username = config.get("username")
        self.password = config.get("password")

        self.headers = {
            "Content-Type": "application/json"
        }

        if self.token:
            self.headers["Authorization"] = f"Bearer {self.token}"

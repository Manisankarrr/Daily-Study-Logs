# Abstraction - Reduce complexity by hiding unnecessary details

class EmailService:
    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating...")
        
    def _disconnect(self):
        print("disconnecting email...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("sending email...")
        self._disconnect()

email = EmailService()
email.send_email()

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Ensure only one instance is created
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize logger settings (called only once)
        if not hasattr(self, '_initialized'):
            self.log_messages = []
            self._initialized = True

    def log(self, message):
        # Log a message
        self.log_messages.append(message)

    def get_logs(self):
        # Get the list of logged messages
        return self.log_messages


# Example Usage
logger1 = Logger()
logger2 = Logger()

# Both instances refer to the same object
print(logger1 is logger2)  # Output: True

# Logging messages
logger1.log("Error: File not found")
logger2.log("Info: Application started")
logger1.log("Warning: Low disk space")

# Retrieving logged messages
print(logger1.get_logs())
# Output: ["Error: File not found", "Info: Application started", "Warning: Low disk space"]

class LincolnLayer:
    """A layer in a lincoln log structure, which can contain multiple Lincoln Logs."""
    def __init__(self):
       self.logs = []

    def add_log(self, log):
       """Add a Lincoln Log to the layer."""
       self.logs.append(log)

    def __str__(self):
       return f"Layer with {len(self.logs)} log(s): " + ", ".join(str(log) for log in self.logs)
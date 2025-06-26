"""Module for defining a Lincoln Layer and its associated methods."""
class LincolnLayer:
    """A layer in a lincoln log structure, which can contain multiple Lincoln Logs."""
    def __init__(self):
       self.logs = []

    def add_log(self, log):
       """Add a Lincoln Log to the layer."""
       self.logs.append(log)

    def __str__(self):
       """String representation of the Lincoln Layer, showing the logs it contains."""
       return f"Layer with {len(self.logs)} log(s): " + ", ".join(str(log) for log in self.logs)

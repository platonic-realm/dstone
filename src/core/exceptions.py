"""
Custom exceptions for DStone.
"""


class DependencyError(Exception):
    """
    Exception raised for errors in the plugin dependency system.

    Attributes:
        plugin (str): Name of the plugin with the dependency issue.
        dependency (str): Name of the dependency causing the issue.
        message (str): Explanation of the error.
    """

    def __init__(self, plugin: str, dependency: str):
        self.plugin = plugin
        self.dependency = dependency
        self.message = f"DependencyError for plugin: '{self.plugin}' - Dependency: '{self.dependency}')"
        super().__init__(self.message)

    def __str__(self):
        return self.message

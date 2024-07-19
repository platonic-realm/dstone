"""
Dummy Plugin

This module initializes the DummyPlugin and provides metadata for the plugin manager.
"""

from .dummy import DummyPlugin

# Metadata for the plugin manager
plugin_name = "dummy"
plugin_version = "1.0"
plugin_description = "A template plugin for demonstration"

# The plugin class to be loaded by the plugin manager
plugin_class = DummyPlugin

# You can add any other metadata that might be useful for your plugin manager
plugin_author = "Your Name"
plugin_license = "MIT"
plugin_dependencies = []  # List any other plugins this one depends on


# Optional: A function to validate the plugin's configuration
# def validate_config(config):
#     """
#     Validate the configuration for the DummyPlugin.
#
#     Args:
#         config (dict): The configuration to validate.
#
#     Returns:
#         bool: True if the configuration is valid, False otherwise.
#     """
#     # Add your configuration validation logic here
#     return True


# Optional: A function to get default configuration values
# def get_default_config():
#     """
#     Get the default configuration for the DummyPlugin.
#
#     Returns:
#         dict: The default configuration.
#     """
#     return {
#         "example_setting": "default_value"
#     }

"""
Base Plugin Module
==================

This module defines the BasePlugin class, which serves as a foundation for creating plugins
in a plugin system where the core API handles session management.
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional


@dataclass
class BasePlugin(ABC):
    """
    A base class for plugins in a plugin system with core API session management.

    This class provides a foundation for creating plugins with common attributes and methods.
    It uses the dataclass decorator for automatic generation of __init__, __repr__, and __eq__ methods.

    Attributes:
        name (str): The name of the plugin.
        version (str): The version of the plugin.
        description (str): A brief description of the plugin's purpose and functionality.
        aliases (List[str]): Alternative names for the plugin.
        priority (int): The priority of the plugin in the system.
        dependencies (List[str]): Names of other plugins this plugin depends on.
        sessionable (bool): Whether the plugin can maintain session state.
        initialized (bool): Whether the plugin has been initialized.
        app: The application object providing core functionalities.
    """

    name: str
    version: str
    description: str
    aliases: List[str] = field(default_factory=list)
    priority: int = 0
    dependencies: List[str] = field(default_factory=list)
    sessionable: bool = False
    initialized: bool = False
    app: Any = field(default=None)

    @abstractmethod
    def initialize(self, config: Dict[str, Any]) -> None:
        """
        Initialize the plugin with the given configuration.

        Args:
            config (Dict[str, Any]): Configuration dictionary for the plugin.
        """
        pass

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the main functionality of the plugin.

        The session data, if needed, should be accessed through the app object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Any: The result of the plugin execution.
        """
        pass

    @abstractmethod
    def cleanup(self) -> None:
        """
        Perform any necessary cleanup operations.
        """
        pass

    def get_info(self) -> Dict[str, Any]:
        """
        Return basic information about the plugin.

        Returns:
            Dict[str, Any]: A dictionary containing plugin information.
        """
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "aliases": self.aliases,
            "priority": self.priority,
            "dependencies": self.dependencies,
            "sessionable": self.sessionable,
            "initialized": self.initialized
        }

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Return a list of capabilities supported by the plugin.

        Returns:
            List[str]: A list of capability strings.
        """
        pass

    @abstractmethod
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate the configuration for the plugin.

        Args:
            config (Dict[str, Any]): Configuration dictionary to validate.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        pass

    def __enter__(self):
        """
        Enter the runtime context for the plugin.

        Raises:
            RuntimeError: If the plugin is not initialized.

        Returns:
            BasePlugin: The plugin instance.
        """
        if not self.initialized:
            raise RuntimeError("Plugin must be initialized before use.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context for the plugin.

        Args:
            exc_type: The exception type, if any.
            exc_val: The exception value, if any.
            exc_tb: The exception traceback, if any.
        """
        self.cleanup()

    @classmethod
    def create(cls,
               name: str,
               version: str,
               description: str,
               app: Any,
               aliases: List[str] = None,
               priority: int = 0,
               dependencies: List[str] = None,
               sessionable: bool = False,
               config: Optional[Dict[str, Any]] = None) -> 'BasePlugin':
        """
        Factory method to create and initialize a plugin instance.

        Args:
            name (str): The name of the plugin.
            version (str): The version of the plugin.
            description (str): A brief description of the plugin.
            app (Any): The application object providing core functionalities.
            aliases (List[str], optional): Alternative names for the plugin.
            priority (int, optional): The priority of the plugin.
            dependencies (List[str], optional): Names of other plugins this plugin depends on.
            sessionable (bool, optional): Whether the plugin can maintain session state.
            config (Dict[str, Any], optional): Configuration dictionary for initialization.

        Returns:
            BasePlugin: An instance of the plugin.
        """
        plugin = cls(name,
                     version,
                     description,
                     aliases,
                     priority,
                     dependencies,
                     sessionable,
                     app=app)
        if config:
            plugin.initialize(config)
        return plugin

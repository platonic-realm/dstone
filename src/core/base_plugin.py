"""
Base Plugin Module
==================

This module defines the BasePlugin class, which serves as a foundation for creating plugins
in the DStone application. It provides a streamlined interface for plugin development.
"""

# Python Imports
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Callable

# Local Imports
from src.api.utils.logging import get_plugin_logger


@dataclass
class BasePlugin(ABC):
    """
    A base class for plugins in the DStone application.

    This class provides a foundation for creating plugins with common attributes and methods.
    It uses the dataclass decorator for automatic generation of __repr__ and __eq__ methods.

    Attributes:
        name (str): The name of the plugin.
        version (str): The version of the plugin.
        description (str): A brief description of the plugin's purpose and functionality.
        app (Any): The application object providing core functionalities.
        aliases (List[str]): Alternative names for the plugin.
        priority (int): The priority of the plugin in the system.
        dependencies (List[str]): Names of other plugins this plugin depends on.
        sessionable (bool): Whether the plugin can maintain session state.
        initialized (bool): Whether the plugin has been initialized.
    """

    name: str
    version: str
    description: str
    app: Any
    aliases: List[str] = field(default_factory=list)
    priority: int = 0
    dependencies: List[str] = field(default_factory=list)
    sessionable: bool = False
    initialized: bool = False

    def __init__(self,
                 name: str,
                 version: str,
                 description: str,
                 app: Any,
                 aliases: List[str] = None,
                 priority: int = 0,
                 dependencies: List[str] = None,
                 sessionable: bool = False):
        """
        Initialize the plugin.

        Args:
            name (str): The name of the plugin.
            version (str): The version of the plugin.
            description (str): A brief description of the plugin's purpose.
            app (Any): The main application object, providing access to shared resources.
            aliases (List[str], optional): Alternative names for the plugin.
            priority (int, optional): The priority of the plugin in the system.
            dependencies (List[str], optional): Names of other plugins this plugin depends on.
            sessionable (bool, optional): Whether the plugin can maintain session state.
        """
        self.name = name
        self.version = version
        self.description = description
        self.app = app
        self.aliases = aliases or []
        self.priority = priority
        self.dependencies = dependencies or []
        self.sessionable = sessionable
        self.logger = get_plugin_logger(self.name)

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any) -> Any:
        """
        Execute the main functionality of the plugin.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Any: The result of the plugin execution.
        """
        pass

    @abstractmethod
    def setup_ui(self) -> None:
        """
        Set up the user interface for the plugin.
        This method should be implemented by subclasses to create any UI components.
        """
        pass

    def attach(self, on_attach: Callable[[], None]) -> None:
        """
        Attach the plugin to the application.

        Args:
            on_attach (Callable[[], None]): Callback function to be called when the plugin is attached.
        """
        on_attach()

    def detach(self, on_detach: Callable[[], None]) -> None:
        """
        Detach the plugin from the application.

        Args:
            on_detach (Callable[[], None]): Callback function to be called when the plugin is detached.
        """
        on_detach()

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
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """
        Validate the configuration for the plugin.

        Args:
            config (Dict[str, Any]): Configuration dictionary to validate.

        Returns:
            bool: True if the configuration is valid, False otherwise.
        """
        pass

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
                     app, aliases,
                     priority,
                     dependencies,
                     sessionable)
        if config and plugin.validate_config(config):
            # Apply configuration if provided and valid
            pass  # TODO: Apply configuration
        return plugin

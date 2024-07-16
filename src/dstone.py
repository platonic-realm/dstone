"""
DStone Module
=============

This module defines the DStone class, which is responsible for plugin management
and providing the basic UI framework using Dash.
"""

# Python Imports
import os
import importlib
import inspect
from typing import Dict, Any

# Library Imports
import dash
import dash_bootstrap_components as dbc
from dash import html

# Local Imports
from src.core.base_plugin import BasePlugin
from src.core.exceptions import DependencyError


class DStone:
    """
    DStone (Deep Stone) class for managing plugins and providing a UI framework.

    This class handles plugin discovery, registration, loading, and execution. It also sets up
    the basic UI structure using Dash.
    """

    def __init__(self, plugins_dir):
        self.plugins: Dict[str, BasePlugin] = {}
        self.discover_plugins(plugins_dir)

        self.app = dash.Dash(
            __name__,
            suppress_callback_exceptions=True,
            external_stylesheets=[dbc.themes.CYBORG, dbc.icons.FONT_AWESOME],
            add_log_handler=False,
        )

        self.setup_ui()

    def discover_plugins(self, plugin_dir: str) -> None:
        """
        Discover plugins in the specified directory.

        Args:
            plugin_dir (str): The directory to search for plugins.
        """
        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py') and not filename.startswith('__'):
                module_name = filename[:-3]
                module = importlib.import_module(f'plugins.{module_name}')
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, BasePlugin) and obj != BasePlugin:
                        self.register_plugin(obj)

    def register_plugin(self, plugin_class: type) -> None:
        """
        Register a plugin with DStone.

        Args:
            plugin_class (type): The class of the plugin to register.
        """
        plugin_instance = plugin_class.create(
            name=plugin_class.__name__,
            version=getattr(plugin_class, 'version', '0.1'),
            description=getattr(plugin_class, 'description', 'No description provided'),
            app=self
        )
        self.plugins[plugin_instance.name] = plugin_instance

    def load_plugin(self, plugin_name: str) -> None:
        """
        Load a registered plugin and check its dependencies.

        Args:
            plugin_name (str): The name of the plugin to load.

        Raises:
            ValueError: If the plugin is not found.
            DependencyError: If a dependency cannot be satisfied.
        """
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin {plugin_name} not found")

        plugin = self.plugins[plugin_name]

        # Check dependencies
        for dependency in plugin.dependencies:
            if dependency not in self.plugins:
                raise DependencyError(f"Dependency {dependency} for plugin {plugin_name} not found")
            if not self.plugins[dependency].initialized:
                self.load_plugin(dependency)  # Recursively load dependencies

        plugin.initialize({})  # You might want to pass actual config here
        plugin.initialized = True

    def load_all_plugins(self) -> None:
        """
        Load all registered plugins, respecting dependencies.
        """
        for plugin_name in self.plugins:
            if not self.plugins[plugin_name].initialized:
                self.load_plugin(plugin_name)

    def execute_plugins(self) -> None:
        """
        Execute all loaded plugins, respecting dependencies and priorities.
        """
        # Sort plugins by priority (lower number = higher priority)
        sorted_plugins = sorted(self.plugins.values(), key=lambda x: x.priority)

        executed = set()

        def execute_with_dependencies(plugin):
            if plugin.name in executed:
                return

            # Execute dependencies first
            for dep_name in plugin.dependencies:
                dep_plugin = self.plugins[dep_name]
                execute_with_dependencies(dep_plugin)

            # Execute the plugin
            plugin.execute()
            executed.add(plugin.name)

        # Execute plugins in order of priority
        for plugin in sorted_plugins:
            execute_with_dependencies(plugin)

    def setup_ui(self) -> None:
        """
        Set up the basic UI structure using Dash.
        """
        # TODO: Implement the base UI setup here

        sidebar = html.Div(
            [
                html.Div(
                    [
                        html.Img(src=self.app.get_asset_url("logo.png"), alt="logo", width="80%",),
                    ],
                    className="sidebar-header",
                ),
                html.Hr(),
                dbc.Nav(
                    [
                        dbc.NavLink(
                            [html.I(className="fas fa-home me-2"), html.Span("Dashboard")],
                            href="/",
                            active="exact",
                        ),
                        dbc.NavLink(
                            [
                                html.I(className="fas fa-calendar-alt me-2"),
                                html.Span("Projects"),
                            ],
                            href="/projects",
                            active="exact",
                        ),
                        dbc.NavLink(
                            [
                                html.I(className="fas fa-envelope-open-text me-2"),
                                html.Span("Datasets"),
                            ],
                            href="/datasets",
                            active="exact",
                        ),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            className="sidebar",
        )

        self.app.layout = html.Div(
            [
                sidebar,
                html.Div(
                    [
                        dash.page_container
                    ],
                    className="content",
                ),
            ]
        )

    def run(self,
            debug: bool = False,
            port: int = 8050,
            reload: bool = False) -> None:
        """
        Run the DStone application.

        Args:
            debug (bool): Whether to run in debug mode.
            port (int): The port to run the application on.
            reload (bool): Whether enable hot reloading.
        """
        self.load_all_plugins()
        self.execute_plugins()
        self.app.run_server(debug=debug, port=port, use_reloader=reload)

    # Session management methods
    def get_session_data(self, plugin_name: str) -> Dict[str, Any]:
        """
        Get session data for a specific plugin.

        Args:
            plugin_name (str): The name of the plugin.

        Returns:
            Dict[str, Any]: The session data for the plugin.
        """
        # TODO: Implement session data retrieval
        # This should interact with session management system
        pass

    def set_session_data(self, plugin_name: str, data: Dict[str, Any]) -> None:
        """
        Set session data for a specific plugin.

        Args:
            plugin_name (str): The name of the plugin.
            data (Dict[str, Any]): The session data to set.
        """
        # TODO: Implement session data setting
        # This should interact with session management system
        pass

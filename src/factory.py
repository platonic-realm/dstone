"""
Factory Module for DStone Application

This module provides factory functions for creating various components and instances
required by the DStone application. It centralizes the instantiation logic, making
it easier to manage dependencies and configurations across the application.
"""

# Python Imports
import logging
from typing import Dict, Any
from pathlib import Path

# Local Imports
from src.dstone import DStone


def create_dstone_instance(configs: Dict[str, Any], dstone_root: Path) -> DStone:
    """
    Create and configure a DStone instance based on the provided configuration.

    This function handles the setup of the DStone instance, including:
    - Configuring the plugins directory
    - Initializing the DStone object

    Args:
        configs (Dict[str, Any]): The application configuration dictionary.
        dstone_root (Path): The root path of dstone project.

    Returns:
        DStone: A fully configured DStone instance ready for use.

    Raises:
    """

    # Get logger for this module
    logger = logging.getLogger(__name__)

    plugins_dir = dstone_root / 'src' / 'plugins'
    assets_dir = dstone_root / 'assets'

    # Create a DStone instance (which will discover plugins during initialization)
    logger.info("Initializing DStone and discovering plugins...")
    dstone = DStone(str(plugins_dir),
                    str(assets_dir))

    # Log discovered plugins
    for plugin_name, plugin in dstone.plugins.items():
        logger.info(f"Discovered plugin: {plugin_name} (v{plugin.version}): {plugin.description}")

    return dstone

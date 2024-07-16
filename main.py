"""
Main entry point for the DStone application.

This script initializes the DStone instance and runs the application.
"""

# Python Imports
import sys

# Local Imports
from src.dstone import DStone, DependencyError
from src.api.utils.logging import get_main_logger
from src.api.io.fs import get_project_root, create_directory


def main(debug: bool, reload: bool):
    # Basic configuratoins
    logger = get_main_logger('INFO')

    root_dir = get_project_root()
    plugins_dir = root_dir / 'src' / 'plugins'
    create_directory(plugins_dir)

    # Create a DStone instance (which will discover plugins during initialization)
    logger.info("Initializing DStone and discovering plugins...")
    dstone = DStone(str(plugins_dir))

    logger.info("Discovered plugins:")
    for plugin_name, plugin in dstone.plugins.items():
        logger.info(f"- {plugin_name} (v{plugin.version}): {plugin.description}")

    # Attempt to load and run the application
    try:
        logger.info("Starting the application...")
        dstone.run(debug=debug, reload=reload)
    except DependencyError as e:
        logger.info(f"Dependency Error: {e}")
        sys.exit(1)
    except Exception as e:
        logger.info(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # TODO: Implement a config manager and pass it to main to configure the app
    main(debug=True, reload=False)

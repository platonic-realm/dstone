"""
Main entry point for the DStone application.

This script initializes the DStone instance and runs the application.
"""

# Change the caching directory
import sys
sys.pycache_prefix = "/tmp/dstone/"

# Python Imports
import yaml
import logging
from pathlib import Path

# Local Imports
from src import factory
from src.core.exceptions import DependencyError
from src.api.utils.logging import configure_main_logger
from src.api.io.fs import get_project_root


def dstone_main(configs: dict, dstone_root: Path):

    logger = logging.getLogger(__name__)

    dstone = factory.create_dstone_instance(configs, dstone_root)

    logger.info("Starting the application.")
    dstone.run(debug=configs['dstone']['debug'],
               reload=configs['dstone']['reload'])


if __name__ == "__main__":

    configure_main_logger('INFO')
    logger = logging.getLogger(__name__)

    # Load dstone configuratoins
    dstone_root = get_project_root()
    config_path = dstone_root / 'config.yml'
    with open(config_path, 'r') as config_file:
        configs = yaml.safe_load(config_file)

    try:
        dstone_main(configs, dstone_root)

    except DependencyError as e:
        logger.error(f"Dependency Error: {e}")
        sys.exit(1)

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

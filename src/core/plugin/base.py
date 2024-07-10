from abc import ABC, abstractmethod


class BasePlugin(ABC):
    @abstractmethod
    def name(self) -> str:
        """Return the name of the plugin."""
        pass

    @abstractmethod
    def description(self) -> str:
        """Return a description of the plugin."""
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        """Main method to run the plugin's functionality."""
        pass

    @abstractmethod
    def get_ui_component(self):
        """Return a Dash component for the plugin's UI."""
        pass

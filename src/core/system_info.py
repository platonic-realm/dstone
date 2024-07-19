"""
SystemInfo Class Module

This module defines a SystemInfo class that gathers system information at initialization
and provides access to this data using the [] operator. It collects information about
the CPU, memory, operating system, and infrastructure (environment type).

Classes:
    SystemInfo: A class to collect and store system information.

Usage:
    sys_info = SystemInfo()
    cpu_info = sys_info['cpu']
    mem_info = sys_info['mem']
    os_info = sys_info['os']
    infra_info = sys_info['infra']
"""

# Python Imports
import psutil
import platform
import subprocess
from typing import Dict, Any

# Local Imports
from src.api.utils.bytes import bytes_to_human_readable


class SystemInfo:
    """
    A class to collect and store system information.

    This class gathers information about the system's CPU, memory, operating system,
    and infrastructure (environment type) upon initialization. The information can be
    accessed using dictionary-like syntax with the [] operator.

    Attributes:
        info (Dict[str, Any]): A dictionary containing all gathered system information.

    Methods:
        __getitem__(key): Allows accessing information using dictionary-like syntax.
    """

    def __init__(self):
        """
        Initialize the SystemInfo instance and gather all system information.
        """
        self.info = {
            'cpu': self._get_cpu_info(),
            'mem': self._get_memory_info(),
            'os': self._get_os_info(),
            'infra': self._get_infrastructure_info(),
        }

    def __getitem__(self, key):
        """
        Allow accessing system information using dictionary-like syntax.

        Args:
            key (str): The key for the desired information ('cpu', 'mem', 'os', or 'infra').

        Returns:
            Any: The requested information, or None if the key is not found.
        """
        return self.info.get(key, None)

    def _get_cpu_info(self) -> Dict[str, Any]:
        """
        Get CPU information.

        Returns:
            Dict[str, Any]: A dictionary containing CPU information including:
                - pcores: Number of physical cores
                - lcores: Number of logical cores
                - max_freq: Maximum CPU frequency (if available)
                - model: CPU model information
        """
        return {
            "pcores": psutil.cpu_count(logical=False),
            "lcores": psutil.cpu_count(logical=True),
            "max_freq": psutil.cpu_freq().max if hasattr(psutil.cpu_freq(), 'max') else None,
            "model": platform.processor()
        }

    def _get_memory_info(self) -> Dict[str, Any]:
        """
        Get memory information.

        Returns:
            Dict[str, Any]: A dictionary containing memory information including:
                - total: Total physical memory in bytes
                - human_readable: Total physical memory in a human-readable format
        """
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "human_readable": bytes_to_human_readable(mem.total),
        }

    def _get_os_info(self) -> Dict[str, Any]:
        """
        Get detailed operating system information.

        Returns:
            Dict[str, Any]: A dictionary containing OS information including:
                - system: OS name (e.g., 'Linux', 'Windows', 'Darwin')
                - release: OS release information
                - version: OS version
                - architecture: System architecture
                - node: Network node hostname
                - platform: A single string containing OS information
                - libc_version: libc version (Linux only)
                - distro: Linux distribution information (Linux only)
        """
        os_info = {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "architecture": platform.architecture(),
            "node": platform.node(),
            "platform": platform.platform(),
        }
        if os_info["system"] == "Linux":
            os_info["libc_version"] = platform.libc_ver()
            os_info["distro"] = self._get_linux_distro()
        elif os_info["system"] == "Windows":
            # TODO: Add Windows-specific code
            pass
        elif os_info["system"] == "Darwin":
            # TODO: Add macOS-specific code
            pass
        return os_info

    def _get_linux_distro(self) -> str:
        """
        Get Linux distribution information.

        This method tries multiple approaches to determine the Linux distribution:
        1. Using the 'distro' library
        2. Reading from /etc/os-release file
        3. Using the 'lsb_release' command

        Returns:
            str: A string containing the Linux distribution information, or "Unknown" if unable to determine.
        """
        try:
            import distro
            return f"{distro.name()} {distro.version()} {distro.codename()}"
        except ImportError:
            try:
                with open("/etc/os-release") as f:
                    lines = f.readlines()
                info = dict(line.strip().split("=", 1) for line in lines if "=" in line)
                return f"{info.get('NAME', 'Unknown')} {info.get('VERSION', '')}"
            except FileNotFoundError:
                try:
                    result = subprocess.run(['lsb_release', '-ds'], capture_output=True, text=True)
                    return result.stdout.strip()
                except (FileNotFoundError, subprocess.SubprocessError):
                    return "Unknown"

    def _get_infrastructure_info(self) -> Dict[str, Any]:
        """
        Determine the type of environment (HPC, Cloud, or Local).

        Returns:
            Dict[str, Any]: A dictionary containing infrastructure information including:
                - category: The type of environment ('HPC', 'Cloud', or 'Local')
                - details: Additional details about the environment (for HPC and Cloud)
        """
        # TODO: Implement detection for HPC and Cloud environments
        if self._is_hpc():
            return {"category": "HPC", "details": self._get_hpc_details()}
        elif self._is_cloud():
            return {"category": "Cloud", "details": self._get_cloud_details()}
        else:
            return {"category": "Local"}

    def _is_hpc(self) -> bool:
        """
        Check if running in an HPC environment.

        TODO: Implement detection for HPC environments (e.g., checking for the presence of job schedulers like SLURM).

        Returns:
            bool: True if running in an HPC environment, False otherwise.
        """
        return False

    def _get_hpc_details(self) -> Dict[str, str]:
        """
        Get details about the HPC environment.

        TODO: Implement gathering of HPC-specific details (e.g., cluster name, job ID, allocated resources).

        Returns:
            Dict[str, str]: A dictionary containing HPC-specific details.
        """
        return {}

    def _is_cloud(self) -> bool:
        """
        Check if running in a cloud environment.

        TODO: Implement detection for cloud environments (e.g., checking for cloud-specific metadata services).

        Returns:
            bool: True if running in a cloud environment, False otherwise.
        """
        return False

    def _get_cloud_details(self) -> Dict[str, str]:
        """
        Get details about the cloud environment.

        TODO: Implement gathering of cloud-specific details (e.g., cloud provider, instance type, region).

        Returns:
            Dict[str, str]: A dictionary containing cloud-specific details.
        """
        return {}

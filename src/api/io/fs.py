"""
Expanded File System Operations Module

This module provides a comprehensive set of file and directory operations for the DStone API.
It includes functions for file and directory manipulation, as well as advanced search capabilities.
"""

import os
import shutil
from pathlib import Path
from typing import List, Union, Callable, Iterator
import fnmatch


def get_project_root() -> Path:
    """
    Get the root directory of the project.

    This function traverses up the directory tree from the current file
    until it finds a directory containing a '.git' folder or a 'src' folder,
    which is assumed to be the project root.

    Returns:
        Path: The path to the project root directory.

    Raises:
        FileNotFoundError: If the project root cannot be determined.
    """
    current_path = Path(__file__).resolve().parent
    while current_path != current_path.parent:
        if (current_path / '.git').exists() or (current_path / 'src').exists():
            return current_path
        current_path = current_path.parent

    raise FileNotFoundError("Could not determine the project root directory.")


def list_files(directory: Union[str, Path], extension: str = None) -> List[str]:
    """
    List all files in a directory, optionally filtering by extension.

    Args:
        directory (Union[str, Path]): The directory to list files from.
        extension (str, optional): File extension to filter by. Defaults to None.

    Returns:
        List[str]: A list of file names in the directory.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    path = Path(directory)
    if not path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    if extension:
        return [f.name for f in path.glob(f'*.{extension}')]
    return [f.name for f in path.glob('*') if f.is_file()]


def delete_file(path: Union[str, Path]) -> None:
    """
    Delete a file.

    Args:
        path (Union[str, Path]): The path of the file to delete.

    Raises:
        FileNotFoundError: If the file does not exist.
        OSError: If the file cannot be deleted.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    file_path.unlink()


def copy_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """
    Copy a file from source to destination.

    Args:
        src (Union[str, Path]): The path of the source file.
        dst (Union[str, Path]): The path of the destination file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        OSError: If the file cannot be copied.
    """
    shutil.copy2(src, dst)


def move_file(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """
    Move a file from source to destination.

    Args:
        src (Union[str, Path]): The path of the source file.
        dst (Union[str, Path]): The path of the destination file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        OSError: If the file cannot be moved.
    """
    shutil.move(src, dst)


def get_file_size(path: Union[str, Path]) -> int:
    """
    Get the size of a file in bytes.

    Args:
        path (Union[str, Path]): The path of the file.

    Returns:
        int: The size of the file in bytes.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return file_path.stat().st_size


def read_text_file(path: Union[str, Path], encoding: str = 'utf-8') -> str:
    """
    Read the contents of a text file.

    Args:
        path (Union[str, Path]): The path of the file to read.
        encoding (str, optional): The encoding of the file. Defaults to 'utf-8'.

    Returns:
        str: The contents of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file cannot be read.
    """
    with open(path, 'r', encoding=encoding) as file:
        return file.read()


def write_text_file(path: Union[str, Path], content: str, encoding: str = 'utf-8') -> None:
    """
    Write content to a text file.

    Args:
        path (Union[str, Path]): The path of the file to write.
        content (str): The content to write to the file.
        encoding (str, optional): The encoding to use. Defaults to 'utf-8'.

    Raises:
        IOError: If the file cannot be written.
    """
    with open(path, 'w', encoding=encoding) as file:
        file.write(content)


def get_file_extension(path: Union[str, Path]) -> str:
    """
    Get the extension of a file.

    Args:
        path (Union[str, Path]): The path of the file.

    Returns:
        str: The file extension (without the dot) or an empty string if there's no extension.
    """
    return Path(path).suffix[1:]  # [1:] to remove the leading dot


def get_file_stem(path: Union[str, Path]) -> str:
    """
    Get the stem (filename without extension) of a file.

    Args:
        path (Union[str, Path]): The path of the file.

    Returns:
        str: The stem of the file.

    Example:
        >>> get_file_stem('/path/to/file.txt')
        'file'
        >>> get_file_stem('document.pdf')
        'document'
        >>> get_file_stem('image.with.multiple.dots.jpg')
        'image.with.multiple.dots'
    """
    return Path(path).stem


def get_file_directory(path: Union[str, Path]) -> str:
    """
    Get the directory of a file.

    Args:
        path (Union[str, Path]): The path of the file.

    Returns:
        str: The directory containing the file.

    Example:
        >>> get_file_directory('/path/to/file.txt')
        '/path/to'
        >>> get_file_directory('document.pdf')
        '.'
        >>> get_file_directory('/home/user/documents/report.docx')
        '/home/user/documents'
    """
    return str(Path(path).parent)


def create_directory(path: Union[str, Path]) -> None:
    """Create a directory if it doesn't exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def delete_directory(path: Union[str, Path], recursive: bool = False) -> None:
    """
    Delete a directory.

    Args:
        path (Union[str, Path]): The path of the directory to delete.
        recursive (bool): If True, recursively delete subdirectories. Defaults to False.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: If the directory cannot be deleted.
    """
    dir_path = Path(path)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {path}")
    if recursive:
        shutil.rmtree(dir_path)
    else:
        dir_path.rmdir()


def list_directories(path: Union[str, Path]) -> List[str]:
    """
    List all subdirectories in a given directory.

    Args:
        path (Union[str, Path]): The path of the directory to list subdirectories from.

    Returns:
        List[str]: A list of subdirectory names.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    dir_path = Path(path)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {path}")
    return [d.name for d in dir_path.iterdir() if d.is_dir()]


def is_directory_empty(path: Union[str, Path]) -> bool:
    """
    Check if a directory is empty.

    Args:
        path (Union[str, Path]): The path of the directory to check.

    Returns:
        bool: True if the directory is empty, False otherwise.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    dir_path = Path(path)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {path}")
    return not any(dir_path.iterdir())


def copy_directory(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """
    Copy a directory and its contents to a new location.

    Args:
        src (Union[str, Path]): The path of the source directory.
        dst (Union[str, Path]): The path of the destination directory.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        OSError: If the directory cannot be copied.
    """
    shutil.copytree(src, dst)


def move_directory(src: Union[str, Path], dst: Union[str, Path]) -> None:
    """
    Move a directory and its contents to a new location.

    Args:
        src (Union[str, Path]): The path of the source directory.
        dst (Union[str, Path]): The path of the destination directory.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        OSError: If the directory cannot be moved.
    """
    shutil.move(src, dst)


def get_directory_size(path: Union[str, Path]) -> int:
    """
    Get the total size of a directory and its contents in bytes.

    Args:
        path (Union[str, Path]): The path of the directory.

    Returns:
        int: The total size of the directory in bytes.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    dir_path = Path(path)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {path}")
    return sum(f.stat().st_size for f in dir_path.glob('**/*') if f.is_file())


def recursive_search(directory: Union[str, Path],
                     filter_func: Callable[[Path], bool] = None) -> Iterator[Path]:
    """
    Recursively search a directory and yield paths that match the filter function.

    Args:
        directory (Union[str, Path]): The directory to search.
        filter_func (Callable[[Path], bool], optional): A function that takes a Path object
            and returns True if the path should be included in the results.
            If None, all paths are included. Defaults to None.

    Yields:
        Iterator[Path]: An iterator of Path objects that match the filter.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    dir_path = Path(directory)
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    for root, _, files in os.walk(dir_path):
        for file in files:
            file_path = Path(root) / file
            if filter_func is None or filter_func(file_path):
                yield file_path

# Existing functions (list_files, delete_file, copy_file, move_file, get_file_size,
# read_text_file, write_text_file, get_file_extension) remain the same

# Example filter functions for recursive_search


def filter_by_extension(extension: str) -> Callable[[Path], bool]:
    """
    Create a filter function that matches files with a specific extension.

    Args:
        extension (str): The file extension to match (without the dot).

    Returns:
        Callable[[Path], bool]: A filter function for use with recursive_search.
    """
    return lambda path: path.suffix.lower() == f'.{extension.lower()}'


def filter_by_name_pattern(pattern: str) -> Callable[[Path], bool]:
    """
    Create a filter function that matches files using a glob-style pattern.

    Args:
        pattern (str): The glob-style pattern to match against file names.

    Returns:
        Callable[[Path], bool]: A filter function for use with recursive_search.
    """
    return lambda path: fnmatch.fnmatch(path.name, pattern)


def filter_by_size(min_size: int = None, max_size: int = None) -> Callable[[Path], bool]:
    """
    Create a filter function that matches files within a specified size range.

    Args:
        min_size (int, optional): Minimum file size in bytes. Defaults to None.
        max_size (int, optional): Maximum file size in bytes. Defaults to None.

    Returns:
        Callable[[Path], bool]: A filter function for use with recursive_search.
    """
    def size_filter(path: Path) -> bool:
        size = path.stat().st_size
        if min_size is not None and size < min_size:
            return False
        if max_size is not None and size > max_size:
            return False
        return True
    return size_filter

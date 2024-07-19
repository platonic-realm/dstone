"""
Bytes Utility Module

This module provides a comprehensive set of utility functions for various
byte-related operations, including conversions, human-readable representations,
endianness manipulations, and encoding/decoding operations.

Functions:
    bytes_to_human_readable: Convert bytes to a human-readable string.
    human_readable_to_bytes: Convert a human-readable string to bytes.
    bits_to_human_readable: Convert bits to a human-readable string.
    bits_to_bytes: Convert bits to bytes.
    bytes_to_bits: Convert bytes to bits.
    binary_prefix_to_decimal_prefix: Convert a value from a binary prefix to a decimal prefix.
    decimal_prefix_to_binary_prefix: Convert a value from a decimal prefix to a binary prefix.
    bits_per_second_to_human_readable: Convert bits per second to a human-readable string.
    bytes_per_second_to_human_readable: Convert bytes per second to a human-readable string.
    seconds_to_human_readable: Convert seconds to a human-readable time string.
    little_endian_to_big_endian: Convert a little-endian byte string to big-endian.
    big_endian_to_little_endian: Convert a big-endian byte string to little-endian.
    int_to_bytes: Convert an integer to a byte string.
    bytes_to_int: Convert a byte string to an integer.
    hex_to_bytes: Convert a hexadecimal string to bytes.
    bytes_to_hex: Convert bytes to a hexadecimal string.
    base64_to_bytes: Convert a base64 string to bytes.
    bytes_to_base64: Convert bytes to a base64 string.
"""

import re
from typing import Union
import base64


def bytes_to_human_readable(bytes_value: Union[int, float]) -> str:
    """
    Convert a byte value to a human-readable string.

    Args:
        bytes_value (Union[int, float]): The value in bytes to convert.

    Returns:
        str: A human-readable string representation of the byte value.

    Examples:
        >>> bytes_to_human_readable(1023)
        '1023.00 B'
        >>> bytes_to_human_readable(1024)
        '1.00 KiB'
        >>> bytes_to_human_readable(1048576)
        '1.00 MiB'
    """
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB']
    size = float(bytes_value)
    unit_index = 0

    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


def human_readable_to_bytes(size_string: str) -> int:
    """
    Convert a human-readable string to bytes.

    Args:
        size_string (str): A string representing a file size (e.g., '5.2 MiB', '3GiB').

    Returns:
        int: The size in bytes.

    Raises:
        ValueError: If the input string is not in a valid format.

    Examples:
        >>> human_readable_to_bytes('5.2 MiB')
        5452595
        >>> human_readable_to_bytes('3GiB')
        3221225472
    """
    units = {'B': 1, 'KIB': 1024, 'MIB': 1024**2, 'GIB': 1024**3, 'TIB': 1024**4, 'PIB': 1024**5}
    pattern = r'^\s*(\d+(?:\.\d+)?)\s*([BKMGTP]I?B?)\s*$'
    match = re.match(pattern, size_string, re.IGNORECASE)

    if not match:
        raise ValueError("Invalid size string format")

    size, unit = match.groups()
    return int(float(size) * units[unit.upper()])


def bits_to_human_readable(bits_value: Union[int, float]) -> str:
    """
    Convert a bit value to a human-readable string.

    Args:
        bits_value (Union[int, float]): The value in bits to convert.

    Returns:
        str: A human-readable string representation of the bit value.

    Examples:
        >>> bits_to_human_readable(1000)
        '1000.00 bit'
        >>> bits_to_human_readable(1000000)
        '1.00 Mbit'
        >>> bits_to_human_readable(1000000000)
        '1.00 Gbit'
    """
    units = ['bit', 'Kbit', 'Mbit', 'Gbit', 'Tbit', 'Pbit', 'Ebit']
    size = float(bits_value)
    unit_index = 0

    while size >= 1000.0 and unit_index < len(units) - 1:
        size /= 1000.0
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


def bits_to_bytes(bits: Union[int, float]) -> float:
    """
    Convert bits to bytes.

    Args:
        bits (Union[int, float]): The number of bits to convert.

    Returns:
        float: The equivalent number of bytes.

    Examples:
        >>> bits_to_bytes(8)
        1.0
        >>> bits_to_bytes(1024)
        128.0
    """
    return bits / 8


def bytes_to_bits(bytes_value: Union[int, float]) -> float:
    """
    Convert bytes to bits.

    Args:
        bytes_value (Union[int, float]): The number of bytes to convert.

    Returns:
        float: The equivalent number of bits.

    Examples:
        >>> bytes_to_bits(1)
        8.0
        >>> bytes_to_bits(128)
        1024.0
    """
    return bytes_value * 8


def binary_prefix_to_decimal_prefix(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from a binary prefix to a decimal prefix.

    Args:
        value (float): The value to convert.
        from_unit (str): The binary prefix unit (e.g., 'MiB', 'GiB').
        to_unit (str): The decimal prefix unit (e.g., 'MB', 'GB').

    Returns:
        float: The converted value.

    Raises:
        ValueError: If the unit prefixes are invalid.

    Examples:
        >>> binary_prefix_to_decimal_prefix(1, 'MiB', 'MB')
        1.048576
        >>> binary_prefix_to_decimal_prefix(1, 'GiB', 'GB')
        1.073741824
    """
    binary_prefixes = {'KiB': 1024, 'MiB': 1024**2, 'GiB': 1024**3, 'TiB': 1024**4, 'PiB': 1024**5}
    decimal_prefixes = {'KB': 1000, 'MB': 1000**2, 'GB': 1000**3, 'TB': 1000**4, 'PB': 1000**5}

    if from_unit not in binary_prefixes or to_unit not in decimal_prefixes:
        raise ValueError("Invalid unit prefixes")

    binary_value = value * binary_prefixes[from_unit]
    return binary_value / decimal_prefixes[to_unit]


def decimal_prefix_to_binary_prefix(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from a decimal prefix to a binary prefix.

    Args:
        value (float): The value to convert.
        from_unit (str): The decimal prefix unit (e.g., 'MB', 'GB').
        to_unit (str): The binary prefix unit (e.g., 'MiB', 'GiB').

    Returns:
        float: The converted value.

    Raises:
        ValueError: If the unit prefixes are invalid.

    Examples:
        >>> decimal_prefix_to_binary_prefix(1, 'MB', 'MiB')
        0.95367431640625
        >>> decimal_prefix_to_binary_prefix(1, 'GB', 'GiB')
        0.9313225746154785
    """
    binary_prefixes = {'KiB': 1024, 'MiB': 1024**2, 'GiB': 1024**3, 'TiB': 1024**4, 'PiB': 1024**5}
    decimal_prefixes = {'KB': 1000, 'MB': 1000**2, 'GB': 1000**3, 'TB': 1000**4, 'PB': 1000**5}

    if from_unit not in decimal_prefixes or to_unit not in binary_prefixes:
        raise ValueError("Invalid unit prefixes")

    decimal_value = value * decimal_prefixes[from_unit]
    return decimal_value / binary_prefixes[to_unit]


def bits_per_second_to_human_readable(bps: Union[int, float]) -> str:
    """
    Convert bits per second to a human-readable string.

    Args:
        bps (Union[int, float]): The number of bits per second.

    Returns:
        str: A human-readable string representation of the transfer rate.

    Examples:
        >>> bits_per_second_to_human_readable(1000)
        '1.00 Kbit/s'
        >>> bits_per_second_to_human_readable(1500000)
        '1.50 Mbit/s'
    """
    units = ['bit/s', 'Kbit/s', 'Mbit/s', 'Gbit/s', 'Tbit/s']
    size = float(bps)
    unit_index = 0

    while size >= 1000.0 and unit_index < len(units) - 1:
        size /= 1000.0
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


def bytes_per_second_to_human_readable(bps: Union[int, float]) -> str:
    """
    Convert bytes per second to a human-readable string.

    Args:
        bps (Union[int, float]): The number of bytes per second.

    Returns:
        str: A human-readable string representation of the transfer rate.

    Examples:
        >>> bytes_per_second_to_human_readable(1024)
        '1.00 KiB/s'
        >>> bytes_per_second_to_human_readable(1572864)
        '1.50 MiB/s'
    """
    units = ['B/s', 'KiB/s', 'MiB/s', 'GiB/s', 'TiB/s']
    size = float(bps)
    unit_index = 0

    while size >= 1024.0 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"


def seconds_to_human_readable(seconds: Union[int, float]) -> str:
    """
    Convert seconds to a human-readable time string.

    Args:
        seconds (Union[int, float]): The number of seconds to convert.

    Returns:
        str: A human-readable time string.

    Examples:
        >>> seconds_to_human_readable(3661)
        '1 hour, 1 minute, 1 second'
        >>> seconds_to_human_readable(86400)
        '1 day'
    """
    intervals = [
        (60 * 60 * 24, 'day'),
        (60 * 60, 'hour'),
        (60, 'minute'),
        (1, 'second')
    ]

    result = []
    for count, name in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                result.append(f"{value} {name}")
            else:
                result.append(f"{value} {name}s")
    return ', '.join(result)


def little_endian_to_big_endian(byte_string: bytes) -> bytes:
    """
    Convert a little-endian byte string to big-endian.

    Args:
        byte_string (bytes): The little-endian byte string to convert.

    Returns:
        bytes: The big-endian representation of the input.

    Examples:
        >>> little_endian_to_big_endian(b'\x01\x00\x00\x00')
        b'\x00\x00\x00\x01'
    """
    return byte_string[::-1]


def big_endian_to_little_endian(byte_string: bytes) -> bytes:
    """
    Convert a big-endian byte string to little-endian.

    Args:
        byte_string (bytes): The big-endian byte string to convert.

    Returns:
        bytes: The little-endian representation of the input.

    Examples:
        >>> big_endian_to_little_endian(b'\x00\x00\x00\x01')
        b'\x01\x00\x00\x00'
    """
    return byte_string[::-1]


def int_to_bytes(x: int, length: int = None, byteorder: str = 'big') -> bytes:
    """
    Convert an integer to a byte string.

    Args:
        x (int): The integer to convert.
        length (int, optional): The length of the resulting byte string. If None,
                                the minimum number of bytes required is used.
        byteorder (str, optional): The byte order: 'big' or 'little'. Defaults to 'big'.

    Returns:
        bytes: The byte string representation of the integer.

    Examples:
        >>> int_to_bytes(258)
        b'\x01\x02'
        >>> int_to_bytes(258, length=4, byteorder='little')
        b'\x02\x01\x00\x00'
    """
    if length is None:
        length = (x.bit_length() + 7) // 8
    return x.to_bytes(length, byteorder=byteorder)


def bytes_to_int(byte_string: bytes, byteorder: str = 'big') -> int:
    """
    Convert a byte string to an integer.

    Args:
        byte_string (bytes): The byte string to convert.
        byteorder (str, optional): The byte order: 'big' or 'little'. Defaults to 'big'.

    Returns:
        int: The integer representation of the byte string.

    Examples:
        >>> bytes_to_int(b'\x01\x02')
        258
        >>> bytes_to_int(b'\x02\x01\x00\x00', byteorder='little')
        258
    """
    return int.from_bytes(byte_string, byteorder=byteorder)


def hex_to_bytes(hex_string: str) -> bytes:
    """
    Convert a hexadecimal string to bytes.

    Args:
        hex_string (str): The hexadecimal string to convert.

    Returns:
        bytes: The byte representation of the hexadecimal string.

    Raises:
        ValueError: If the input string contains non-hexadecimal characters.

    Examples:
        >>> hex_to_bytes('48656c6c6f')
        b'Hello'
        >>> hex_to_bytes('0123456789ABCDEF')
        b'\x01#Eg\x89\xab\xcd\xef'
    """
    try:
        return bytes.fromhex(hex_string)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")


def bytes_to_hex(byte_string: bytes) -> str:
    """
    Convert bytes to a hexadecimal string.

    Args:
        byte_string (bytes): The bytes to convert.

    Returns:
        str: The hexadecimal representation of the bytes.

    Examples:
        >>> bytes_to_hex(b'Hello')
        '48656c6c6f'
        >>> bytes_to_hex(b'\x01#Eg\x89\xab\xcd\xef')
        '0123456789abcdef'
    """
    return byte_string.hex()


def base64_to_bytes(base64_string: str) -> bytes:
    """
    Convert a base64 string to bytes.

    Args:
        base64_string (str): The base64 string to convert.

    Returns:
        bytes: The byte representation of the base64 string.

    Raises:
        ValueError: If the input string is not a valid base64 encoding.

    Examples:
        >>> base64_to_bytes('SGVsbG8=')
        b'Hello'
        >>> base64_to_bytes('AQIDBAU=')
        b'\x01\x02\x03\x04\x05'
    """
    try:
        return base64.b64decode(base64_string)
    except base64.binascii.Error:
        raise ValueError("Invalid base64 string")


def bytes_to_base64(byte_string: bytes) -> str:
    """
    Convert bytes to a base64 string.

    Args:
        byte_string (bytes): The bytes to convert.

    Returns:
        str: The base64 representation of the bytes.

    Examples:
        >>> bytes_to_base64(b'Hello')
        'SGVsbG8='
        >>> bytes_to_base64(b'\x01\x02\x03\x04\x05')
        'AQIDBAU='
    """
    return base64.b64encode(byte_string).decode()


# Example usage
if __name__ == "__main__":
    print(bytes_to_human_readable(1048576))
    print(human_readable_to_bytes('1 MiB'))
    print(bits_to_human_readable(1000000))
    print(bits_to_bytes(1024))
    print(bytes_to_bits(128))
    print(binary_prefix_to_decimal_prefix(1, 'GiB', 'GB'))
    print(decimal_prefix_to_binary_prefix(1, 'GB', 'GiB'))
    print(bits_per_second_to_human_readable(1500000))
    print(bytes_per_second_to_human_readable(1572864))
    print(seconds_to_human_readable(3661))
    print(little_endian_to_big_endian(b'\x01\x00\x00\x00'))
    print(big_endian_to_little_endian(b'\x00\x00\x00\x01'))
    print(int_to_bytes(258))
    print(bytes_to_int(b'\x01\x02'))
    print(hex_to_bytes('48656c6c6f'))
    print(bytes_to_hex(b'Hello'))
    print(base64_to_bytes('SGVsbG8='))
    print(bytes_to_base64(b'Hello'))

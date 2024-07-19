import sys
sys.pycache_prefix = "/tmp/dstone/"

import unittest

from src.api.utils.bytes import bytes_to_human_readable, \
    human_readable_to_bytes, bits_to_human_readable, bits_to_bytes, \
    bytes_to_bits, binary_prefix_to_decimal_prefix, decimal_prefix_to_binary_prefix, \
    bits_per_second_to_human_readable, bytes_per_second_to_human_readable, \
    seconds_to_human_readable, little_endian_to_big_endian, big_endian_to_little_endian, \
    int_to_bytes, bytes_to_int, hex_to_bytes, bytes_to_hex, bytes_to_base64, base64_to_bytes


class TestBytesModule(unittest.TestCase):

    def test_bytes_to_human_readable(self):
        self.assertEqual(bytes_to_human_readable(1023), "1023.00 B")
        self.assertEqual(bytes_to_human_readable(1024), "1.00 KiB")
        self.assertEqual(bytes_to_human_readable(1048576), "1.00 MiB")

    def test_human_readable_to_bytes(self):
        self.assertEqual(human_readable_to_bytes('1 B'), 1)
        self.assertEqual(human_readable_to_bytes('1 KiB'), 1024)
        self.assertEqual(human_readable_to_bytes('1 MiB'), 1048576)
        with self.assertRaises(ValueError):
            human_readable_to_bytes('invalid input')

    def test_bits_to_human_readable(self):
        self.assertEqual(bits_to_human_readable(1000), "1.00 Kbit")
        self.assertEqual(bits_to_human_readable(1000000), "1.00 Mbit")
        self.assertEqual(bits_to_human_readable(1000000000), "1.00 Gbit")

    def test_bits_to_bytes(self):
        self.assertEqual(bits_to_bytes(8), 1.0)
        self.assertEqual(bits_to_bytes(1024), 128.0)

    def test_bytes_to_bits(self):
        self.assertEqual(bytes_to_bits(1), 8.0)
        self.assertEqual(bytes_to_bits(128), 1024.0)

    def test_binary_prefix_to_decimal_prefix(self):
        self.assertAlmostEqual(binary_prefix_to_decimal_prefix(1, 'MiB', 'MB'), 1.048576)
        self.assertAlmostEqual(binary_prefix_to_decimal_prefix(1, 'GiB', 'GB'), 1.073741824)
        with self.assertRaises(ValueError):
            binary_prefix_to_decimal_prefix(1, 'invalid', 'MB')

    def test_decimal_prefix_to_binary_prefix(self):
        self.assertAlmostEqual(decimal_prefix_to_binary_prefix(1, 'MB', 'MiB'), 0.95367431640625)
        self.assertAlmostEqual(decimal_prefix_to_binary_prefix(1, 'GB', 'GiB'), 0.9313225746154785)
        with self.assertRaises(ValueError):
            decimal_prefix_to_binary_prefix(1, 'invalid', 'MiB')

    def test_bits_per_second_to_human_readable(self):
        self.assertEqual(bits_per_second_to_human_readable(1000), "1.00 Kbit/s")
        self.assertEqual(bits_per_second_to_human_readable(1500000), "1.50 Mbit/s")

    def test_bytes_per_second_to_human_readable(self):
        self.assertEqual(bytes_per_second_to_human_readable(1024), "1.00 KiB/s")
        self.assertEqual(bytes_per_second_to_human_readable(1572864), "1.50 MiB/s")

    def test_seconds_to_human_readable(self):
        self.assertEqual(seconds_to_human_readable(3661), "1 hour, 1 minute, 1 second")
        self.assertEqual(seconds_to_human_readable(86400), "1 day")

    def test_little_endian_to_big_endian(self):
        self.assertEqual(little_endian_to_big_endian(b'\x01\x00\x00\x00'), b'\x00\x00\x00\x01')

    def test_big_endian_to_little_endian(self):
        self.assertEqual(big_endian_to_little_endian(b'\x00\x00\x00\x01'), b'\x01\x00\x00\x00')

    def test_int_to_bytes(self):
        self.assertEqual(int_to_bytes(258), b'\x01\x02')
        self.assertEqual(int_to_bytes(258, length=4, byteorder='little'), b'\x02\x01\x00\x00')

    def test_bytes_to_int(self):
        self.assertEqual(bytes_to_int(b'\x01\x02'), 258)
        self.assertEqual(bytes_to_int(b'\x02\x01\x00\x00', byteorder='little'), 258)

    def test_hex_to_bytes(self):
        self.assertEqual(hex_to_bytes('48656c6c6f'), b'Hello')
        with self.assertRaises(ValueError):
            hex_to_bytes('invalid hex')

    def test_bytes_to_hex(self):
        self.assertEqual(bytes_to_hex(b'Hello'), '48656c6c6f')

    def test_base64_to_bytes(self):
        self.assertEqual(base64_to_bytes('SGVsbG8='), b'Hello')
        with self.assertRaises(ValueError):
            base64_to_bytes('invalid base64!')

    def test_bytes_to_base64(self):
        self.assertEqual(bytes_to_base64(b'Hello'), 'SGVsbG8=')


if __name__ == '__main__':
    unittest.main()

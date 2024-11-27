#!/usr/bin/python3

"""
Log Parsing
"""

import sys
import re


def print_stats(total_size, status_counts):
    """
    Print stats
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        print(f"{status}: {status_counts[status]}")


def parse_log():
    """
    Parse Log
    """
    total_size = 0
    line_count = 0
    status_counts = {}

    try:
        for line in sys.stdin:
            # Regex to match log format
            match = re.search(
               r'(?P<ip>\S+)-?\s*' \
               r'\[.*\] "GET /projects/260 HTTP/1.1" ' \
               r'(?P<status>\S+) (?P<size>\S+)',
               line.strip()
            )

            if match:
                status = match.group("status")
                file_size = match.group("size")

                # Track metrics
                if file_size.isdigit():
                    total_size += int(file_size)

                if status.isdigit():
                    status = int(status)
                    if status not in status_counts:
                        status_counts[status] = 0
                    status_counts[status] += 1

                    line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except (KeyboardInterrupt, EOFError):
        print_stats(total_size, status_counts)
    finally:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    parse_log()

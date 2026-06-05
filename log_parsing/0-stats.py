#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
Prints statistics every 10 lines and/or on keyboard interruption (CTRL + C).
"""

import sys
import re


def print_stats(total_size, status_codes):
    """Print statistics: total file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    line_count = 0
    total_size = 0
    status_codes = {}
    
    # Pattern to match log format: IP - [date] "METHOD path HTTP/VERSION" status_code size
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "(\w+) (.*?) (HTTP/\d\.\d)" (\d+) (\d+)$'
    
    try:
        for line in sys.stdin:
            line = line.rstrip('\n')
            match = re.match(pattern, line)
            
            if match:
                try:
                    status_code = int(match.group(6))
                    file_size = int(match.group(7))
                except ValueError:
                    # Skip if status code or size is not an integer
                    continue
                
                line_count += 1
                total_size += file_size
                
                # Only track allowed status codes
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    if status_code not in status_codes:
                        status_codes[status_code] = 0
                    status_codes[status_code] += 1
                
                # Print stats every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
                    
    except KeyboardInterrupt:
        # Print stats on CTRL + C
        print_stats(total_size, status_codes)

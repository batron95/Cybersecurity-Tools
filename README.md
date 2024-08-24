# Cybersecurity Tools

This is a simple Python script that provides basic cybersecurity utilities. The tools included are:

1. **File Hashing**: Generate cryptographic hashes for files using algorithms like SHA256.
2. **Port Scanning**: Scan a specified range of ports on a given host to identify open ports.
3. **Website Status Check**: Check the status of a website by sending an HTTP GET request.

## Features

- **File Hashing**: Supports SHA256, MD5, and other hashing algorithms.
- **Port Scanning**: Scans a range of TCP ports on a specified host to identify which ports are open.
- **Website Status Check**: Returns the HTTP status code and reason for a given URL.

## Prerequisites

- Python 3.x
- The following Python libraries (install them using `pip` if necessary):
  - `requests`

## Installation

## 1.Clone the repository:
   ```bash
           git clone https://github.com/your-username/cybersecurity-tools.git
   cd cybersecurity-tools

## 2.Install required dependencies.
            pip install requests

  ## Usage
Run the script using Python:

```bash
             python cybersecurity_tools.py

You will be presented with a menu to choose the desired tool:

Cybersecurity Tools
1. Hash a File
2. Scan for Open Ports
3. Check Website Status
4. Exit
Choose an option (1-4):

1. Hash a File
  Enter the file name you want to hash.
  Enter the desired hashing algorithm (default is SHA256).
  Example:
  Enter the file name to hash: example.txt
  Enter the hashing algorithm (default is SHA256): md5

2. Scan for Open Ports
  Enter the host IP address or domain.
  Enter the start port and end port (default range is 1-1024).

  Example:
  Enter the host to scan (e.g., 127.0.0.1): 192.168.1.1
  Enter the start port (default is 1): 20
  Enter the end port (default is 1024): 100

3. Check Website Status
  Enter the website URL.
  Example:

  Enter the website URL (e.g., http://example.com): http://example.com

4. Exit
  Choose this option to exit the program.

License
  This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
  Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

Acknowledgments
  Thanks to the open-source community for providing useful libraries like requests.

Feel free to modify the `README.md` to better suit your project's needs or add additional sections as necessary!

import hashlib
import socket
import requests
import os

def hash_file(filename, algorithm='sha256'):
    """Generate a hash for the given file using the specified algorithm."""
    h = hashlib.new(algorithm)
    with open(filename, 'rb') as file:
        chunk = file.read(8192)
        while chunk:
            h.update(chunk)
            chunk = file.read(8192)
    return h.hexdigest()

def scan_open_ports(host, start_port=1, end_port=1024):
    """Scan for open ports on a given host within the specified range."""
    open_ports = []
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def check_website_status(url):
    """Check the status of a website by sending an HTTP GET request."""
    try:
        response = requests.get(url, timeout=5)
        return response.status_code, response.reason
    except requests.RequestException as e:
        return None, str(e)

def main():
    while True:
        print("\nCybersecurity Tools")
        print("1. Hash a File")
        print("2. Scan for Open Ports")
        print("3. Check Website Status")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            filename = input("Enter the file name to hash: ")
            if os.path.isfile(filename):
                algorithm = input("Enter the hashing algorithm (default is SHA256): ") or 'sha256'
                print(f"{algorithm.upper()} hash of {filename}: {hash_file(filename, algorithm)}")
            else:
                print(f"File not found: {filename}. Please provide a valid file name.")
        
        elif choice == '2':
            host = input("Enter the host to scan (e.g., 127.0.0.1): ")
            start_port = int(input("Enter the start port (default is 1): ") or 1)
            end_port = int(input("Enter the end port (default is 1024): ") or 1024)
            open_ports = scan_open_ports(host, start_port, end_port)
            if open_ports:
                print(f"Open ports on {host}: {open_ports}")
            else:
                print(f"No open ports found on {host} in the range {start_port}-{end_port}")
        
        elif choice == '3':
            url = input("Enter the website URL (e.g., http://example.com): ")
            status_code, reason = check_website_status(url)
            if status_code:
                print(f"Website {url} responded with status: {status_code} {reason}")
            else:
                print(f"Failed to check website {url}: {reason}")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

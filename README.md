# Subpath Scanner

A powerful Python tool to discover common paths and random paths of a specified domain.

## Requirements
- Python 3.x
- `requests` library
- `colorama` library

## Installation

1. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the tool:
    ```bash
    python main.py
    ```

2. Choose an option:
    - Type `1` to run the subpath scanner and enter the domain to discover paths.
    - Type `2` to view the list of common paths.
    - Type `3` to add new paths to the list.

3. Follow the prompts to enter the domain, view results, or add new paths. For adding paths, type each new path and press Enter. Type `exit` to finish adding.

## Features
- Scans for common paths.
- Generates and tests random paths.
- Allows users to add custom paths.
- Displays found paths.

## Example

```bash
Subpath Scanner
===============

Choose an option (type 'exit' to quit):

1  = Run Subpath Scanner
2  = List of Common Paths
3  = Add Paths

root@you:~$ 1
[Subpath Scanner]: Enter the domain: example.com

[Subpath Scanner]: Subpath Scan Results
Found Paths:
  https://example.com/admin
  https://example.com/login
  https://example.com/dashboard
  ...

root@you:~$ 2

[Subpath Scanner]: Common Paths
Common Paths:
  admin
  login
  dashboard
  ...

root@you:~$ 3
[Subpath Scanner]: Enter paths to add (type 'exit' to finish adding):
Add Path: newpath

[Subpath Scanner]: Added path: newpath

Add Path: anotherpath

[Subpath Scanner]: Added path: anotherpath

Add Path: exit

[Subpath Scanner]: Path addition finished.

```

## Usage Caution
- For educational or testing purposes only.
- Do not use for malicious activities.
- Follow ethical standards while using this tool.

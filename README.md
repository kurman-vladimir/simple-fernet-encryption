# Secure Symmetric Encryption and Decryption

![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Python script for secure string encryption (using Fernet) with password-based key derivation (using PBKDF2-HMAC-SHA256)

## Usage

### Setup

Before using this script, ensure you have Python 3.13 or higher installed on your system.

1. Clone this repository:

   ```bash
   git clone https://github.com/kurman-vladimir/simple-fernet-encription.git
    ```
2. Navigate to the project directory:

    ```bash
   cd simple-fernet-encription
    ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Check code and run tests

   ```bash
   ruff check && mypy --strict ./ && pytest ./unit_tests.py
   ```

## Running the Application

Run main.py:

   ```bash
   python ./main.py encrypt "secret string to encrypt" --encryption-key PaSsWoRd
   python ./main.py decrypt "M3ImcsKPNDBggBJEIJlDFu-RJdCMPWilijBbWeFbR1A=$gAAAAABoobwXYg3AVyDCSwx9lPUr5rqYxl4LkR03YlQ82uUDj3NHzcsYmg506Jvm0FU0Cus9tFLxdV3a4d_ItceTICUP39UKoXFJjQyM2n6xlZu371JpwOA=" --encryption-key PaSsWoRd
   ```

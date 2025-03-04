#!/usr/bin/env python3

# Use this script to generate your own values for encryption key
# and token secret. Then modify the script that starts Visual DB.

import secrets
import base64

def generate_key(length):
    """
    Generate a cryptographically secure random key of specified byte length.
    
    Args:
        length (int): Number of random bytes to generate
        
    Returns:
        str: Base64url-encoded random string
    """
    # Generate random bytes of supplied length
    random_bytes = secrets.token_bytes(length)
    
    # Encode to base64 and make URL-safe
    base64_encoded = base64.b64encode(random_bytes).decode('utf-8')
    base64_url_encoded = base64_encoded.replace('+', '-').replace('/', '_').replace('=', '')
    
    return base64_url_encoded

if __name__ == "__main__":
    encryption_key = generate_key(16)
    token_secret = generate_key(64)

    print(f"VDB_ENCRYPTION_KEY={encryption_key}")
    print(f"VDB_TOKEN_SECRET={token_secret}")


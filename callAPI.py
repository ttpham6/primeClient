
import json
import urllib.request


def generate_primes(limit: int, host: str = "localhost", port: int = 8000) -> dict:
    """
    Send a request to generate prime numbers up to a limit using the prime generation API.
    
    Args:
        limit: Upper limit for generating prime numbers
        host: API host (default="localhost")
        port: API port (default=8000)
        
    Returns:
        dict: Response from the API containing the generated primes
    """
    
    host = "127.0.0.1"
    port = "5000"
    url = f"http://{host}:{port}/generate-primes"
    data = json.dumps({"limit": limit}).encode('utf-8')
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        request = urllib.request.Request(
            url=url,
            data=data,
            headers=headers,
            method="POST"
        )
        
        with urllib.request.urlopen(request) as response:
            return json.loads(response.read().decode('utf-8'))
            
    except urllib.error.URLError as e:
        return {"error": f"Connection failed: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Invalid response from server"}

# response = generate_primes(100)
# print(response)
def main():
    response = generate_primes(100)
    print(response)


if __name__ == "__main__":
    main()
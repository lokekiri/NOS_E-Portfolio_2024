import subprocess

def tracert(domain):
    try:
        result = subprocess.run(["tracert", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("tracert command not found. Use 'traceroute' on Linux/Mac.")
    except Exception as e:
        print(f"Error: {e}")

domain = input("Enter the website or IP address: ")
tracert(domain)

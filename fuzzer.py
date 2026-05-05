import requests

def load_wordlist(filename="wordlists.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] {filename} not found in current directory.")
        print("[!] Please create wordlists.txt and add endpoints.")
        exit()

def main():
    base_url = input("Enter domain or IP : ").strip()

    if not base_url.startswith("http"):
        base_url = "http://" + base_url

    words = load_wordlist()

    print(f"\n[*] Starting fuzzing on {base_url}\n")

    for word in words:
        url = f"{base_url.rstrip('/')}/{word}"

        try:
            res = requests.get(url, timeout=5)

            if res.status_code != 404:
                print(f"[+] {word} -> {res.status_code}")
                print(res.text[:200])  # preview response
                print("-" * 40)

        except requests.exceptions.RequestException as e:
            print(f"[!] Error on {word}: {e}")

if __name__ == "__main__":
    main()

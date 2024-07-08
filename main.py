import requests
import os
import colorama
import random
import string
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

colorama.init()
clear_command = "cls" if os.name == "nt" else "clear"

def clear_screen():
    os.system(clear_command)

def print_info(title, info):
    print(colorama.Fore.GREEN + f"[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"{title}")
    print("")
    for key, value in info.items():
        if isinstance(value, list):
            print(colorama.Fore.YELLOW + f"{key}:")
            for item in value:
                print(colorama.Fore.LIGHTWHITE_EX + f"  {item}")
        else:
            print(colorama.Fore.YELLOW + f"{key}: " + colorama.Fore.LIGHTWHITE_EX + f"{value}")
    print("")

paths = [
    "admin", "login", "dashboard", "api", "user", "profile", "settings", "uploads",
    "download", "docs", "support", "blog", "about", "contact", "help", "search",
    "static", "files", "news", "forum", "tickets", "cart", "checkout", "order", "track",
    "terms", "privacy", "sitemap", "register", "reset-password", "verify-email", "newsletter",
    "payment", "subscription", "reports", "monitoring", "feedback", "contact-us", "careers",
    "news", "events", "feedback", "community", "resources", "careers", "services", "products",
    "legal", "login", "logout", "terms-of-service", "privacy-policy", "user-profile",
    "admin-dashboard", "admin-login", "admin-portal", "admin-console", "admin-panel",
    "manage", "statistics", "audit", "history", "logs", "backend", "support-tickets",
    "admin-settings", "user-settings", "site-map", "social-media", "affiliate", "recovery",
    "reset", "verify", "activation", "subscribe", "unsubscribe", "feedback-form",
    "contact-form", "donate", "campaigns", "subscription-plans", "billing", "invoices",
    "checkout", "cart", "orders", "user-orders", "tracking", "shipping", "returns",
    "refunds", "wishlist", "search-results", "search-query", "search-page", "notifications",
    "alerts", "subscriptions", "deals", "offers", "promotions", "events", "calendar",
    "schedule", "bookings", "appointments", "register", "sign-up", "forgot-password",
    "reset-password", "change-password", "user-management", "admin-management", "admin-users",
    "admin-roles", "admin-permissions", "api-docs", "api-v1", "api-v2", "api-v3", "api-v4",
    "api-testing", "api-explorer", "api-support", "developer", "developers", "dev",
    "api-endpoints", "api-keys", "api-docs", "webhooks", "hooks", "integration", "connect",
    "oauth", "auth", "authentication", "authorization", "social-login", "single-sign-on",
    "sso", "email-verification", "email-confirmation", "password-reset", "password-recovery",
    "account", "profile-settings", "personal-info", "change-email", "change-phone",
    "support-center", "faq", "help-center", "guides", "tutorials", "how-to", "documentation",
    "developer-tools", "cli", "command-line", "tools", "utilities", "services", "web-services",
    "api-status", "system-status", "health-check", "ping", "test", "benchmark", "performance",
    "site-status", "status"
]

def check_path(domain, path):
    url = f'https://{domain}/{path}'
    try:
        response = requests.get(url, timeout=1)
        if response.status_code == 200:
            return url
    except requests.RequestException:
        pass
    return None

def subpath_scanner(domain, paths):
    found_paths = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_path, domain, path) for path in paths]
        for future in futures:
            result = future.result()
            if result:
                found_paths.append(result)

    for _ in range(10):
        random_path = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        url = f'https://{domain}/{random_path}'
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                found_paths.append(url)
        except requests.RequestException:
            pass

    return {"Found Paths": list(set(found_paths))}

def add_paths():
    global paths
    print(colorama.Fore.GREEN + "[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter paths to add (type 'exit' to finish adding):")
    while True:
        new_path = input(colorama.Fore.MAGENTA + "Add Path: " + colorama.Fore.WHITE).strip()
        if new_path.lower() == 'exit':
            break
        elif new_path:
            paths.append(new_path)
            print(colorama.Fore.GREEN + "[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + f"Added path: {new_path}")
        else:
            print(colorama.Fore.RED + "[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "No path entered. Please try again.")
    print(colorama.Fore.GREEN + "[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Path addition finished.")

def main():
    while True:
        clear_screen()
        print(colorama.Fore.GREEN + "[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Choose an option (type 'exit' to quit):")
        print("")
        print(colorama.Fore.YELLOW + "1 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "Run Subpath Scanner")
        print(colorama.Fore.YELLOW + "2 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "List of Common Paths")
        print(colorama.Fore.YELLOW + "3 " + colorama.Fore.LIGHTYELLOW_EX + "= " + colorama.Fore.WHITE + "Add Paths")
        print("")

        choice = input(colorama.Fore.MAGENTA + "root@you:~$ " + colorama.Fore.WHITE).strip()

        if choice == '1':
            domain = input(colorama.Fore.GREEN + "[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Enter the domain: " + colorama.Fore.WHITE).strip()
            info = subpath_scanner(domain, paths)
            print_info("Subpath Scan Results", info)
        elif choice == '2':
            print_info("Common Paths", {"Common Paths": paths})
        elif choice == '3':
            add_paths()
        elif choice.lower() == 'exit':
            break
        else:
            print(colorama.Fore.GREEN + "[Subpath Scanner]: " + colorama.Fore.RED + "Invalid choice, please try again.")
        
        input(colorama.Fore.GREEN + "[Subpath Scanner]: " + colorama.Fore.LIGHTYELLOW_EX + "Press Enter to continue...")

if __name__ == "__main__":
    main()

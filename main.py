import os
import sys
import requests
from bs4 import BeautifulSoup
import time
import json
from pathlib import Path
import random

CACHE_DIR = Path.home() / ".module_docs_cache"
CACHE_DIR.mkdir(exist_ok=True)

# Colors for CLI
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Fetch documentation URL
def fetch_module_url(module_name):
    print(f"{Colors.OKCYAN}Searching for documentation of {module_name}...{Colors.ENDC}")
    search_url = f"https://pypi.org/search/?q={module_name}"
    response = requests.get(search_url)

    if response.status_code != 200:
        print(f"{Colors.FAIL}Failed to connect to PyPI. Status code: {response.status_code}{Colors.ENDC}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("a", class_="package-snippet")
    if not result:
        print(f"{Colors.WARNING}No PyPI page found for module: {module_name}{Colors.ENDC}")
        return None

    module_url = "https://pypi.org" + result["href"]
    print(f"{Colors.OKGREEN}Found PyPI page: {module_url}{Colors.ENDC}")
    return module_url

# Fetch documentation content
def fetch_documentation_content(module_name):
    cache_file = CACHE_DIR / f"{module_name}.json"
    if cache_file.exists():
        print(f"{Colors.OKBLUE}Loading cached documentation for {module_name}.{Colors.ENDC}")
        with open(cache_file, "r") as f:
            return json.load(f)

    module_url = fetch_module_url(module_name)
    if not module_url:
        return None

    response = requests.get(module_url)
    if response.status_code != 200:
        print(f"{Colors.FAIL}Failed to fetch documentation. Status code: {response.status_code}{Colors.ENDC}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    description = soup.find("p", class_="package-description__summary")
    description = description.text.strip() if description else "No description available."

    content = {
        "module": module_name,
        "url": module_url,
        "description": description,
    }

    with open(cache_file, "w") as f:
        json.dump(content, f)

    return content

# Display documentation
def display_documentation(content):
    if not content:
        print(f"{Colors.FAIL}No documentation available.{Colors.ENDC}")
        return

    print(f"{Colors.HEADER}Module: {content['module']}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}Description: {content['description']}{Colors.ENDC}")
    print(f"{Colors.OKCYAN}More Info: {content['url']}{Colors.ENDC}")

# Hackathon tips
def get_random_hackathon_tip():
    tips = [
        "Remember to take breaks and stay hydrated!",
        "Collaborate effectively with your team for better results.",
        "Test your code frequently to catch bugs early.",
        "Keep your project scope realistic given the time constraints.",
        "Focus on a working prototype rather than perfection.",
        "Write clear and concise documentation for your project.",
        "Plan your tasks with a timeline to stay organized.",
        "Don’t hesitate to ask mentors for help.",
        "Use version control to manage your code changes.",
        "Take short walks to refresh your mind.",
        "Celebrate small milestones with your team.",
        "Ensure your code is readable and maintainable.",
        "Prioritize features that deliver the most value.",
        "Sleep is important – don’t pull all-nighters.",
        "Share your progress on social media to build excitement.",
        "Take care of ergonomics to avoid fatigue.",
        "Prepare a solid pitch or demo for your project.",
        "Use online resources wisely but avoid over-researching.",
        "Focus on solving a real problem rather than adding fluff.",
        "Document your setup process for smooth deployment.",
        "Set achievable goals for each hackathon session.",
        "Debugging can be fun – stay positive!",
        "Keep snacks and water within reach for quick energy boosts.",
        "Use a project management tool to assign tasks.",
        "Learn from others’ projects and ideas.",
        "Don’t stress too much about winning – enjoy the process.",
        "Practice your final presentation ahead of time.",
        "Ensure your project is accessible and user-friendly.",
        "Keep backups of your code to avoid data loss.",
        "Embrace challenges as opportunities to learn."
    ]
    return random.choice(tips)

# Main CLI
if __name__ == "__main__":
    print(f"{Colors.BOLD}Welcome to ModuleDoc Finder!{Colors.ENDC}")
    print("This tool helps you find documentation for Python modules.\n")

    if len(sys.argv) < 2:
        print(f"{Colors.WARNING}Usage: python script.py <module_name>{Colors.ENDC}")
        sys.exit(1)

    module_name = sys.argv[1]
    content = fetch_documentation_content(module_name)
    display_documentation(content)

    # Reminder for hackathon fun
    random_tip = get_random_hackathon_tip()
    print(f"\n{Colors.OKGREEN}Hackathon Tip: {random_tip}{Colors.ENDC}")
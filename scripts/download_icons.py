
import os
import requests
import shutil

icons = {
    "code": "flat-color-icons:code",
    "palette": "flat-color-icons:palette",
    "server": "flat-color-icons:services",
    "database": "flat-color-icons:database",
    "chart-line": "flat-color-icons:line-chart",
    "tools": "flat-color-icons:settings",
    "python": "logos:python",
    "ruby": "logos:ruby",
    "js": "logos:javascript",
    "typescript": "logos:typescript-icon",
    "html5": "logos:html-5",
    "css3": "logos:css-3",
    "php": "logos:php",
    "go": "logos:go",
    "dotnetcore": "logos:dotnet",
    "swift": "logos:swift",
    "atom": "logos:react",
    "ant": "logos:ant-design",
    "zustand": "logos:zustand",
    "ember": "logos:ember",
    "wind": "logos:tailwindcss-icon",
    "forward": "logos:nextjs-icon",
    "zap": "logos:vitejs",
    "angularjs": "logos:angular-icon",
    "bootstrap": "logos:bootstrap",
    "django-plain-wordmark": "logos:django-icon",
    "djangorest-plain-wordmark": "logos:django-icon",
    "flask-plain-wordmark": "logos:flask",
    "rails-plain-wordmark": "logos:rails",
    "rspec": "logos:rspec",
    "fastapi": "logos:fastapi-icon",
    "express-original": "logos:express",
    "mysql": "logos:mysql-icon",
    "postgresql": "logos:postgresql",
    "sqlite": "logos:sqlite",
    "neo4j-plain-wordmark": "logos:neo4j",
    "redis": "logos:redis",
    "firebase": "logos:firebase",
    "rabbitmq": "logos:rabbitmq-icon",
    "elasticsearch": "logos:elasticsearch",
    "grafana": "logos:grafana",
    "numpy": "logos:numpy",
    "pandas": "logos:pandas-icon",
    "jupyter": "logos:jupyter",
    "github-original-wordmark": "logos:github-icon",
    "google": "logos:google-icon",
    "traefikproxy": "logos:traefik",
    "jenkins": "logos:jenkins",
    "terraform": "logos:terraform-icon",
    "kubernetes": "logos:kubernetes",
    "docker": "logos:docker-icon",
    "aws": "logos:aws",
    "gcp": "logos:google-cloud",
    "git": "logos:git-icon",
    "gitlab": "logos:gitlab",
    "vscode": "logos:visual-studio-code",
    "linux": "logos:linux-tux",
    "nixos": "logos:nixos",
    "postman": "logos:postman-icon",
    "nginx": "logos:nginx",
    "apache": "logos:apache",
    "hugo": "logos:hugo",
    "launchdarkly": "logos:launchdarkly",
    "ollama": "skill-icons:ollama-light",
    "huggingface": "logos:huggingface"
}

# Delete icons folder
directory_path = "../static/tech_icons"
if os.path.exists(directory_path):
    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' and all its contents have been removed.")
    except OSError as e:
        print(f"Error: {directory_path} : {e.strerror}")
else:
    print(f"Directory '{directory_path}' not found.")

os.makedirs(directory_path, exist_ok=True)

for name, slug in icons.items():
    prefix, icon_name = slug.split(":")
    url = f"https://api.iconify.design/{prefix}/{icon_name}.svg?width=56&height=56"
    print(f"Fetching {name} from {url}...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{directory_path}/{name}.svg", "wb") as f:
                f.write(response.content)
        else:
            with open(f"log.txt", "a") as f:
                f.write(f"Failed to fetch {name}: {response.status_code}\n")
    except Exception as e:
        with open(f"log.txt", "a") as f:
            f.write(f"Error fetching {name}: {e}\n")

print("Done!")

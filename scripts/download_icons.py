
import os
import requests
import shutil

icons = {
    "angularjs": "logos:angular-icon",
    "ant": "logos:ant-design",
    "apache": "logos:apache",
    "react": "logos:react",
    "aws": "logos:aws",
    "bootstrap": "logos:bootstrap",
    "chart-line": "flat-color-icons:line-chart",
    "css3": "logos:css-3",
    "database": "flat-color-icons:database",
    "django": "logos:django-icon",
    "djangorest": "devicon-plain:djangorest",
    "docker": "logos:docker-icon",
    "dotnetcore": "logos:dotnet",
    "elasticsearch": "logos:elasticsearch",
    "ember": "vscode-icons:file-type-ember",
    "express": "skill-icons:expressjs-light",
    "fastapi": "logos:fastapi-icon",
    "fastly": "logos:fastly",
    "firebase": "logos:firebase-icon",
    "flask": "skill-icons:flask-dark",
    "nextjs": "logos:nextjs-icon",
    "gcp": "logos:google-cloud",
    "git": "logos:git-icon",
    "github": "mdi:github",
    "gitlab": "material-icon-theme:gitlab",
    "go": "logos:go",
    "google": "logos:google-icon",
    "grafana": "logos:grafana",
    "html5": "logos:html-5",
    "huggingface": "devicon:huggingface",
    "hugo": "devicon:hugo",
    "jenkins": "logos:jenkins",
    "js": "logos:javascript",
    "jupyter": "logos:jupyter",
    "kubernetes": "logos:kubernetes",
    "launchdarkly": "logos:launchdarkly-icon",
    "linux": "logos:linux-tux",
    "mysql": "logos:mysql-icon",
    "neo4j": "vscode-icons:file-type-neo4j",
    "nginx": "logos:nginx",
    "nixos": "devicon:nixos",
    "numpy": "logos:numpy",
    "ollama": "simple-icons:ollama",
    "pandas": "logos:pandas-icon",
    "php": "logos:php",
    "postgresql": "logos:postgresql",
    "postman": "logos:postman-icon",
    "python": "logos:python",
    "rabbitmq": "logos:rabbitmq-icon",
    "rails": "skill-icons:rails",
    "redis": "logos:redis",
    "rspec": "material-icon-theme:rspec",
    "ruby": "logos:ruby",
    "sqlite": "vscode-icons:file-type-sqlite",
    "swift": "logos:swift",
    "terraform": "logos:terraform-icon",
    "typescript": "logos:typescript-icon",
    "vscode": "logos:visual-studio-code",
    "tailwind": "logos:tailwindcss-icon",
    "vite": "logos:vitejs",
    "zustand": "devicon:zustand"
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

# Delete log
log_path = "log.txt"
if os.path.exists(log_path):
    try:
        os.remove(log_path)
        print(f"File '{log_path}' has been removed.")
    except OSError as e:
        print(f"Error: {log_path} : {e.strerror}")
else:
    print(f"File '{log_path}' not found.")

# Create icons folder
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

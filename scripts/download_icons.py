
import os
import requests
import shutil

icons = {
    "angularjs": "logos:angular-icon",
    "ant": "logos:ant-design",
    "apache": "logos:apache",
    "react": "logos:react",
    "aws": "skill-icons:aws-light",
    "bootstrap": "logos:bootstrap",
    "chart-line": "flat-color-icons:line-chart",
    "css3": "logos:css-3",
    "database": "flat-color-icons:database",
    "django": "logos:django-icon",
    "djangorest": "devicon-plain:djangorest-wordmark",
    "docker": "logos:docker-icon",
    "dotnetcore": "logos:dotnet",
    "elasticsearch": "logos:elasticsearch",
    "elk": "simple-icons:elk",
    "ember": "vscode-icons:file-type-ember",
    "express": "skill-icons:expressjs-light",
    "copilot": "devicon:githubcopilot-wordmark",
    "fastapi": "logos:fastapi-icon",
    "fastly": "logos:fastly",
    "firebase": "logos:firebase-icon",
    "flask": "skill-icons:flask-dark",
    "nextjs": "logos:nextjs-icon",
    "gcp": "logos:google-cloud",
    "git": "logos:git-icon",
    "github": "skill-icons:github-light",
    "gitlab": "material-icon-theme:gitlab",
    "go": "logos:go",
    "google": "logos:google-icon",
    "grafana": "logos:grafana",
    "html5": "logos:html-5",
    "huggingface": "devicon:huggingface",
    "hugo": "devicon:hugo",
    "jenkins": "logos:jenkins",
    "javascript": "logos:javascript",
    "java": "skill-icons:java-dark",
    "jupyter": "logos:jupyter",
    "kubernetes": "logos:kubernetes",
    "launchdarkly": "logos:launchdarkly-icon",
    "linux": "logos:linux-tux",
    "mysql": "logos:mysql",
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
    "zustand": "devicon:zustand",
    "donejs": "file-icons:donejs",
    "sinatra": "logos:sinatra",
    "progress": "vscode-icons:file-type-progress",
    "antigravity": "material-symbols:antigravity-outline",
    "proxmox": "devicon-plain:proxmox-wordmark",
    "pytest": "devicon:pytest-wordmark",
    "reactquery": "logos:react-query-icon",
    "playwright": "material-icon-theme:playwright",
    "materialui": "devicon-plain:materialui",
    "jest": "skill-icons:jest",
    "ai": "carbon:ai",
    "cucumber": "logos:cucumber",
    "jquery": "skill-icons:jquery",
    "browserstack": "devicon:browserstack",
    "wordpress": "devicon-plain:wordpress-wordmark",
    "statamic": "simple-icons:statamic",
    "googleanalytics": "logos:google-analytics",
    "mocha": "devicon:mocha",
    "chai": "logos:chai",
    "less": "logos:less",
    "sass": "skill-icons:sass",
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
    url = f"https://api.iconify.design/{prefix}/{icon_name}.svg?width=56&height=56&color=%23dddddd"
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

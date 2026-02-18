# kcarmonamurphy.github.io

Welcome to my personal portfolio site!

The site is built using Hugo, a lightning-fast static site generator. It uses the sleek and professional [Careercanvas theme](https://github.com/felipecordero/careercanvas), designed and built by the legendary [Felipe Cordero](https://github.com/felipecordero) - thank you so much for open sourcing this wonderful project!

### Site features:
* Work Experience & Tech Stack: A deep dive into my professional background and the tools/languages I've used on professional projects and hobby tinkering.
* Projects: A showcase of my key work, including technical challenges I've solved and links to repositories on Github.
* Connect with me: I’ve integrated Calendly so you can schedule a meeting with me directly through the site. Also, I'm using Formspree to host a contact form without exposing my real email address.
* Hiding credentials through Cloudflare: To keep things secure, I’ve implemented a Cloudflare Worker which performs an API request to fetch Pexels images for the homepage background on behalf of my portfolio site, in order to not expose the Pexels credentials

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
- [Hugo](https://gohugo.io/installation/) (Extended version recommended)
- [Node.js](https://nodejs.org/) (for npm packages)
- [npm](https://www.npmjs.com/) (comes with Node.js)

Optional for Pexels dynamic backgrounds to work:
- [Cloudflare Workers](https://workers.cloudflare.com/)
- [Pexels API](https://www.pexels.com/)

## 🏗️ Installation

1. Clone the repository:
```bash
git clone
cd kcarmonamurphy.github.io
```

2. Install npm dependencies:
```bash
npm install
```

## 🚀 Development

To start the development server:

```bash
npm run dev
```

This command runs `hugo server -D`, which starts a local server and includes draft content (content with `draft: true` in the front matter). This is useful for previewing unpublished or in-progress content during development.

The site will be available at `http://localhost:1313`

## 🏗️ Building

To build the site for production, you need to:

1. Build the CSS with Tailwind:
```bash
npm run build:css
```

2. Build the site with Hugo:
```bash
npm run build
```

Or you can do both in one command:
```bash
npm run build:css && npm run build
```

The built site will be in the `public/` directory.

Note: The CSS build step is necessary because the site uses Tailwind CSS, which needs to be processed to generate the final CSS file with only the used styles.

## Pexels Dynamic Background

Content coming soon

## 📁 Project Structure

- `assets/` - Contains source files for CSS, JavaScript, and other assets
- `content/` - Contains the content of your site
- `static/` - Contains static files like images
- `themes/careercanvas/` - Contains the CareerCanvas theme
- `config.toml` - Main configuration file
- `tailwind.config.js` - Tailwind CSS configuration

## 🛠️ Technologies Used

- [Hugo](https://gohugo.io/) - Static site generator
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [@tailwindcss/typography](https://tailwindcss.com/docs/typography-plugin) - Typography plugin for Tailwind CSS
- [CareerCanvas](https://github.com/felipecordero/careercanvas) - Custom Hugo theme
- [Cloudflare Workers](https://workers.cloudflare.com/) - Cloudflare workers for serverless functions

## 👨‍💻 About the Theme

The [Careercanvas theme](https://github.com/felipecordero/careercanvas) is a custom Hugo theme designed and built by [Felipe Cordero](https://github.com/felipecordero), who has kindly open sourced the theme for others to use. It is targeted for technical and engineering portfolios. It features:
- Modern, responsive design
- Dark mode support
- Interactive components
- Image galleries
- Multilingual support
- Optimized for technical content

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📫 Contact

For any questions or suggestions, please open an issue in the GitHub repository or visit [felipecordero.com](https://felipecordero.com).
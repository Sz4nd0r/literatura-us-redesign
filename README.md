# Literatura.us 2.0 - Modernization Project

Welcome to the **Literatura.us 2.0** repository. This project is a comprehensive modernization of the [literatura.us](https://literatura.us) website, focusing on providing a premium reading experience, modern aesthetics, improved SEO, and total accessibility for classic literature.

## 📺 Project Overview

Watch the project demonstration and walkthrough here:
**[View Project Demonstration on YouTube](https://youtu.be/2msKDA5HpDU)**

## 🚀 Key Features

*   **Premium Reading Experience**: Specifically designed typography and color palettes for reduced eye strain during long-form reading.
*   **Modern Architecture**: Migrated from legacy systems to a modern static site generation (SSG) workflow.
*   **AI-Powered Formatting**: Intelligent processing of literary texts to ensure semantic markdown, proper dialogue formatting (em-dashes), and consistent paragraph structures.
*   **Blazing Fast Search**: Integrated Pagefind for instant, client-side search across all authors and works.
*   **SEO Optimized**: Semantic HTML and optimized metadata for better discoverability.

## 🏗️ Project Architecture

The project is divided into three main components:

### 1. Scraper (`/scraper`)
A Python-based utility that extracts content from the original `literatura.us` website. It uses `BeautifulSoup` and `requests` to navigate and scrape stories, saving the data into structured YAML files.

### 2. Formatters (`/semantic_formatter`, `/heuristic_formatter`)
Automated pipelines to clean and format the scraped raw text:
*   **Semantic Formatter**: Uses AI (Gemini API) and heuristic rules to convert plain text into beautiful markdown, handling Spanish dialogue conventions and narrative flow.
*   **Audit Tools**: Scripts to verify the integrity and formatting of the processed texts.

### 3. Site (`/site`)
The frontend built with **11ty (Eleventy)**:
-   **Templating**: Nunjucks-based layouts.
-   **Styling**: Tailwind CSS for a modern, responsive design.
-   **Images**: Optimized using `@11ty/eleventy-img`.
-   **Search**: Powered by Pagefind.

## 🛠️ Technology Stack

-   **Frontend**: 11ty, Nunjucks, Tailwind CSS, Pagefind.
-   **Backend/Tools**: Python, YAML.
-   **AI**: Gemini Pro (for semantic formatting).

## 📂 Directory Structure

-   `site/`: The main Eleventy project.
-   `scraper/`: Python scripts for data extraction.
-   `semantic_formatter/`: AI and rule-based text processing tools.
-   `heuristic_formatter/`: Pattern-based text cleaning tools.

---

*This project is dedicated to making classic literature accessible and enjoyable in the digital age.*

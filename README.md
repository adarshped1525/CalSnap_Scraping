🔍 Project Context – CalBurn (AI-Powered Health Assistant)

This web scraping and image dataset collection task forms a foundational component of CalBurn, a group project that leverages AI and Data Science to promote personalized health and nutrition. CalBurn is a smart application where users can upload a photo of their food plate. The system detects and classifies food items using computer vision and estimates nutritional content using curated datasets.

From a data science perspective, this task involves:

    Web scraping structured food item names from reliable sources (e.g., Health Canada) to build an initial taxonomy of common fruits and vegetables.
    Automated image data collection using Google Images Search API to build a visual dataset for training object detection models (e.g., YOLO, Faster R-CNN).
    Creating clean, labeled datasets to support downstream machine learning tasks such as image classification, segmentation, and nutrient estimation.

The extracted insights will later be cross-referenced with the user's medical profile to generate AI-driven recommendations for exercises and personalized diet plans — enabling a data-driven, health-aware lifestyle assistant.

BeautifulSoup web scraping script that extracts fruits and vegetables information from the Health Canada website. This is the companion script to your image downloader.
🥕 Web Scraper for Fruits and Vegetables (Health Canada)

This Python script uses BeautifulSoup to scrape fruits and vegetables data from the official Health Canada website:

📎 URL: https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/nutrient-value-some-common-foods-2008.html#a8

The extracted data is saved in an Excel file for later use in applications like dataset creation or image scraping (e.g., using the Google Image Search script).
📋 Features

    Extracts fruit and vegetable names from structured tables on the official Canada Health page.
    Cleans and organizes the data into separate columns.
    Saves the output to an Excel file compatible with other scripts.
    Designed to work reliably with HTML tables using BeautifulSoup.

📁 Output Format

The resulting Excel file (List.xlsx) will contain:
Fruits 	Vegetables
Apple, raw 	Carrot, raw
Banana, raw 	Spinach, raw
... 	...

This file can be directly used in the Google Images Downloader script to collect training data.
🧰 Requirements

    Python 3.6+
    Required Python packages:

pip install requests beautifulsoup4 pandas openpyxl

🔍 How It Works

    Fetches HTML content from the Health Canada nutrient page.
    Parses the section labeled A.8 Vegetables and Fruit.
    Identifies and separates fruit and vegetable entries based on structure and text.
    Outputs cleaned data into an Excel file.

💻 Example Code Summary

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/nutrient-value-some-common-foods-2008.html#a8'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Custom logic to extract fruits and vegetables goes here...

You can build out the full logic to find the appropriate section using heading tags and scrape the respective <table> content.
✅ Usage

Just run the script:

python fruits_vegetables_scraper.py

The script will create an Excel file:

List.xlsx

📎 Related

You can use this file directly with:

📁 google_images_downloader.py — your image scraping script that uses these categories to download training data.
⚠️ Disclaimer

Data is sourced from a government website and is intended for non-commercial, educational, and research use only. Please verify the information periodically in case the website structure changes.
🧾 License

Open for educational use. Attribution appreciated if reused in projects.

Let me know if you’d like to generate the script itself for this scraper or link both projects in a single repository.

This file explains the web scraping script using the google_images_search library. It explains the purpose, setup, usage, and customization:
🔎 Google Image Scraper for Fruits & Vegetables

This script automates the process of downloading images of fruits and vegetables from Google Images using the google_images_search Python library. It's particularly useful for collecting image datasets for machine learning, computer vision, or educational purposes.
📂 Features

    Searches for and downloads images based on names listed in an Excel file.
    Separates fruits and vegetables into different directories.
    Handles retries, sanitization of filenames, and logging.
    Includes optional image filters like size, type, and file format.

📋 Requirements

    Python 3.6+
    A Google Cloud API key and a Custom Search Engine (CSE) ID
    Required Python packages (see below)

🔧 Installation

    Install required libraries:

pip install google_images_search pandas openpyxl

    openpyxl is required for reading .xlsx files with pandas.

    Set up Google Custom Search Engine:

    Go to Google Custom Search
    Create a search engine and enable "Image Search"
    Get your API key from the Google Cloud Console

📁 Directory Structure

Image_Data/
├── Fruits/
│   ├── Apple/
│   ├── Banana/
│   └── ...
└── Vegetables/
    ├── Carrot/
    ├── Tomato/
    └── ...

🧠 How It Works

    Reads from an Excel file with two columns: Fruits and Vegetables.
    Uses the google_images_search API to find and download images.
    Saves images to designated folders with proper sanitization and logging.

✏️ Usage
1. Update Your API Keys

Replace the placeholders in the script:

API_KEY = 'YOUR_API_KEY'
CX = 'YOUR_CUSTOM_SEARCH_ENGINE_ID'

2. Prepare Your Excel File

Make sure your Excel file (List.xlsx) looks like this:
Fruits 	Vegetables
Apple 	Carrot
Banana 	Tomato
... 	...
3. Run the Script

python image_downloader.py

    It will automatically create folders and download up to 10 images per item.

🛠️ Customization

You can tweak the following parameters in the script:

    max_images: Number of images per item
    imgSize, fileType, safe: Google image search filters
    base_fruit_directory, base_vegetable_directory: Output paths

🐛 Logging

All events (successes, warnings, errors) are logged to image_downloader.log for debugging and tracking.
⚠️ Limitations

    Google Search Quota: You may hit the API quota limit. The script includes retry and wait logic for quota errors.
    Duplicate Images: Basic filtering is applied using image URLs, but duplicates may still occur.

🧾 License

This project is for educational and non-commercial use. Make sure to comply with image usage rights and Google’s API terms.



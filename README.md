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


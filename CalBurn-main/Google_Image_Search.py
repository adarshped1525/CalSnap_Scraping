from google_images_search import GoogleImagesSearch
import os
import pandas as pd
import re
import time
import random
import logging

# Replace with your actual API key and search engine ID
API_KEY = 'AIzaSyDGorF-fteDwC3d-cl6S7TrCRSeJfjnagk'  # Replace with your API key
CX = 'a6c62a3ef9c854e96'  # Replace with your Custom Search Engine ID

# Create a GoogleImagesSearch object
gis = GoogleImagesSearch(API_KEY, CX)

# Set up logging
logging.basicConfig(filename='image_downloader.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load the Excel file
file_path = r'C:\Users\moksh\OneDrive\Documents\OneDrive\Desktop\LCIT\Term 2\AISC2006 - Step Presentation (Step 2)\Scraped_Dummy_Data\Attributes_Data\List.xlsx'
data = pd.read_excel(file_path)

# Assuming the Excel file has two columns: 'Fruits' and 'Vegetables'
fruits = data['Fruits'].dropna().tolist()      # List of fruits
vegetables = data['Vegetables'].dropna().tolist()  # List of vegetables

# Set your target directories for fruits and vegetables
base_fruit_directory = r'C:\Users\moksh\Downloads\Image_Data\Fruits'
base_vegetable_directory = r'C:\Users\moksh\Downloads\Image_Data\Vegetables'

# Ensure the directories exist
os.makedirs(base_fruit_directory, exist_ok=True)
os.makedirs(base_vegetable_directory, exist_ok=True)

# Function to sanitize item names
def sanitize_name(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip()

# Function to sanitize and truncate filenames
def sanitize_filename(filename, max_length=200):
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename).strip()
    filename = filename.replace(',', '_')  # Replace commas with underscores
    return filename[:max_length]

# Function to search and download images for a given list of items
def download_images(item_list, base_directory, is_fruit=True, max_images=10):
    for item in item_list:
        sanitized_item = sanitize_name(item)
        item_directory = os.path.join(base_directory, sanitized_item)
        os.makedirs(item_directory, exist_ok=True)

        logging.info(f"\nSearching for images of: {item}\n")
        print(f"\nSearching for images of: {item}\n")

        search_term = f"{item} fruit" if is_fruit else f"{item} vegetable"
        search_params = {
            'q': search_term,
            'num': max_images,
            'safe': 'medium',
            'imgType': 'photo',
            'imgSize': 'medium',  # Additional parameter for image size
            'fileType': 'jpg'     # Additional parameter for file type
        }

        # Initialize retry parameters
        retries = 3
        wait_time = 1

        for attempt in range(retries):
            try:
                gis.search(search_params=search_params)
                time.sleep(wait_time)  # Pause between requests
                break  # Exit the retry loop if successful
            except Exception as e:
                logging.error(f"Attempt {attempt + 1}: Error during search for {item}: {e}")
                print(f"Attempt {attempt + 1}: Error during search for {item}: {e}")
                if "Quota exceeded" in str(e):
                    print("Quota exceeded. Waiting for 60 seconds...\n")
                    time.sleep(60)  # Wait for 60 seconds if quota exceeded
                    break  # Exit the retry loop after handling quota error
                wait_time *= 2  # Exponential backoff strategy
                time.sleep(wait_time)

        # Check if images were found
        if len(gis.results()) == 0:
            logging.warning(f"No images found for: {item}\n")
            print(f"No images found for: {item}\n")
            continue

        unique_image_urls = set()
        for image in gis.results():
            if image.url in unique_image_urls:
                continue
            
            unique_image_urls.add(image.url)
            image_filename = sanitize_filename(image.url.split('/')[-1])
            logging.info(f"Sanitized filename: {image_filename}\n")
            print(f"Sanitized filename: {image_filename}\n")
            try:
                image.download(item_directory)
                logging.info(f"Downloaded {image_filename} to {item_directory}\n")
                print(f"Downloaded {image_filename} to {item_directory}\n")
                if len(unique_image_urls) >= max_images:  # Check if max_images reached
                    break  # Stop downloading once we reach the max count
            except Exception as e:
                logging.error(f"Error downloading {image_filename}: {e}\n")
                print(f"Error downloading {image_filename}: {e}\n")

        time.sleep(random.uniform(1, 3))  # Sleep between 1 to 3 seconds

# Download images for fruits and vegetables
download_images(fruits, base_fruit_directory, is_fruit=True)
download_images(vegetables, base_vegetable_directory, is_fruit=False)

print(f"\nFruit images downloaded to: {base_fruit_directory}\n")
print(f"Vegetable images downloaded to: {base_vegetable_directory}\n")

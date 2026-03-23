# Configuration settings for the Google Places scraper

# Define the base URL for the Google Places API
BASE_URL = 'https://maps.googleapis.com/maps/api/place'

# API Key for authentication
API_KEY = 'YOUR_API_KEY_HERE'

# Specify the types of places to search
PLACE_TYPES = ['restaurant', 'cafe', 'bar']

# Distance (in meters) to search around the location
RADIUS = 500

# File to save the scraped data
OUTPUT_FILE = 'scraper_results.json'
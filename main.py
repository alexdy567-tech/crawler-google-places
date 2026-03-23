import requests

# Google Places API key
API_KEY = 'YOUR_API_KEY'

# Function to get places

def get_places(location, radius=1500, type='restaurant'):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={{location}}&radius={{radius}}&type={{type}}&key={{API_KEY}}'
    response = requests.get(url)
    return response.json()

# Example usage

if __name__ == '__main__':
    location = '37.7749,-122.4194'  # San Francisco coordinates
    places = get_places(location)
    print(places)
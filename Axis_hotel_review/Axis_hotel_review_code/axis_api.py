import requests
import csv
from dotenv import load_dotenv
import os
import praw
import googlemaps
import pandas as pd

load_dotenv()  # Load environment variables from .env
API_KEY = os.getenv("MAPS_API_KEY")

gmaps = googlemaps.Client(key=API_KEY)

viana_axis_hotel = 'AXIS VIANA BUSINESS & SPA HOTEL'
ponte_lima_axis_hotel = 'Axis Ponte de Lima Golf Resort Hotel'
ofir_axis_hotel = 'Axis Ofir Beach Resort Hotel'
braga_axis_hotel = 'Basic Braga by Axis'
vermar_axis_hotel = 'Hotel Axis Vermar Conference & Beach Hotel'
porto_axis_hotel = 'Axis Porto Business & SPA Hotel'
porto_club_axis_hotel = 'Axis Porto Club Hotel'

def get_hotel_reviews(hotel_name, api_key):
    """Fetches all reviews for a hotel using the Google Places API, handling pagination."""
    place_id = gmaps.find_place(input=hotel_name, input_type='textquery', fields=['place_id'])['candidates'][0]['place_id']
    all_reviews = []
    next_page_token = None

    while True:
        place_details = gmaps.place(place_id, fields=['name', 'reviews'])
        reviews = place_details['result']['reviews']
        all_reviews.extend(reviews)

        if 'next_page_token' in place_details['result']:
            next_page_token = place_details['result']['next_page_token']
        else:
            break

    return all_reviews

def save_reviews_to_csv(reviews, file_name):
    """Saves hotel reviews to a CSV file."""
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Review'])  # Write header row
        for review in reviews:
            writer.writerow([review['text']])  # Write each review as a row

# Example usage
viana_reviews = get_hotel_reviews(viana_axis_hotel, API_KEY)
save_reviews_to_csv(viana_reviews, 'viana_reviews.csv')

ponte_lima_reviews = get_hotel_reviews(ponte_lima_axis_hotel, API_KEY)
save_reviews_to_csv(ponte_lima_reviews, 'ponte_lima_reviews.csv')

ofir_reviews = get_hotel_reviews(ofir_axis_hotel, API_KEY)
save_reviews_to_csv(ofir_reviews, 'ofir_reviews.csv')

braga_reviews = get_hotel_reviews(braga_axis_hotel, API_KEY)
save_reviews_to_csv(braga_reviews, 'braga_reviews.csv')

vermar_reviews = get_hotel_reviews(vermar_axis_hotel, API_KEY)
save_reviews_to_csv(vermar_reviews, 'vermar_reviews.csv')

porto_business_reviews = get_hotel_reviews(porto_axis_hotel, API_KEY)
save_reviews_to_csv(porto_business_reviews, 'porto_business_reviews.csv')

porto_club_reviews = get_hotel_reviews(porto_club_axis_hotel, API_KEY)
save_reviews_to_csv(porto_club_reviews, 'porto_club_reviews.csv')

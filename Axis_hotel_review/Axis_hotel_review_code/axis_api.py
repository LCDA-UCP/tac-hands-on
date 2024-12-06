import requests
import csv
from dotenv import load_dotenv
import os
import praw
import googlemaps
import pandas as pd


load_dotenv
API_KEY = os.getenv("MAPS_API_KEY")

gmaps = googlemaps.Client(key=API_KEY)

viana_axis_hotel = 'AXIS VIANA BUSINESS & SPA HOTEL'
ponte_lima_axis_hotel = 'Axis Ponte de Lima Golf Resort Hotel'
ofir_axis_hotel = 'Axis Ofir Beach Resort Hotel'
braga_axis_hotel = 'Basic Braga by Axis'
vermar_axis_hotel = 'Hotel Axis Vermar Conference & Beach Hotel'
porto_axis_hotel = 'Axis Porto Business & SPA Hotel'
porto_club_axis_hotel = 'Axis Porto Club Hotel'

viana_details = gmaps.places(viana_axis_hotel)
ponte_lima_details = gmaps.places(ponte_lima_axis_hotel)
ofir_details = gmaps.places(ofir_axis_hotel)
braga_details = gmaps.places(braga_axis_hotel)
vermar_axis_hotel = gmaps.places(vermar_axis_hotel)
porto_business_details = gmaps.places(porto_axis_hotel)
porto_club_details = gmaps.places(porto_club_axis_hotel)


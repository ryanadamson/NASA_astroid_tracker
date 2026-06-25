from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
NASA_API_KEY = os.getenv("NASA_API_KEY")

@app.get("/api/asteroids")
def get_asteroids():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={NASA_API_KEY}"
    response = requests.get(url)  # was response.get(url)
    data = response.json()  # was response.json (missing brackets)
    
    asteroids = []
    for date, items in data["near_earth_objects"].items():
        for a in items:  # you were missing this loop!
            asteroids.append({
                "name": a["name"],
                "date": date,
                "diameter_m": round(a["estimated_diameter"]["meters"]["estimated_diameter_max"]),
                "hazardous": a["is_potentially_hazardous_asteroid"],  # typo fixed
                "miss_distance_km": round(float(a["close_approach_data"][0]["miss_distance"]["kilometers"]))
            })
    
    return sorted(asteroids, key=lambda x: x["miss_distance_km"])

app.mount("/", StaticFiles(directory="static", html=True), name="static")
# 🌍 NASA Asteroid Tracker

A real-time web app that tracks near-Earth asteroids passing by this week, built with Python and the NASA NeoWs API.

## What it does

- Fetches live asteroid data from NASA's Near Earth Object Web Service (NeoWs)
- Displays all asteroids passing close to Earth in the next 7 days
- Sorts by closest miss distance so the most interesting ones are first
- Flags potentially hazardous asteroids with a warning badge
- Shows diameter and miss distance for each object

## Tech Stack

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **API:** NASA NeoWs (Near Earth Object Web Service)
- **Deployment:** Railway

## Running locally

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
```
3. Get a free NASA API key at https://api.nasa.gov
4. Create a `.env` file:

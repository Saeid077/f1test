import os
import urllib.request

# --- CONFIGURATION ---
BASE_DIR = "static/img"
FOLDERS = [
    "drivers/avatar",
    "drivers/landscape",
    "teams/logo",
    "teams/car"
]

# (Filename, URL)
IMAGES = [
    # --- DRIVERS (AVATAR - IN SUITS) ---
    ("drivers/avatar/max-verstappen.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Max_Verstappen_2024_China_Portrait.jpg/600px-Max_Verstappen_2024_China_Portrait.jpg"),
    ("drivers/avatar/lando-norris.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Lando_Norris_2024_China_Portrait.jpg/600px-Lando_Norris_2024_China_Portrait.jpg"),
    ("drivers/avatar/lewis-hamilton.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Lewis_Hamilton_2024_China_Portrait.jpg/600px-Lewis_Hamilton_2024_China_Portrait.jpg"),
    ("drivers/avatar/charles-leclerc.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Charles_Leclerc_2024_China_Portrait.jpg/600px-Charles_Leclerc_2024_China_Portrait.jpg"),
    ("drivers/avatar/george-russell.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/George_Russell_2024_China_Portrait.jpg/600px-George_Russell_2024_China_Portrait.jpg"),
    ("drivers/avatar/oscar-piastri.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Oscar_Piastri_2024.jpg/600px-Oscar_Piastri_2024.jpg"),
    ("drivers/avatar/fernando-alonso.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Fernando_Alonso_2024.jpg/600px-Fernando_Alonso_2024.jpg"),
    ("drivers/avatar/carlos-sainz.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Carlos_Sainz_Jr._2024.jpg/600px-Carlos_Sainz_Jr._2024.jpg"),
    ("drivers/avatar/nico-hulkenberg.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Nico_Hulkenberg_2024.jpg/600px-Nico_Hulkenberg_2024.jpg"),
    ("drivers/avatar/alex-albon.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Alex_Albon_2024.jpg/600px-Alex_Albon_2024.jpg"),
    
    # --- TEAMS (LOGOS) ---
    ("teams/logo/ferrari.png", "https://upload.wikimedia.org/wikipedia/de/thumb/c/c0/Scuderia_Ferrari_Logo.svg/500px-Scuderia_Ferrari_Logo.svg.png"),
    ("teams/logo/mclaren.png", "https://upload.wikimedia.org/wikipedia/en/thumb/6/66/McLaren_Racing_logo.svg/500px-McLaren_Racing_logo.svg.png"),
    ("teams/logo/red-bull.png", "https://upload.wikimedia.org/wikipedia/en/thumb/4/41/Red_Bull_Racing_logo.svg/500px-Red_Bull_Racing_logo.svg.png"),
    ("teams/logo/mercedes.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg/500px-Mercedes_AMG_Petronas_F1_Logo.svg.png"),
    ("teams/logo/aston-martin.png", "https://upload.wikimedia.org/wikipedia/fr/thumb/7/72/Aston_Martin_Aramco_Cognizant_F1.svg/500px-Aston_Martin_Aramco_Cognizant_F1.svg.png"),
    ("teams/logo/alpine.png", "https://upload.wikimedia.org/wikipedia/fr/thumb/6/60/Alpine_F1_Team_2021_Logo.svg/500px-Alpine_F1_Team_2021_Logo.svg.png"),
    ("teams/logo/williams.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e8/Williams_Racing_2020_logo.png/500px-Williams_Racing_2020_logo.png"),
    ("teams/logo/audi.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/92/Audi-Logo_2016.svg/500px-Audi-Logo_2016.svg.png"),
    ("teams/logo/haas.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Logo_Haas_F1.png/500px-Logo_Haas_F1.png"),
    ("teams/logo/cadillac.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Cadillac_logo.svg/500px-Cadillac_logo.svg.png"),

    # --- LANDSCAPES (CARS/ACTION) ---
    ("teams/car/ferrari.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Ferrari_SF-24_of_Leclerc%2C_2024_Chinese_Grand_Prix.jpg/800px-Ferrari_SF-24_of_Leclerc%2C_2024_Chinese_Grand_Prix.jpg"),
    ("teams/car/red-bull.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Max_Verstappen%2C_2024_Chinese_Grand_Prix_%2853677569100%29.jpg/800px-Max_Verstappen%2C_2024_Chinese_Grand_Prix_%2853677569100%29.jpg"),
    ("teams/car/mclaren.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Lando_Norris%2C_2024_Chinese_Grand_Prix_%2853676237242%29.jpg/800px-Lando_Norris%2C_2024_Chinese_Grand_Prix_%2853676237242%29.jpg"),
    ("teams/car/mercedes.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/George_Russell%2C_2024_Chinese_Grand_Prix_%2853677353916%29.jpg/800px-George_Russell%2C_2024_Chinese_Grand_Prix_%2853677353916%29.jpg"),
]

def setup():
    # 1. Create Folders
    for folder in FOLDERS:
        path = os.path.join(BASE_DIR, folder)
        os.makedirs(path, exist_ok=True)
        print(f"📂 Verified folder: {path}")

    # 2. Download Images
    print("⬇️  Downloading images... (This might take a minute)")
    headers = {'User-Agent': 'Mozilla/5.0'} # Fake browser to bypass some blocks

    for filename, url in IMAGES:
        save_path = os.path.join(BASE_DIR, filename)
        if not os.path.exists(save_path):
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
                    out_file.write(response.read())
                print(f"✅ Downloaded: {filename}")
            except Exception as e:
                print(f"❌ Failed to download {filename}: {e}")
        else:
            print(f"⚡ Exists: {filename}")

if __name__ == "__main__":
    setup()
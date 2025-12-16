import sqlite3

# --- 2026 TEAMS DATA ---
# (Rank, Name, Full Name, Color, Logo URL, Car URL)
TEAMS_DATA = [
    (1, "Ferrari", "Scuderia Ferrari HP", "#E80020", 
     "https://upload.wikimedia.org/wikipedia/de/c/c0/Scuderia_Ferrari_Logo.svg",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/ferrari.png.transform/2col/image.png"),
    
    (2, "McLaren", "McLaren F1 Team", "#FF8000", 
     "https://upload.wikimedia.org/wikipedia/en/6/66/McLaren_Racing_logo.svg",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/mclaren.png.transform/2col/image.png"),
    
    (3, "Red Bull", "Red Bull Ford", "#3671C6", 
     "https://i.redd.it/e3a3aakmjm701.jpg",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/red-bull-racing.png.transform/2col/image.png"),
    
    (4, "Mercedes", "Mercedes-AMG Petronas", "#27F4D2", 
     "https://upload.wikimedia.org/wikipedia/commons/f/fb/Mercedes_AMG_Petronas_F1_Logo.svg",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/mercedes.png.transform/2col/image.png"),
    
    (5, "Aston Martin", "Aston Martin Aramco", "#229971", 
     "https://media.formula1.com/image/upload/c_lfill,w_3392/q_auto/v1740000000/content/dam/fom-website/manual/Misc/2021preseason/Aston-Martin-logo.webp",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/aston-martin.png.transform/2col/image.png"),
    
    (6, "Alpine", "BWT Alpine F1 Team", "#0093cc", 
     "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Alpine_F1_Team_Logo.svg/1200px-Alpine_F1_Team_Logo.svg.png",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/alpine.png.transform/2col/image.png"),
    
    (7, "Williams", "Williams Racing", "#64C4FF", 
     "https://upload.wikimedia.org/wikipedia/commons/e/e8/Williams_Racing_2020_logo.png",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/williams.png.transform/2col/image.png"),
    
    (8, "RB", "Visa Cash App RB", "#6692FF", 
     "https://www.vantage97.com/cdn/shop/collections/1582650557134.jpg?crop=center&height=500&v=1709396901&width=600",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/rb.png.transform/2col/image.png"),
    
    (9, "Audi", "Audi F1 Team", "#F5F5F5", 
     "https://upload.wikimedia.org/wikipedia/commons/9/92/Audi-Logo_2016.svg",
     "https://robbreport.com/wp-content/uploads/2022/08/AudiF1.jpg?w=1000"), # Audi Concept Car
    
    (10, "Haas", "MoneyGram Haas F1 Team", "#B6BABD", 
     "https://upload.wikimedia.org/wikipedia/commons/d/d4/Logo_Haas_F1.png",
     "https://media.formula1.com/d_team_car_fallback_image.png/content/dam/fom-website/teams/2025/haas-f1-team.png.transform/2col/image.png"),
    
    (11, "Cadillac", "Cadillac F1 Team", "#FFD700", 
     "https://images.cults3d.com/3005JpOC5o3SyTdse4pLo30sElU=/516x516/filters:no_upscale():format(webp)/https://fbi.cults3d.com/uploaders/41446188/illustration-file/824144c9-da78-4abd-aebe-aad2ce3a349d/CADILLAC-F1-TEAM.jpg",
     "https://unn.ua/_next/image?url=https%3A%2F%2Funn.ua%2Fimg%2F2025%2F09%2F19%2F1758277108-3101-large.webp&w=720&q=75") # Cadillac Hypercar Concept
]

# --- 2026 DRIVERS DATA ---
DRIVERS_DATA = [
    # RED BULL
    ("Max Verstappen", 1, "Red Bull", "#3671C6", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/verstappen.png.transform/2col/image.png"),
    ("Isack Hadjar", 6, "Red Bull", "#3671C6", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSPMwNM82kpKUvkfmsrZWUCi8-pcPj3Q9lDZg&s"), # WIKI
    
    # MCLAREN
    ("Lando Norris", 4, "McLaren", "#FF8000", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/norris.png.transform/2col/image.png"),
    ("Oscar Piastri", 81, "McLaren", "#FF8000", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/piastri.png.transform/2col/image.png"),
    
    # FERRARI
    ("Lewis Hamilton", 44, "Ferrari", "#E80020", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/hamilton.png.transform/2col/image.png"),
    ("Charles Leclerc", 16, "Ferrari", "#E80020", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/leclerc.png.transform/2col/image.png"),
    
    # MERCEDES
    ("George Russell", 63, "Mercedes", "#27F4D2", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/russell.png.transform/2col/image.png"),
    ("Kimi Antonelli", 12, "Mercedes", "#27F4D2", "https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/mercedes/andant01/2025mercedesandant01right.webp"), # WIKI
    
    # ASTON MARTIN
    ("Fernando Alonso", 14, "Aston Martin", "#229971", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/alonso.png.transform/2col/image.png"),
    ("Lance Stroll", 18, "Aston Martin", "#229971", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/stroll.png.transform/2col/image.png"),
    
    # ALPINE
    ("Pierre Gasly", 10, "Alpine", "#0093cc", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/gasly.png.transform/2col/image.png"),
    ("Franco Colapinto", 43, "Alpine", "#0093cc", "https://media.formula1.com/image/upload/c_fill,w_720/q_auto/v1740000000/common/f1/2025/alpine/fracol01/2025alpinefracol01right.webp"),
    
    # WILLIAMS
    ("Carlos Sainz", 55, "Williams", "#64C4FF", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/sainz.png.transform/2col/image.png"),
    ("Alex Albon", 23, "Williams", "#64C4FF", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/albon.png.transform/2col/image.png"),
    
    # HAAS
    ("Esteban Ocon", 31, "Haas", "#B6BABD", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/ocon.png.transform/2col/image.png"),
    ("Oliver Bearman", 87, "Haas", "#B6BABD", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/bearman.png.transform/2col/image.png"),
    
    # RB
    ("Liam Lawson", 30, "RB", "#6692FF", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/lawson.png.transform/2col/image.png"),
    ("Arvid Lindblad", 24, "RB", "#6692FF", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBq5tRbbLq5GUFTXc3I1Kpv6h4PG_YiUnl3Q&s"), # WIKI (Car shot as placeholder for rookie)
    
    # AUDI
    ("Nico Hulkenberg", 27, "Audi", "#F5F5F5", "https://media.formula1.com/content/dam/fom-website/drivers/2025Drivers/hulkenberg.png.transform/2col/image.png"),
    ("Gabriel Bortoleto", 5, "Audi", "#F5F5F5", "data:image/jpeg;base64,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"), # WIKI
    
    # CADILLAC
    ("Sergio Perez", 11, "Cadillac", "#FFD700", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0X_5cCKlMEJcT3aeQyzZl8LjTx-jShHSbEw&s   "), # WIKI (In car)
    ("Valtteri Bottas", 77, "Cadillac", "#FFD700", "https://www.formulaonehistory.com/wp-content/uploads/2023/10/Valtteri-Bottas-Cadillac.webp") # WIKI (In car)
]

def create_db():
    conn = sqlite3.connect('f1_2026.db')
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS drivers")
    cursor.execute("""
        CREATE TABLE drivers (
            id INTEGER PRIMARY KEY,
            name TEXT, number INTEGER, team TEXT, color TEXT,
            avatar_url TEXT
        )
    """)
    
    cursor.execute("DROP TABLE IF EXISTS teams")
    cursor.execute("""
        CREATE TABLE teams (
            id INTEGER PRIMARY KEY,
            name TEXT, full_name TEXT, color TEXT,
            logo_url TEXT, car_url TEXT
        )
    """)
    
    cursor.executemany("INSERT INTO drivers (name, number, team, color, avatar_url) VALUES (?,?,?,?,?)", DRIVERS_DATA)
    cursor.executemany("INSERT INTO teams (id, name, full_name, color, logo_url, car_url) VALUES (?,?,?,?,?,?)", TEAMS_DATA)
    
    conn.commit()
    conn.close()
    print("✅ SUCCESS: Database updated with Working Images!")

if __name__ == '__main__':
    create_db()
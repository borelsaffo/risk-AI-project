import time, os, requests, random
# Simple worker that simulates fetching data, computing features, and calling the API
API_URL = os.environ.get("API_URL", "http://api:8000/scoring")

def simulate_asset_event():
    payload = {
        "vuln_score": round(random.uniform(0,10),2),
        "criticalite": random.randint(1,5),
        "exposition": random.choice([0,1]),
        "historique_incident": random.randint(0,5)
    }
    return payload

def main_loop():
    print("Worker started - sending test scoring requests to API")
    while True:
        payload = simulate_asset_event()
        try:
            r = requests.post(API_URL, json=payload, timeout=10)
            print("Payload:", payload, "=>", r.json())
        except Exception as e:
            print("Error calling API:", e)
        time.sleep(5)

if __name__ == '__main__':
    main_loop()

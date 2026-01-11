import csv
import logging
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://appuser:apppassword@db:5432/appdb"
)

OUTPUT_DIR = "/seed_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(OUTPUT_DIR, "seed.log"),
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

engine = create_engine(DATABASE_URL)

USERS = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "Diana", "email": "diana@example.com"},
    {"name": "Eve", "email": "eve@example.com"},
]

def main():
    with engine.begin() as conn:
        for user in USERS:
            conn.execute(
                text(
                    "INSERT INTO users (name, email) VALUES (:name, :email)"
                ),
                user,
            )
            logging.info(f"Inserted user {user['email']}")

    csv_path = os.path.join(OUTPUT_DIR, "users.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email"])
        writer.writeheader()
        writer.writerows(USERS)

    logging.info("Seeding completed successfully")

if __name__ == "__main__":
    main()

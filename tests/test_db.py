from backend.database.database import engine
from sqlalchemy import text

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT version();"))
        print("Connected Successfully!")
        print(result.fetchone()[0])
except Exception as e:
    print("Connection Failed!")
    print(e)
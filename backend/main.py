from fastapi import FastAPI
from database import get_connection

app = FastAPI(title="Lyria OS API")


@app.get("/")
def home():
    return {
        "message": "Welcome to Lyria OS"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/projects")
def projects():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, description, created_at
        FROM projects
        ORDER BY id;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "created_at": row[3],
        }
        for row in rows
    ]
from fastapi import FastAPI
from database import get_connection
from schemas.project import ProjectCreate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lyria OS API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.post("/projects")
def create_project(project: ProjectCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO projects (name, description)
        VALUES (%s, %s)
        """,
        (project.name, project.description),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Proyecto creado"}
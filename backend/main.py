from fastapi import FastAPI
from database import get_connection
from schemas.project import ProjectCreate
from fastapi.middleware.cors import CORSMiddleware
from schemas.memory import MemoryUpdate
from schemas.decision import DecisionCreate
from schemas.chat import ChatMessage
from services.orchestrator import process_message

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

@app.get("/projects/{project_id}/memory")
def get_project_memory(project_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            p.id,
            p.name,
            p.description,
            m.goal,
            m.architecture,
            m.tech_stack,
            m.decisions,
            m.conventions
        FROM projects p
        JOIN project_memory m
            ON p.id = m.project_id
        WHERE p.id = %s
        """,
        (project_id,),
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        return {"error": "Proyecto no encontrado"}

    return {
        "id": row[0],
        "name": row[1],
        "description": row[2],
        "goal": row[3],
        "architecture": row[4],
        "tech_stack": row[5],
        "decisions": row[6],
        "conventions": row[7],
    }

@app.put("/projects/{project_id}/memory")
def update_memory(project_id: int, memory: MemoryUpdate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE project_memory
        SET
            architecture = %s,
            tech_stack = %s,
            decisions = %s,
            conventions = %s,
            updated_at = CURRENT_TIMESTAMP
        WHERE project_id = %s
        """,
        (
            memory.architecture,
            memory.tech_stack,
            memory.decisions,
            memory.conventions,
            project_id,
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Memoria actualizada"}

@app.put("/projects/{project_id}/decision")
def add_decision(project_id: int, body: DecisionCreate):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE project_memory
        SET decisions =
            CASE
                WHEN decisions IS NULL OR decisions = ''
                THEN %s
                ELSE decisions || E'\n• ' || %s
            END,
            updated_at = CURRENT_TIMESTAMP
        WHERE project_id = %s
        """,
        (
            "• " + body.decision,
            body.decision,
            project_id,
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Decisión guardada"}

@app.post("/projects")
def create_project(project: ProjectCreate):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    INSERT INTO projects (name, description)
    VALUES (%s, %s)
    RETURNING id
    """,
    (project.name, project.description),
    )

    project_id = cursor.fetchone()[0]

    cursor.execute(
        """
        INSERT INTO project_memory (
            project_id,
            goal,
            architecture,
            tech_stack
        )
        VALUES (%s, %s, %s, %s)
        """,
        (
            project_id,
            project.goal,
            "Pendiente",
            "Pendiente",
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {
    "id": project_id,
    "message": "Proyecto creado"
}

@app.post("/chat")
def chat(body: ChatMessage):

    reply = process_message(body.message)

    return {
        "reply": reply
    }
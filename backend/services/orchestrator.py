from database import get_connection

def process_message(message: str):

    text = message.lower()

    if "hola" in text:
        return "Hola Cecilia. Soy Lyria."

    if "abre" in text:

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                p.name,
                m.goal,
                m.architecture,
                m.tech_stack
            FROM projects p
            JOIN project_memory m
            ON p.id = m.project_id
            WHERE LOWER(p.name) = LOWER(%s)
        """, (message.replace("Abre ", "").strip(),))

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row:

            return f"""
Proyecto abierto: {row[0]}

Objetivo:
{row[1]}

Arquitectura:
{row[2]}

Stack:
{row[3]}
"""

        return "No encontré ese proyecto."

    return "He recibido tu instrucción."
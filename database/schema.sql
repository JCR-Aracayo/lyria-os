-- Tabla principal de proyectos
CREATE TABLE IF NOT EXISTS projects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Memoria permanente de cada proyecto
CREATE TABLE IF NOT EXISTS project_memory (
    id SERIAL PRIMARY KEY,
    project_id INTEGER UNIQUE REFERENCES projects(id),
    goal TEXT,
    architecture TEXT,
    tech_stack TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
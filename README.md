# Lyria OS

Sistema Operativo de Ingeniería con Agentes IA.

## Visión

Lyria es un Director de Ingeniería Inteligente capaz de coordinar agentes especializados (Frontend, Backend, QA, Security y DevOps) para desarrollar proyectos de software desde una conversación.

Su objetivo no es reemplazar al desarrollador, sino actuar como el orquestador que planifica, recuerda el contexto y delega trabajo a múltiples agentes.

## Estado del proyecto

**Versión actual:** v0.2 — Chat Inteligente + Orquestador

### Roadmap

* [x] Semana 1 — Fundación (Docker + React + FastAPI + PostgreSQL)
* [x] Semana 2 — CRUD de proyectos
* [x] Semana 3 — Memoria persistente de proyectos
* [x] Semana 4 — Chat Inteligente
* [ ] Semana 5 — Orquestador de agentes
* [ ] Semana 6 — Voz y comandos naturales

## Arquitectura

```text
React Chat UI
      │
      ▼
FastAPI API
      │
      ▼
Lyria Core (Orchestrator)
      │
      ▼
PostgreSQL + Project Memory
```

## Funcionalidades implementadas

* Crear y listar proyectos
* Memoria persistente por proyecto
* Actualizar arquitectura, stack y decisiones
* Chat tipo ChatGPT
* Comunicación React ↔ FastAPI (`POST /chat`)
* Apertura de proyectos desde lenguaje natural
* API documentada con Swagger

## Stack tecnológico

| Tecnología      | Uso                          |
| --------------- | ---------------------------- |
| React 19 + Vite | Interfaz de usuario          |
| FastAPI         | API principal                |
| PostgreSQL 17   | Base de datos                |
| Docker Compose  | Desarrollo local             |
| DBeaver         | Administración de PostgreSQL |

## Estructura

```text
lyria-os/
├── frontend/
├── backend/
│   ├── schemas/
│   └── services/
├── database/
├── agents/
├── memory/
├── docs/
└── docker-compose.yml
```

## Próximo objetivo

Construir el sistema de orquestación de agentes para que Lyria pueda delegar tareas a Frontend, Backend y QA de forma inteligente.

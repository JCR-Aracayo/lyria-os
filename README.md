# Lyria OS

Sistema Operativo de Ingeniería con Agentes IA.

## Visión

Lyria es un Director de Ingeniería Inteligente capaz de coordinar agentes especializados (Frontend, Backend, QA, Security y DevOps) para desarrollar proyectos de software desde una conversación.

Su objetivo no es reemplazar al desarrollador, sino actuar como el orquestador que planifica, recuerda el contexto y delega trabajo a múltiples agentes.

## Estado del proyecto

**Versión actual:** v0.1 — Fundación + Memoria Persistente

### Roadmap

* [x] Semana 1 — Fundación (Docker + React + FastAPI + PostgreSQL)
* [x] Semana 2 — CRUD de proyectos
* [x] Semana 3 — Memoria persistente de proyectos
* [ ] Semana 4 — Chat de Lyria
* [ ] Semana 5 — Orquestador de agentes
* [ ] Semana 6 — Voz y comandos naturales

## Arquitectura

```text
Frontend (React + Vite)
        │
        ▼
Backend (FastAPI)
        │
        ▼
PostgreSQL
        │
        ▼
Project Memory
```

## Funcionalidades implementadas

* Crear proyectos
* Listar proyectos
* Memoria persistente por proyecto
* Actualizar arquitectura y stack tecnológico
* Registrar decisiones de ingeniería
* API documentada con Swagger

## Stack tecnológico

| Tecnología     | Uso                                |
| -------------- | ---------------------------------- |
| React + Vite   | Interfaz de usuario                |
| FastAPI        | API principal                      |
| PostgreSQL 17  | Base de datos                      |
| Docker Compose | Orquestación local                 |
| DBeaver        | Administración de la base de datos |

## Estructura

```text
lyria-os/
├── frontend/
├── backend/
├── database/
├── agents/
├── memory/
├── docs/
└── docker-compose.yml
```

## Próximo objetivo

Construir el chat de Lyria para gestionar proyectos desde lenguaje natural y preparar el futuro orquestador de agentes.

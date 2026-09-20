# Lyria OS Frontend

Frontend oficial de Lyria OS desarrollado con React + Vite.

## Objetivo

Proporcionar la interfaz de conversación entre el usuario y Lyria, mostrando proyectos, chat y el estado del orquestador.

## Funcionalidades

* Chat tipo ChatGPT
* Sidebar de proyectos
* Panel de estado
* Comunicación con FastAPI
* Diseño oscuro inspirado en asistentes IA

## Tecnologías

* React 19
* Vite
* React Router
* CSS

## Ejecutar

```bash
npm install
npm run dev
```

Servidor de desarrollo:

```text
http://localhost:5173
```

## Estado

**Versión:** v0.2

Este módulo se comunica con el backend mediante el endpoint `POST /chat` y constituye la interfaz principal de Lyria Core.

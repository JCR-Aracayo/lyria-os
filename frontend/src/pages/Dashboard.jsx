import { useEffect, useState } from "react";

export default function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    async function fetchProjects() {
      const response = await fetch("http://localhost:8000/projects");
      const data = await response.json();
      setProjects(data);
    }

    fetchProjects();
  }, []);

  async function createProject() {
    await fetch("http://localhost:8000/projects", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name,
        description,
      }),
    });

    const response = await fetch("http://localhost:8000/projects");
    const data = await response.json();

    setProjects(data);

    setName("");
    setDescription("");
  }

  return (
    <section>
      <h2>Dashboard</h2>

      <div className="card">
        <h3>Nuevo proyecto</h3>

        <input
          placeholder="Nombre del proyecto"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />

        <textarea
          placeholder="Descripción"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />

        <button onClick={createProject}>
          Crear proyecto
        </button>
      </div>

      <div className="card">
        <h3>Proyectos</h3>

        {projects.map((project) => (
          <div key={project.id}>
            <h4>{project.name}</h4>
            <p>{project.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
import { NavLink } from "react-router-dom";

export default function Sidebar() {
  return (
    <aside className="sidebar">
      <h1 className="logo">Lyria OS</h1>

      <p className="sidebar-title">PROYECTOS</p>

      <nav>
        <NavLink to="/">ERP Pastelería</NavLink>
        <NavLink to="/">Speaking AI</NavLink>
        <NavLink to="/">Lyria OS</NavLink>
      </nav>

      <button className="new-project">
        + Nuevo proyecto
      </button>
    </aside>
  );
}
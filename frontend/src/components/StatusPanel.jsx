export default function StatusPanel() {
  return (
    <aside className="status-panel">
      <h3>Estado</h3>

      <div className="status-card">
        <p>Proyecto activo</p>
        <strong>ERP Pastelería</strong>
      </div>

      <div className="status-card">
        <p>Orquestador</p>
        <span className="online">● En línea</span>
      </div>

      <div className="status-card">
        <p>Agentes</p>
        <small>Frontend · Backend · QA</small>
      </div>
    </aside>
  );
}
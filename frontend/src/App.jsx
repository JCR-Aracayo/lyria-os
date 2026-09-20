import { Routes, Route } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import StatusPanel from "./components/StatusPanel";
import Chat from "./pages/Chat";

export default function App() {
  return (
    <div className="layout">
      <Sidebar />

      <main className="main-content">
        <Routes>
          <Route path="/" element={<Chat />} />
        </Routes>
      </main>

      <StatusPanel />
    </div>
  );
}
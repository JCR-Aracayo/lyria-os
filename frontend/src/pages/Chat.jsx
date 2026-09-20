import { useState } from "react";

export default function Chat() {
  const [input, setInput] = useState("");

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hola Cecilia. Soy Lyria, tu Director de Ingeniería."
    }
  ]);

  const [loading, setLoading] = useState(false);

async function sendMessage() {

    if (!input.trim()) return;

    const userMessage = {
        role: "user",
        content: input,
    };

    setMessages((prev) => [...prev, userMessage]);

    const currentInput = input;
    setInput("");
    setLoading(true);

    try {
        const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            message: currentInput,
        }),
        });

        const data = await response.json();

        await new Promise(resolve => setTimeout(resolve, 1000));

        const aiMessage = {
        role: "assistant",
        content: data.reply,
        };

        setMessages((prev) => [...prev, aiMessage]);

    } catch {

    setMessages((prev) => [
        ...prev,
        {
        role: "assistant",
        content: "Error conectando con Lyria.",
        },
    ]);

    } finally {
        setLoading(false);
    }
    }

  return (
    <section className="chat-page">

      <div className="chat-header">
        <h2>Lyria</h2>
        <span>Director de Ingeniería IA</span>
      </div>

      <div className="messages">

        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.role === "user" ? "user" : "ai"}`}
          >
            {msg.content}
          </div>
        ))}
        {loading && (
            <div className="message ai">
                Lyria está pensando...
            </div>
        )}

      </div>

      <div className="chat-input">

        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Escribe una instrucción..."
        />

        <button
        onClick={sendMessage}
        disabled={loading}
        >
        {loading ? "..." : "Enviar"}
        </button>

      </div>

    </section>
  );
}
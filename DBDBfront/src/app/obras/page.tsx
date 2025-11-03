"use client";

import { useEffect, useState } from "react";
import Card from "../../components/card";
import Link from "next/link";

export default function ObrasPage() {
  const [obras, setObras] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/obras")
      .then((res) => res.json())
      .then((data) => setObras(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <section>
      <h1>Obras</h1>
      <Link href="/obras/add" style={styles.addBtn}>Adicionar Obra</Link>
      <div style={styles.grid}>
        {obras.map((obra) => (
          <Link key={obra.id} href={`/obras/${obra.id}`}>
            <Card
              title={obra.nome}
              description={`Início: ${obra.data_ini} | Fim: ${obra.data_fin}`}
              image={obra.imagem}
            />
          </Link>
        ))}
      </div>
    </section>
  );
}

const styles = {
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
    gap: "1.5rem",
    marginTop: "1rem",
  },
  addBtn: {
    display: "inline-block",
    backgroundColor: "#0070f3",
    color: "white",
    padding: "0.5rem 1rem",
    borderRadius: "4px",
    textDecoration: "none",
  },
};

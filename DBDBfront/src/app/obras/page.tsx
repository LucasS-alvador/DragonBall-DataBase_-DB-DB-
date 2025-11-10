"use client";

import { useEffect, useState } from "react";
import { obraService } from "../../services/api";
import Card from "../../components/card";
import Link from "next/link";

export default function ObrasPage() {
  const [obras, setObras] = useState<any[]>([]);

  useEffect(() => {
    const fetchObras = async () => {
      try {
        const data = await obraService.getAll();
        setObras(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchObras();
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
              description={`Início: ${obra.dtIni} | Fim: ${obra.dtFim}`}
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
    backgroundColor: "#4169E1",
    border: '3px solid #000000ff',
    color: "#ffc320ff",
    padding: "0.5rem 1rem",
    fontWeight:"bold",
    borderRadius: "4px",
    textDecoration: "none",
  },
};

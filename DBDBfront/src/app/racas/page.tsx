"use client";

import { useEffect, useState } from "react";
import { racaService } from "../../services/api";
import Card from "../../components/card";
import Link from "next/link";
import type { Raca } from "../../types/models";

export default function RacasPage() {
  const [racas, setRacas] = useState<Raca[]>([]);

  useEffect(() => {
    const fetchRacas = async () => {
      try {
        const data = await racaService.getAll();
        setRacas(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchRacas();
  }, []);

  return (
    <section>
      <h1>Raças</h1>
      <Link href="/racas/add" style={styles.addBtn}>Adicionar Raça</Link>
      <div style={styles.grid}>
        {racas.map((raca) => (
          <Link key={raca.id} href={`/racas/${raca.id}`}>
            <Card
              title={raca.nome}
              description={`Poder Base: ${raca.poderBase}`}
              image={raca.imagem}
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
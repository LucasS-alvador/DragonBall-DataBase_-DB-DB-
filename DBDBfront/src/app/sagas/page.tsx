"use client";

import { useEffect, useState } from "react";
import { sagaService } from "../../services/api";
import Card from "../../components/card";
import Link from "next/link";
import type { Saga } from "../../types/models";

export default function SagasPage() {
  const [sagas, setSagas] = useState<Saga[]>([]);

  useEffect(() => {
    const fetchSagas = async () => {
      try {
        const data = await sagaService.getAll();
        setSagas(data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchSagas();
  }, []);

  return (
    <section>
      <h1>Sagas</h1>
      <Link href="/sagas/add" style={styles.addBtn}>Adicionar Saga</Link>
      <div style={styles.grid}>
        {sagas.map((saga) => (
          <Link key={saga.id} href={`/sagas/${saga.id}`}>
            <Card
              title={saga.desc}
              description={`Episódios: ${saga.epIni} - ${saga.epFim}`}
              image={saga.imagem}
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
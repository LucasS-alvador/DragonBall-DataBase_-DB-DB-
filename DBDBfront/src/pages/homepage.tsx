import React from "react";
import { Link } from "react-router-dom";

const classes = ["Obra", "Saga", "Raca", "PersonagemBase", "PersonagemSaga", "Transformacao"];

export default function HomePage() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Projeto Database Viewer</h1>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {classes.map(cls => (
          <Link
            to={`/${cls.toLowerCase()}`}
            key={cls}
            className="p-6 bg-blue-100 rounded-lg hover:bg-blue-200 text-center shadow"
          >
            {cls}
          </Link>
        ))}
      </div>
    </div>
  );
}

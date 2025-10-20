import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/api";
import Card from "../components/card";

export default function ClassPage() {
  const { className } = useParams();
  const [objects, setObjects] = useState<any[]>([]);

  useEffect(() => {
    api.get(`/api/${className}`).then(res => setObjects(res.data));
  }, [className]);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">{className}</h1>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
        {objects.map(obj => (
          <Card
            key={obj.id}
            id={obj.id}
            category={className || ""}
            title={obj.nome || obj.desc || `#${obj.id}`}
            image={obj.imagem || "https://via.placeholder.com/150"}
          />
        ))}
      </div>
    </div>
  );
}

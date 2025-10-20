import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import api from "../api/api";

export default function DetailPage() {
  const { className, id } = useParams();
  const [obj, setObj] = useState<any>(null);

  useEffect(() => {
    api.get(`/api/${className}/${id}`).then(res => setObj(res.data));
  }, [className, id]);

  if (!obj) return <p>Loading...</p>;

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-4">{obj.nome || obj.desc}</h1>
      <img src={obj.imagem || "https://via.placeholder.com/300"} alt={obj.nome} className="w-64 rounded-lg" />
      <pre className="bg-gray-100 p-4 rounded mt-4">{JSON.stringify(obj, null, 2)}</pre>
    </div>
  );
}

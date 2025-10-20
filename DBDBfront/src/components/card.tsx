import React from "react";
import { useNavigate } from "react-router-dom";

interface CardProps {
  title: string;
  image: string;
  id: number;
  category: string;
}

const Card: React.FC<CardProps> = ({ title, image, id, category }) => {
  const navigate = useNavigate();
  return (
    <div
      className="border rounded-lg shadow-md hover:shadow-lg p-4 cursor-pointer"
      onClick={() => navigate(`/${category}/${id}`)}
    >
      <img src={image} alt={title} className="w-full h-40 object-cover rounded-md" />
      <h2 className="text-lg font-semibold mt-2">{title}</h2>
    </div>
  );
};

export default Card;

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/homepage";
import ClassPage from "./pages/classpage";
import DetailPage from "./pages/detailpage";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/:className" element={<ClassPage />} />
        <Route path="/:className/:id" element={<DetailPage />} />
      </Routes>
    </Router>
  );
}

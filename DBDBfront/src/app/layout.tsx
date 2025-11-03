import "./globals.css";
import Navbar from "../components/navbar";

export const metadata = {
  title: "DBDB Front",
  description: "Frontend para banco de dados Dragon Ball",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>
        <Navbar />
        <main style={{ padding: "2rem" }}>{children}</main>
      </body>
    </html>
  );
}

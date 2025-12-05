import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Expense Tracker",
  description: "Personal finance app with budget insights",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}

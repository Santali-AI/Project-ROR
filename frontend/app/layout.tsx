import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'ROR | Multispecies Research', description: 'Research-safe communication observation lab' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="en"><body>{children}</body></html>; }

import React from 'react';
import { Outlet } from 'react-router-dom';
import Footer from "./Footer";
import Navbar from './Navbar';

export default function Layout() {
  return (
    <div >
      <Navbar />
      <div className="min-h-[90vh] bg-gray-200 container mx-auto p-8" >
        <Outlet />
      </div>
      <Footer />
    </div>
  );
}

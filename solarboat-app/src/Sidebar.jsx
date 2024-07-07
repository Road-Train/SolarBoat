import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <aside className="bg-gray-800 text-white w-64 min-h-screen p-4">
      <nav className="space-y-4">
        <img src='/image.png' alt="Project Logo" className="logo"/>
        <Link to="/" className="block py-2 px-4 rounded hover:bg-gray-700">Home</Link>
        <Link to="/profile" className="block py-2 px-4 rounded hover:bg-gray-700">Profile</Link>
        <Link to="/simulation" className="block py-2 px-4 rounded hover:bg-gray-700">3D Simulation</Link>
        <Link to="/recognition" className="block py-2 px-4 rounded hover:bg-gray-700">Object Recognition</Link>
        <Link to="/nuc" className="block py-2 px-4 rounded hover:bg-gray-700">NUC</Link>
      </nav>
    </aside>
  );
};

export default Sidebar;

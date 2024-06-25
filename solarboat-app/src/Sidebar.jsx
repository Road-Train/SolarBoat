import React from 'react';

const Sidebar = () => {
  return (
    <aside className="bg-gray-800 text-white w-64 min-h-screen p-4">
      <nav className="space-y-4">
        <a href="#" className="block py-2 px-4 rounded hover:bg-gray-700">3D Simulation</a>
        <a href="#" className="hblock py-2 px-4 rounded hover:bg-gray-700">Object Recognition</a>
        <a href="#" className="block py-2 px-4 rounded hover:bg-gray-700">NUC Connection</a>
        </nav>
    </aside>
  );
};

export default Sidebar;
import React from 'react';

const Header = () => {
  return (
    <header className="bg-blue-500 text-white py-4 px-6 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-2xl font-bold">Dashboard</h1>
        <nav>
          <ul className="flex space-x-4">
            <li><a href="https://github.com/Road-Train/SolarBoat" className="hover:text-gray-200">GitHub</a></li>
            <li><a href="https://gitlab.com/Road-Train1/SolarBoat" className="hover:text-gray-200">GitLab</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;

// App.jsx
import React from 'react';
import Header from './Header';
import Sidebar from './Sidebar';

const App = () => {
  return (
      <div className="flex h-screen bg-gray-100">
        <Sidebar />
        <div className="flex-1 flex flex-col">
          <Header />
        </div>
      </div>
  );
};

export default App;

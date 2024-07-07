import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Sidebar from './Sidebar';
import Header from './Header';
import Profile from './Profile';
import DashboardContent from './DashboardContent';
import NUC from './NUC'

const App = () => {
  return (
    <div className='flex h-screen'>
      <Sidebar />
      <div className='flex-1 flex flex-col'>
        <Header />
        <main className='flex-1 p-8'>
          <Routes>
            <Route path="/" element={<DashboardContent />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/simulation" element={<div className="simulation-window"><p>Simulation Window</p></div>} />
            <Route path="/recognition" element={<div className="camera-window"><p>Camera Window</p></div>} />
            <Route path="/NUC" Component={NUC} />
          </Routes>
        </main>
      </div>
    </div>
  );
};

export default App;

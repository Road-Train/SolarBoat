import React from 'react';
import { BrowserRouter as Router, Link } from 'react-router-dom';
import Profile from './Profile';
import './index.css';

const Dashboard = () => {
  return (
      <div className="main-content">
        <Router path="/profile" component={Profile} />
        <Router path="/simulation" component={() => <div className="simulation-window"><p>Simulation Window</p></div>} />
        <Router path="/recognition" component={() => <div className="camera-window"><p>Camera Window</p></div>} />
        <Router path="/nuc" component={() => <div className="connection-status"><p>NUC Connection Status</p></div>} />
      </div>
  );
};

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Dashboard</h2>
      <Link to="/profile">Profile</Link>
      <Link to="/simulation">3D Simulation</Link>
      <Link to="/recognition">Object Recognition</Link>
      <Link to="/nuc">NUC</Link>
    </div>
  );
};

const App = () => {
  return (
    <div className='flex'>
      <h1>Welcome to the Dashboard</h1>
      <Dashboard />
    </div>
  );
};

export default App;
import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Profile from './Profile';
//import Login from './Login';
import './index.css';

const Dashboard = () => {
  return (
    <div className="main-content">
      <Router>
        <Route path="/profile" component={Profile} />
        <Route path="/login" component={Login} />
        <Route path="/simulation" component={() => <div className="simulation-window"><p>Simulation Window</p></div>} />
        <Route path="/recognition" component={() => <div className="camera-window"><p>Camera Window</p></div>} />
        <Route path="/nuc" component={() => <div className="connection-status"><p>NUC Connection Status</p></div>} />
      </Router>
    </div>
  );
};

const Sidebar = () => {
  return (
    <div className="sidebar">
      <h2>Dashboard</h2>
      <Link to="/profile">Profile</Link>
      <Link to="/login">Login</Link>
      <Link to="/simulation">3D Simulation</Link>
      <Link to="/recognition">Object Recognition</Link>
      <Link to="/nuc">NUC</Link>
    </div>
  );
};

const App = () => {
  return (
    <Router>
      <div className="flex">
        <Sidebar />
        <Dashboard />
      </div>
    </Router>
  );
};

export default App;
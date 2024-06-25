// App.jsx
import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './Header';
import Sidebar from './Sidebar';
import DashboardContent from './DashboardContent'; // Import DashboardContent
import ThreeDSimulation from './ThreeD'; // Import ThreeDSimulation
import ObjectRecognition from './OR'; // Import ObjectRecognition
import NUCConnection from './NUC'; // Import NUCConnection

const App = () => {
  return (
      <div className="flex h-screen bg-gray-100">
        <Sidebar />
        <div className="flex-1 flex flex-col">
          <Header />
          <Route path="/DashboardContent" exact component={DashboardContent} />
          <Route path="/ThreeD" component={ThreeDSimulation} />
          <Route path="/OR" component={ObjectRecognition} />
          <Route path="/NUC" component={NUCConnection} />
        </div>
      </div>
  );
};

export default App;

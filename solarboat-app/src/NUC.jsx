import React, { useState, useEffect } from 'react';
import './nuc.css'

const NUC = () => {
  const [isConnected, setIsConnected] = useState(false);

  // Mock function to simulate checking the connection status
  useEffect(() => {
    const checkConnection = () => {
      // Simulate an API call to check the connection status
      setTimeout(() => {
        const status = Math.random() > 0.5; // Randomly set the connection status
        setIsConnected(status);
      }, 1000); // Simulate a 1-second delay
    };

    checkConnection();
  }, []);

  return (
    <div className="nuc-status bg-white p-8 rounded-lg shadow-md">
      <h2 className="text-3xl font-semibold mb-4 text-blue-700">NUC Connection Status</h2>
      {isConnected ? (
        <div className="nuc-window p-4 bg-green-100 border-2 border-green-500 rounded-lg">
          <p className="text-xl text-green-700">NUC is connected</p>
        </div>
      ) : (
        <div className="p-4 bg-red-100 border-2 border-red-500 rounded-lg">
          <p className="text-xl text-red-700">NUC is not connected</p>
        </div>
      )}
    </div>
  );
};

export default NUC;

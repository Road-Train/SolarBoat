import React, { useState, useEffect } from 'react';

const NUCConnection = () => {
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    const interval = setInterval(() => {
      setIsConnected(prev => !prev);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex-1 p-8">
      <h2 className="text-3xl font-semibold mb-4">NUC Connection</h2>
      <div className="bg-white shadow-md rounded-lg p-4">
        <div className="connection-status flex items-center justify-center h-96">
          {isConnected ? (
            <p className="text-green-500 text-xl">Connected to NUC</p>
          ) : (
            <p className="text-red-500 text-xl">Waiting for connection...</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default NUCConnection;

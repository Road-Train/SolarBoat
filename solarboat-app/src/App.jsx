import React from 'react';
import Header from './Header';
import Sidebar from './Sidebar';
import Button from './Button';

const App = () => {
  return (
    <>
      <div className="flex h-screen bg-gray-100">
        <Sidebar />
        <div className="flex-1 flex flex-col">
          <Header />
          <Button>Submit</Button>
        </div>
      </div>
    </>
  );
};

export default App;
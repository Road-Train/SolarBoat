import { createRoot } from 'react-dom/client';
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

function NavigationBar() {
  // TODO: Actually implement a navigation bar
  return <h1>Hello from React!</h1>;
}

ReactDOM.render(<App />, document.getElementById('root'));
const domNode = document.getElementById('navigation');
const root = createRoot(domNode);
root.render(<NavigationBar />);
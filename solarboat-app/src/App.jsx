// App.js
import React, { useState } from 'react';
import Button from './Button';
import KnowledgeButton from './KnowledgeButton';

const App = () => {
    const [selectedComponent, setSelectedComponent] = useState(null);

    const renderComponent = (title) => {
        setSelectedComponent(title);
    };

    return (
        <div style={{
            fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
            margin: 0,
            padding: 0,
            background: 'linear-gradient(135deg, #3494e6, #ec6ead)',
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            height: '100vh',
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
        }}>
            <h1 style={{
                textAlign: 'center',
                color: '#fff',
                textShadow: '2px 2px 4px rgba(0,0,0,0.5)',
            }}>Solarboat</h1>

            <div className="button-container" style={{
                display: 'flex',
                flexWrap: 'wrap',
                justifyContent: 'center',
                marginTop: '30px',
            }}>
                <Button title="3D Simulation" onClick={() => renderComponent('3D Simulation')} />
                <Button title="Object Recognition" onClick={() => renderComponent('Object Recognition')} />
                <Button title="NUC" onClick={() => renderComponent('NUC')} />
                <Button title="Game Simulation" onClick={() => renderComponent('Game Simulation')} />
            </div>

            <KnowledgeButton />

            {selectedComponent && (
                <div style={{
                    marginTop: '20px',
                    fontSize: '18px',
                    textAlign: 'center',
                    color: '#fff',
                }}>
                    <h2>{selectedComponent}</h2>
                    {/* Replace with actual component content */}
                    <p>Replace this with your actual React component code for {selectedComponent}</p>
                </div>
            )}

            {/* Navigation and Additional HTML Content */}
            <nav id="navigation"></nav>
        </div>
    );
};

export default App;

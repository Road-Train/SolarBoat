// KnowledgeButton.js
import React from 'react';

const KnowledgeButton = () => {
    return (
        <button className="knowledge-button" style={{
            position: 'absolute',
            top: '10px',
            right: '10px',
            padding: '8px 16px',
            fontSize: '16px',
            border: '2px solid #000000',
            borderRadius: '5px',
            backgroundColor: '#818589',
            color: 'white',
            cursor: 'pointer',
            transition: 'background-color 0.3s, border-color 0.3s, transform 0.2s',
        }}>Knowledge Management</button>
    );
};

export default KnowledgeButton;

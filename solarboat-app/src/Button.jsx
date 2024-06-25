import React from 'react';

const Button = ({ title, onClick }) => {
    return (
        <button style={{
            display: 'inline-flex',
            alignItems: 'center',
            justifyContent: 'center',
            padding: '12px 24px',
            margin: '10px',
            fontSize: '18px',
            cursor: 'pointer',
            backgroundColor: '#818589',
            color: 'white',
            border: '2px solid #000000',
            borderRadius: '5px',
            textAlign: 'center',
            textDecoration: 'none',
            transition: 'background-color 0.3s, border-color 0.3s, transform 0.2s',
            whiteSpace: 'nowrap',
        }} onClick={onClick}>
            {title}
        </button>
    );
};

export default Button;
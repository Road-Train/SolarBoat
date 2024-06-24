body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #3494e6, #ec6ead);
    background-size: cover;
    background-repeat: no-repeat;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

h1 {
    text-align: center;
    color: #fff;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

.button-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 30px;
}

.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 12px 24px;
    margin: 10px;
    font-size: 18px;
    cursor: pointer;
    background-color: #818589;
    color: white;
    border: 2px solid #000000;
    border-radius: 5px;
    text-align: center;
    text-decoration: none;
    transition: background-color 0.3s, border-color 0.3s, transform 0.2s;
    white-space: nowrap;
}

.button:hover {
    background-color: #3494e6;
    border-color: #3494e6;
    transform: scale(1.05);
}

.knowledge-button {
    position: absolute;
    top: 10px;
    right: 10px;
    padding: 8px 16px;
    font-size: 16px;
    border: 2px solid #000000;
    border-radius: 5px;
    background-color: #818589;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s, border-color 0.3s, transform 0.2s;
}

.knowledge-button:hover {
    background-color: #3494e6;
    border-color: #3494e6;
}

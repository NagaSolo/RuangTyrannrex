import React, {useState, useEffect} from 'react';

function App() {
  const [currentHome, setCurrentHome] = useState('Cobaan');

  useEffect(() => {
    fetch('http://localhost:5000/api').then(res => res.json()).then(data => {
      setCurrentHome(data.api);
    });
  }, []);
  return (
    <div className="App">
      <header className="App-header">
        {currentHome}
      </header>
    </div>
  );
}

export default App;

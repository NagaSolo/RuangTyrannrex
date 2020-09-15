import React, {useState, useEffect} from 'react';

export default function Apifetch() {
  const [currentHome, setCurrentHome] = useState('Cobaan');

  useEffect(() => {
    fetch('http://localhost:5000/api').then(res => res.json()).then(data => {
      setCurrentHome(data.api);
    });
  }, []);
  return (
    <div>
      <header>
        {currentHome}
      </header>
    </div>
  );
}
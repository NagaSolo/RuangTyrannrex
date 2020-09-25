import React, {useState, useEffect} from 'react';

export default function Apifetch() {
  const [currentHome, setCurrentHome] = useState('Testing');

  useEffect(() => {
    fetch('/lapindromes').then(res => res.json()).then(data => {
      setCurrentHome(data.Answer);
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
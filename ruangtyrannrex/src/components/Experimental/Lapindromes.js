import React, {useState, useEffect} from 'react';

export default function Lapindromes() {

  let [currentInput, setCurrentInput] = useState('Enter your input ..')

  let [currentAnswer, setCurrentAnswer] = useState('Testing');

  useEffect(() => {
    fetch('/lapindromes', {
      method: 'post',
      body: JSON.stringify({currentInput})
    }).then(res => res.json()).then(data => {
      setCurrentAnswer(data.Answer);
    });
  }, [])

  return (
    <div>
      <input 
        type='text'
        value={currentInput}
        onChange={event => setCurrentInput(event.target.value)}
      />
      <button onClick={currentInput}>Send</button>
      <div>
        <h3>It is.. 
          {currentAnswer}
        </h3>
      </div>
    </div>
  );
}
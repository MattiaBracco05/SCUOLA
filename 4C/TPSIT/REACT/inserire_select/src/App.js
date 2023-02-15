import React, { useState } from 'react';

function App() {
  const [selectedValue, setSelectedValue] = useState('');

  const handleSelectChange = (event) => {
    setSelectedValue(event.target.value);
    alert(`Hai selezionato: ${event.target.value}`);
  };

  return (
    <div>
      <h1>Componente select</h1>
      <select value={selectedValue} onChange={handleSelectChange}>
        <option value="">Scegli un opzione</option>
        <option value="option1">Opzione 1</option>
        <option value="option2">Opzione 2</option>
        <option value="option3">Opzione 3</option>
      </select>
    </div>
  );
}

export default App;

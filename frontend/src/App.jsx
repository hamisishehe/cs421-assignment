import React, { useState } from 'react';
import Students from './Students';
import Courses from './Courses';
import NodeIndicator from './NodeIndicator';

function App() {
  const [view, setView] = useState(null);

  return (
    <div style={{ textAlign: 'center' }}>
      <h1>University Portal</h1>
      <NodeIndicator />
      <button onClick={() => setView('students')}>Students</button>
      <button onClick={() => setView('courses')}>Courses</button>

      {view === 'students' && <Students />}
      {view === 'courses' && <Courses />}
    </div>
  );
}

export default App;

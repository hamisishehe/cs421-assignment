import React, { useEffect, useState } from 'react';

function Students() {
  const [students, setStudents] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/students')
      .then(res => res.json())
      .then(data => setStudents(data.slice(0, 10)))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Students</h2>
      <ul>
        {students.map((s, idx) => (
          <li key={idx}>{s.name} - {s.program}</li>
        ))}
      </ul>
    </div>
  );
}

export default Students;

import React, { useEffect, useState } from 'react';

function Courses() {
  const [subjects, setSubjects] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/subjects')
      .then(res => res.json())
      .then(data => setSubjects(data))
      .catch(console.error);
  }, []);

  return (
    <div>
      <h2>Software Engineering Subjects</h2>
      <ul>
        {subjects.map((s, idx) => (
          <li key={idx}>{s.name} -  {s.year}</li>
        ))}
      </ul>
    </div>
  );
}

export default Courses;

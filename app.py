import os
from flask import Flask, request, jsonify
from models import db, Students, Subjects
import config
from models import Students
from models import Subjects

app = Flask(__name__)
app.config.from_object(config) 


db.init_app(app)


@app.route("/")
def index():
    return ""

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student = Students(
        first_name=data['first_name'],
        last_name=data['last_name'],
        program=data.get('program')
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully', 'student_id': student.id}), 201

@app.route('/subjects', methods=['POST'])
def add_subject():
    data = request.get_json()
    subject = Subjects(
        course_name=data['course_name'],
        course_code=data['course_code'],
        year=data.get('year'),
        student_id=data['student_id']
    )
    db.session.add(subject)
    db.session.commit()
    return jsonify({'message': 'Subject added successfully'}), 201

@app.route('/subjects', methods=['GET'])
def get_subjects():
    subjects = Subjects.query.all()
    output = []

    for subject in subjects:
        subject_data = {
            'id': subject.id,
            'course_name': subject.course_name,
            'course_code': subject.course_code,
            'year': subject.year,
            'student_id': subject.student_id,
            'student_name': f"{subject.student.first_name} {subject.student.last_name}" if subject.student else None
        }
        output.append(subject_data)

    return jsonify(output), 200

@app.route('/students', methods=['GET'])
def get_students():
    students = Students.query.all()
    output = []
    for student in students:
        subjects = [{
            'id': subj.id,
            'course_name': subj.course_name,
            'course_code': subj.course_code,
            'year': subj.year
        } for subj in student.subjects]

        student_data = {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'program': student.program,
            'subjects': subjects
        }
        output.append(student_data)
    return jsonify(output), 200


if __name__ == "__main__":
    app.run(debug=True)

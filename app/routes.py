from flask import Blueprint, request, jsonify, send_from_directory, render_template
import os
from app.agentes import support_agent, support_quality_assurance_agent
from app.tarefas import inquiry_resolution, quality_assurance_review
from crewai import Crew

bp = Blueprint('api', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/kickoff', methods=['POST'])
def kickoff():
    data = request.json
    customer = data.get('customer')
    person = data.get('person')
    inquiry = data.get('inquiry')

    crew = Crew(
        agents=[support_agent, support_quality_assurance_agent],
        tasks=[inquiry_resolution, quality_assurance_review],
        verbose=2,
        memory=True
    )
    
    inputs = {
        "customer": customer,
        "person": person,
        "inquiry": inquiry
    }

    result = crew.kickoff(inputs=inputs)
    return jsonify(result)

@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

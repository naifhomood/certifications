from flask import Flask, render_template, request, jsonify
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
from supabase import create_client, Client
import os
from datetime import datetime

app = Flask(__name__)
Bootstrap(app)

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.route('/')
def index():
    # Get all certificates first
    all_certificates = supabase.table('test').select("*").order('Sr.asc').execute()
    certificates = all_certificates.data
    
    # Print the first certificate to see its structure
    if certificates:
        print("Certificate data structure:", certificates[0].keys())
        print("First certificate:", certificates[0])

    # Calculate top 3 certificate holders
    person_certificates = {}
    for cert in certificates:
        name = cert['Full Name']
        if name in person_certificates:
            person_certificates[name]['count'] += 1
        else:
            person_certificates[name] = {
                'count': 1,
                'profile_image': cert.get('صورة الشخص', ''),
                'department': cert['department']
            }
    
    # Sort and get top 3
    top_3 = sorted(
        [{'name': name, **data} for name, data in person_certificates.items()],
        key=lambda x: x['count'],
        reverse=True
    )[:3]

    # Get unique departments
    all_departments = {cert['department'] for cert in certificates}

    # Get filter parameters
    department = request.args.get('department', '')
    name = request.args.get('name', '')
    cert_type = request.args.get('cert_type', '')
    
    # Apply filters in Python
    filtered_certificates = certificates
    if department:
        filtered_certificates = [cert for cert in filtered_certificates if department.lower() in cert['department'].lower()]
    if name:
        filtered_certificates = [cert for cert in filtered_certificates if name.lower() in cert['Full Name'].lower()]
    if cert_type:
        filtered_certificates = [cert for cert in filtered_certificates if cert_type.lower() in cert['Certificate Name'].lower()]
    
    return render_template('index.html', 
                         certificates=filtered_certificates,
                         departments=sorted(all_departments),
                         top_3=top_3,
                         current_filters={
                             'department': department,
                             'name': name,
                             'cert_type': cert_type
                         })

if __name__ == '__main__':
    app.run(host='192.168.1.22', port=5000, debug=True)

import os
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# Load environment variables
load_dotenv()

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

def fetch_all_certificates():
    try:
        response = supabase.table('test').select("*").order('Sr.asc').execute()
        return response.data
    except Exception as e:
        print(f"Error fetching certificates: {str(e)}")
        return None

def print_certificate(cert):
    print("\n" + "="*50)
    print(f"رقم التسلسل: {cert['Sr']}")
    print(f"الاسم: {cert['Full Name']}")
    print(f"اسم الشهادة: {cert['Certificate Name']}")
    print(f"القسم: {cert['department']}")
    print(f"تاريخ الشهادة: {cert['certfication date']}")
    print(f"رابط الشهادة: {cert['certifation link']}")
    print("="*50)

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    certs = fetch_all_certificates()
    if certs:
        # تنظيم الشهادات حسب القسم
        departments = {}
        for cert in certs:
            dept = cert['department']
            if dept in departments:
                departments[dept] += 1
            else:
                departments[dept] = 1
        
        # ترتيب الشهادات حسب التاريخ
        for cert in certs:
            if cert['certfication date']:
                cert['certfication date'] = datetime.strptime(cert['certfication date'], '%Y-%m-%d').strftime('%Y-%m-%d')
        
        return render_template('index.html', certificates=certs, departments=departments)
    return render_template('index.html', certificates=[], departments={})

if __name__ == "__main__":
    app.run(host='192.168.1.22', port=5000, debug=True)

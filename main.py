import os
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime

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

def main():
    try:
        print("\nجاري جلب جميع الشهادات...\n")
        
        # Fetch all certificates
        certs = fetch_all_certificates()
        if certs:
            print(f"تم العثور على {len(certs)} شهادة:")
            for cert in certs:
                print_certificate(cert)
            
            # Print summary by department
            print("\n" + "="*50)
            print("ملخص الشهادات حسب القسم:")
            departments = {}
            for cert in certs:
                dept = cert['department']
                if dept in departments:
                    departments[dept] += 1
                else:
                    departments[dept] = 1
            
            for dept, count in departments.items():
                print(f"- {dept}: {count} شهادة")
            print("="*50)
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

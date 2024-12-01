# Supabase Python Connection Example

This project demonstrates how to connect to a Supabase database using Python.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
   - Copy `.env` file and update with your Supabase credentials
   - Replace `your-supabase-project-url` with your Supabase project URL
   - Replace `your-supabase-anon-key` with your Supabase anon/public key

3. Run the example:
```bash
python main.py
```

## Important Notes
- Make sure to never commit your actual Supabase credentials to version control
- The example assumes you have a table named 'users' in your database
- Modify the table name and queries according to your database schema

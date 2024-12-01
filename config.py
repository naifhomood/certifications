import os

class Config:
    # Supabase configuration
    SUPABASE_URL = os.environ.get('SUPABASE_URL', 'https://giubtusdpozatzclolix.supabase.co')
    SUPABASE_KEY = os.environ.get('SUPABASE_KEY', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdpdWJ0dXNkcG96YXR6Y2xvbGl4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzI5NTE0ODEsImV4cCI6MjA0ODUyNzQ4MX0.T5tSx--bn2_PhZ6_v1bDj_PXAqlJK5mTvI2iqrRGOqo')
    
    # Flask configuration
    FLASK_ENV = os.environ.get('FLASK_ENV', 'production')
    DEBUG = FLASK_ENV == 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

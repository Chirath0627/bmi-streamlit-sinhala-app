# 1. Select Base Image
FROM python:3.9-slim

# 2. Create Folders Inside Containers
WORKDIR /app

# 3. Copy Requirements file to Container
COPY requirements.txt .

# 4. Libraries install
RUN pip install -r requirements.txt

# 5. Copy All Files
COPY . .

# 6. Run Streamlit  
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
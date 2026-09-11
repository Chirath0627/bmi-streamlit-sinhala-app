# 1. Select Base Image
FROM python:3.9-slim

# 2. Reject Pip root warning and version check warnings
ENV PIP_ROOT_USER_ACTION=ignore
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# 3. Create Folders Inside Containers
WORKDIR /app

# 4. Copy Requirements file to Container
COPY requirements.txt .

# 5. Libraries install
RUN pip install -r requirements.txt

# 6. Copy All Files
COPY . .

# 7. Run Streamlit  
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
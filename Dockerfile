# 1. Base image එක තෝරා ගැනීම
FROM python:3.9-slim

# 2. Container එක ඇතුළේ වැඩ කරන තැන (Folder එක) සැකසීම
WORKDIR /app

# 3. අපේ requirements file එක container එකට copy කිරීම
COPY requirements.txt .

# 4. Libraries install කිරීම
RUN pip install -r requirements.txt

# 5. ඉතිරි ඔක්කොම code files copy කිරීම
COPY . .

# 6. Streamlit run කරන command එක
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
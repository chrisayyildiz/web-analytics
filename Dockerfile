FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# --no-cache-dir reduces image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the working directory
COPY . .

# Make port 8501 available to the world outside this container (Streamlit's default port)
EXPOSE 8501

# Define the command to run when the container starts.
# This chain of commands will:
# 1. Generate fresh data
# 2. Run the ETL process on that data
# 3. Start the Streamlit dashboard
CMD ["sh", "-c", "python data_simulation/generate_data.py && python etl_pipeline/process_data.py && streamlit run dashboard/app.py --server.port=8501 --server.address=0.0.0.0"]

# Web User Behaviour Analytics Project

This project simulates and analyses user behaviour on a website. The final output is an interactive dashboard that provides actionable insights for business stakeholders.

## Business Value

The goal is to understand user behaviour to drive business decisions regarding:
- Marketing campaign optimization and timing.
- UX/UI improvements based on device-specific pain points (e.g., high bounce rates).
- User segmentation for personalization.
- Global expansion strategy by analyzing regional behaviour.

---

## Technology Stack

- **Core Language:** Python
- **Data Handling:** Pandas, NumPy
- **Dashboard:** Streamlit, Plotly
- **Containerization:** Docker
- **Data Simulation:** Faker

---

## Project Structure

```
web-user-analytics/
├── data_simulation/           # Simulated data generator scripts
├── data/                      # Raw and processed data (gitignored)
├── etl_pipeline/              # ETL scripts for processing data
├── analysis/                  # EDA notebooks / scripts
├── dashboard/                 # Streamlit dashboard app
├── Dockerfile                 # Docker container definition
├── .dockerignore              # Files to ignore in Docker build
├── requirements.txt           # Python dependencies
└── README.md                  # Project description
```

---

## How to Run

There are two ways to run this project: using Docker (recommended) or setting up a local Python environment.

### Option 1: Run with Docker (Recommended)

This is the easiest way to run the entire application.

**Prerequisites:**
- Docker must be installed and running on your system.

**Steps:**
1.  **Build the Docker image:**
    Open your terminal in the project root and run:
    ```bash
    docker build -t web-analytics .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8501:8501 web-analytics
    ```

3.  **View the Dashboard:**
    Open your web browser and navigate to `http://localhost:8501`. The dashboard should be live.

### Option 2: Run Locally

**Prerequisites:**
- Python 3.8+

**Steps:**
1.  **Clone the repository.**

2.  **Set up a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the pipeline and dashboard:**
    To see the dashboard, you must first generate and process the data.
    ```bash
    python data_simulation/generate_data.py
    python etl_pipeline/process_data.py
    streamlit run dashboard/app.py
    ```

---

## Example Insights

The analysis of this simulated data typically reveals several key insights:
- **Desktop users convert at a higher rate** than mobile or tablet users, suggesting the desktop experience is more conducive to purchasing.
- **Mobile users have the highest bounce rate**, indicating potential UX friction or performance issues on the mobile site.
- **User engagement and session volume peak in the evening**, which could be the optimal time for marketing pushes and announcements.
- **Session length and pages visited** are strong positive indicators of a user's likelihood to convert.
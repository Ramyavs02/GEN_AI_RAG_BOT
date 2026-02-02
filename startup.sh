#!/bin/bash

echo "Starting FastAPI..."
uvicorn rag_api:app --host 0.0.0.0 --port 8000 &

echo "Starting Streamlit..."
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0

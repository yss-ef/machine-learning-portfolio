#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""
echo "Starting Student ML Platform..."
python app.py

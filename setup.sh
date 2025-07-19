#!/bin/bash

# Mental Health Risk Assessment App Setup Script

echo "Setting up Mental Health Risk Assessment App..."

# Install Python dependencies
pip install -r requirements.txt

# Generate dataset if it doesn't exist
if [ ! -f "mental_health_dataset.csv" ]; then
    echo "Generating dataset..."
    python data_generator.py
fi

echo "Setup complete! Run 'streamlit run simple_app.py' to start the app." 
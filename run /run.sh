#!/bin/bash

echo "🔁 Training model locally..."
python train.py

echo "📦 Committing and pushing code..."
git add .
git commit -m "auto run: trigger pipeline and app"
git push

echo "🚀 Starting Flask app..."
python app.py
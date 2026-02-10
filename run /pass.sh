#!/bin/bash

echo "✅ PASS CASE: Triggering CI/CD pipeline"

cd ..
git add .
git commit -m "model passed quality gate"
git push
#!/bin/bash

echo "✅ PASS CASE: Triggering CI/CD pipeline"

git add .
git commit -m "model passed quality gate"
git push
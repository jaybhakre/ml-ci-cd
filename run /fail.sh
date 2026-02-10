#!/bin/bash

echo "❌ FAIL CASE: Triggering CI/CD pipeline"

git add .
git commit -m "model failed quality gate"
git push
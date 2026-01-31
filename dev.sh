#!/bin/bash

# Development script to run both Hugo server and local API server

echo "🚀 Starting local development environment..."

# Preprocess Tailwind
echo "🎨 Preprocessing Tailwind..."
bun run build:css

# Start the local API server in the background
echo "📡 Starting local API server..."
bun local-dev-server.js &
API_PID=$!

# Wait a moment for the API server to start
sleep 2

# Start Hugo server
echo "🌐 Starting Hugo server..."
bun run dev

# Cleanup function
cleanup() {
    echo "🛑 Stopping servers..."
    kill $API_PID 2>/dev/null
    exit 0
}

# Trap Ctrl+C to cleanup
trap cleanup INT

# Wait for Hugo server to finish
wait

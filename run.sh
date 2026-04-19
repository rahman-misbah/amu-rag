#!/bin/bash

# Colors for pretty output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Store PIDs to kill only our child processes
API_PID=""
STREAMLIT_PID=""

# Function to handle script exit
cleanup() {
    echo -e "\n${YELLOW}Shutting down processes...${NC}"
    
    # Kill only the specific child processes, not the entire process group
    if [ ! -z "$API_PID" ] && kill -0 $API_PID 2>/dev/null; then
        echo -e "${YELLOW}Stopping FastAPI (PID: $API_PID)...${NC}"
        kill -TERM $API_PID 2>/dev/null
        sleep 1
        kill -KILL $API_PID 2>/dev/null
    fi
    
    if [ ! -z "$STREAMLIT_PID" ] && kill -0 $STREAMLIT_PID 2>/dev/null; then
        echo -e "${YELLOW}Stopping Streamlit (PID: $STREAMLIT_PID)...${NC}"
        kill -TERM $STREAMLIT_PID 2>/dev/null
        sleep 1
        kill -KILL $STREAMLIT_PID 2>/dev/null
    fi
    
    echo -e "${GREEN}All processes terminated.${NC}"
    exit 0
}

# Set up trap to catch exit signals
trap cleanup SIGINT SIGTERM EXIT

# Activate conda environment if needed (uncomment and adjust)
# source ~/miniforge3/etc/profile.d/conda.sh && conda activate hackcera

echo -e "${GREEN}Starting AMU RAG System...${NC}"

# Start FastAPI backend
echo -e "${GREEN}Starting FastAPI backend...${NC}"
python run_api.py &
API_PID=$!
echo -e "${GREEN}FastAPI started with PID: $API_PID${NC}"

# Wait a moment for FastAPI to initialize
sleep 3

# Start Streamlit frontend
echo -e "${GREEN}Starting Streamlit frontend...${NC}"
streamlit run streamlit_app.py --server.port 8501 &
STREAMLIT_PID=$!
echo -e "${GREEN}Streamlit started with PID: $STREAMLIT_PID${NC}"

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}Both services are running!${NC}"
echo -e "${GREEN}FastAPI: http://localhost:8000${NC}"
echo -e "${GREEN}FastAPI Docs: http://localhost:8000/docs${NC}"
echo -e "${GREEN}Streamlit: http://localhost:8501${NC}"
echo -e "${YELLOW}Press Ctrl+C to stop all services${NC}"
echo -e "${GREEN}========================================${NC}"

# Wait for both processes
wait $API_PID $STREAMLIT_PID
#!/bin/bash

while true; do
    echo "================================="
    echo "  System Health Check Menu"
    echo "================================="
    echo "1. Check Disk Usage"
    echo "2. Monitor Running Processes"
    echo "3. Assess Memory Usage"
    echo "4. Evaluate CPU Usage"
    echo "5. Exit"
    echo "================================="

    # Prompt user for input
    read -p "Enter your choice [1-5]: " choice

    case $choice in
        1) 
            echo "Checking Disk Usage..."
            df -h
            ;;
        2) 
            echo "Monitoring Running Processes..."
            tasklist | head -20
            ;;
        3) 
            echo "Assessing Memory Usage..."
            systeminfo | grep "Total Physical Memory"
            ;;
        4) 
            echo "Evaluating CPU Usage..."
            wmic cpu get loadpercentage
            ;;
        5) 
            echo "Exiting..."
            exit 0
            ;;
        *) 
            echo "Invalid option! Please enter a valid choice."
            ;;
    esac

    echo ""
done

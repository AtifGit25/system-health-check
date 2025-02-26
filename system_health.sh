#!/bin/bash

# Enable Debugging
set -x

# Infinite Loop for the Menu
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
            if df -h; then
                echo "Disk Usage check successful!"
            else
                echo "Error: Failed to check Disk Usage."
            fi
            ;;
        2) 
            echo "Monitoring Running Processes..."
            if tasklist | head -20; then
                echo "Process Monitoring successful!"
            else
                echo "Error: Failed to monitor processes."
            fi
            ;;
        3) 
            echo "Assessing Memory Usage..."
            if systeminfo | findstr /C:"Total Physical Memory"; then
                echo "Memory Usage check successful!"
            else
                echo "Error: Failed to check Memory Usage."
            fi
            ;;
        4) 
            echo "Evaluating CPU Usage..."
            if wmic cpu get loadpercentage; then
                echo "CPU Usage check successful!"
            else
                echo "Error: Failed to check CPU Usage."
            fi
            ;;
        5) 
            echo "Exiting..."
            # Disable Debugging
            set +x
            exit 0
            ;;
        *) 
            echo "Invalid option! Please enter a valid choice."
            ;;
    esac

    echo ""
done

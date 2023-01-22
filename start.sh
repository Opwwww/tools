if (( $(id -u) == 0 )); then
    echo "Installing modules..." && pip3 install -r requirements.txt && python3 main.py
    else
        echo "You need root to use this program"
        exit
fi

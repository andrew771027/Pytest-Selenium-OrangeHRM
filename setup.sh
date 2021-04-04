RQFILE=requirements.txt
if [ -f "$RQFILE" ]; then
    rm requirements.txt
    echo "Delete $RQFILE"
fi

pip3 freeze > requirements.txt
echo "Create a new $RQFILE"

TREEFILE=tree.txt
if [ -f "$TREEFILE" ]; then
    rm tree.txt
    echo "Delete $RQFILE"
fi

tree > tree.txt -I "venv|__pycache__"
echo "Create a new $TREEFILE"



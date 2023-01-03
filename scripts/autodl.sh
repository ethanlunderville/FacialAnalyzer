python3 cleanurls.py

downloader () {

    echo "HERE IS THE LINE $LINE"

    if [ -z "$1" ]; then
    echo "Error Occured: Please provide a valid URL"
    exit 1
    fi

    a="$(ls -l $FACEPROJECTDIR/faces | wc -l)"

    file="image$((a))"

    wget "$1" -O "$FACEPROJECTDIR/faces/$file" -o /dev/null || rm "$FACEPROJECTDIR/faces/$file"

    convert "$FACEPROJECTDIR/faces/$file" "$FACEPROJECTDIR/faces/${file%.*}.jpeg" 

    rm "$FACEPROJECTDIR/faces/$file"

    echo $1 >> "$FACEPROJECTDIR/output/urls/done"

}

if ! command -v convert &> /dev/null
then
    sudo apt-get install imagemagick
fi

while read LINE; do
    
    num=$(( 1 + $RANDOM % 8 ))
    downloader "$LINE"
    sleep $num

done < $FACEPROJECTDIR/output/urls/urls


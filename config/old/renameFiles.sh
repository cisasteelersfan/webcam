    COUNTER=0
    DirDate=$(date +%m-%d-%y-%T)
    mkdir /home/colby/recorded/$DirDate
    for OLDNAME in /home/colby/temp/*.jpg; do
        while true; do
            COUNTER=$(($COUNTER+1))
            NEWNAME=/home/colby/recorded/$DirDate/`printf '%08d.jpg' $COUNTER`
            if [ ! -e $NEWNAME ]; then break; fi
        done
        mv "$OLDNAME" "$NEWNAME"
    done
    ffmpeg -f image2 -i /home/colby/recorded/$DirDate/%08d.jpg -b 500k /home/colby/recorded/video$DirDate.avi


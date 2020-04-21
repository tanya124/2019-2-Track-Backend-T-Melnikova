#!/bin/bash

source ./backup.config

function backup() {
    DATE=$( date +%Y-%m-%d_At_%H:%M:%S)

    pg_dump -U $DB_USER -h localhost $DB_NAME > $BACKUP_DIR/$DB_NAME/$DATE-backup.dump

    cd ./$BACKUP_DIR/$DB_NAME
    BACKUP_COUNT=`find . -type f | grep "backup" | wc -l`

    if [ ${BACKUP_COUNT} -gt ${MAX_BACKUPS} ]
    then
        DELETE_COUNT=$(( $BACKUP_COUNT - $MAX_BACKUPS ))
        for (( i==1; i<$DELETE_COUNT; i++ ))
        do
            rm ./$(ls | grep "backup" | sort | head -n 1)
        done
    fi
}

backup $@

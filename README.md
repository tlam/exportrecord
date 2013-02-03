# Database backup

    0 18 * * * /usr/local/pgsql/bin/pg_dump -Fp -b -U tlam_export_record tlam_export_record | gzip > $HOME/db_backups/tlam_export_record-`date +\%Y\%m\%d`.sql.gz 2>> $HOME/db_backups/cron.log

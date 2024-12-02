docker exec postgres_db pg_dump -U myuser mydatabase > backup_$(date +%Y%m%d).sql
echo "Backup concluído: backup_$(date +%Y%m%d).sql"
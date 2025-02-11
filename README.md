# PROG8850Template
environment with mysql with docker container

```bash
docker compose up -d
python create_database.py
```

To check running container
```bash
docker ps
```

To access database:

```bash
docker exec -it mysql_container mysql -u root -p
```

To backup database:

```bash
python backup_script.py
```

you can see backups in the backups folder.
"assignment1_backup_20250130_101949.sql"


1.1) Explain database automation and its significance in modern data management. Highlight
the role of automation in handling large volumes of data efficiently and securely.



1.2) Analyze the benefits of automating database tasks, including reduced errors, increased
reliability, faster deployments, and cost efficiency. Support your analysis with real-world
examples or case studies where possible.


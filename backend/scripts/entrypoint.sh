#!/usr/bin/env bash
set -o errexit
set -o pipefail
cmd="$@"

#function db_ready(){
#python << END
#import os
#import sys
#import psycopg2
#from pathlib import Path
#from dotenv import load_dotenv, find_dotenv

#env_path = Path("./") / ".env"

#try:
#	dbname = os.getenv("db_name")
#	dbuser = os.getenv("db_username")
#	dbpassword = os.getenv("db_password")
#	db_host = os.getenv("db_hostname")
#	conn = psycopg2.connect(f"dbname={dbname} user={dbuser} password={dbpassword} host={db_host}")
#except psycopg2.OperationalError as err:
#    print(err)
#	sys.exit(-1)
#sys.exit(0)
#END
#}

#until db_ready; do
#	>%2 echo "database is unavailable - sleeping"
#	sleep 1
#done

#>%2 echo "database is up - continuing docker run"
#echo "Database is up and available"
exec $cmd

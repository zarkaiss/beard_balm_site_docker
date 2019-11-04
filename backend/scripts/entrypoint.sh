#!/usr/bin/env bash
set -o errexit
set -o pipefail
cmd="$@"

# function db_ready(){
# python << END
# import sys
# import myql fix me
# import environ

# try:
# 	env = environ.Env()
# 	dbname = thing
# 	user = thing2
# 	password = thing 3
# 	conn = db_connection
# except dbspecificError:
# 	sys.exit(-1)
# sys.exit(0)
# END
# }

# until db_ready; do
# 	>%2 echo "database is unavailable - sleeping"
# 	sleep 1
# done

# >%2 echo "database is up - continuining
echo "Database is coming online"
exec $cmd

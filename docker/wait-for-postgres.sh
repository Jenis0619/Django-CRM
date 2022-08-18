#!/bin/bash
# wait-for-postgres.sh

set -e

host="$1"

echo "Testing Postgres connection with psql ..."
until PGPASSWORD="$DBPASSWORD" psql -h "$DBHOST" -U $DBUSER -c "\q"; do
  >&2 echo -n .
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd

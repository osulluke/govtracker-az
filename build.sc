#! /bin/bash

rm database/links.db
sqlite3 database/links.db < database/load.sql

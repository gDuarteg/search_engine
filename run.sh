#!/bin/sh
. ./config.sh

[ -f "data/archive.json" ] || python scripts/make_archive_from_donald_tweets.py data/Donald-Tweets!.csv data/archive.json

[ -f "data/index.json"   ] || python scripts/make_index_from_archive.py data/archive.json data/index.json


echo "Digite sua busca:"
read -r line
echo "Pesquisando..."
python scripts/search.py data/archive.json data/index.json "$line"

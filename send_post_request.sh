#!/usr/bin/env bash
curl -XPOST "http://localhost:8000/items/" -H "Content-Type: application/json" -d '{"name": "Table", "price": 5}' | jq

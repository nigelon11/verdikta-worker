#!/usr/bin/env bash
export GH_TOKEN="${GH_GLOBAL:-$GITHUB_TOKEN}"
"$@"

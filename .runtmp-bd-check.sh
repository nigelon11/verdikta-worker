#!/bin/bash
if [ -n "${GH_READ_PAT:+x}" ]; then
  echo "GH_READ_PAT_SET"
else
  echo "GH_READ_PAT_UNSET"
fi

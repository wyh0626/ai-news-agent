#!/bin/sh
# Git invokes this helper; the token is never stored in the remote URL or logs.
case "$1" in
  *Username*) printf '%s\n' 'x-access-token' ;;
  *Password*) printf '%s\n' "$GIT_TOKEN" ;;
  *) exit 1 ;;
esac

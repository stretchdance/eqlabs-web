#!/usr/bin/env bash

# Workaround for kicking off two subprocesses, allows you to quit both at once via Ctrl-C.
# See: https://spin.atomicobject.com/2017/08/24/start-stop-bash-background-process/
trap "kill 0" EXIT

# These need to be run separately to work around:
# https://github.com/getpelican/pelican/issues/2674
pelican --autoreload &
pelican --listen &

# Launch Firefox to load the page.
open -a Brave http://localhost:8000

# Wait for all background processes to finish.
wait
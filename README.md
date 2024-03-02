### AI AGENT for running shell commands ###

You must have a valid OctoAI Api Key stored in the env variable ```OCTOAI_TOKEN```

## To RUN ##

```echo -e '#!/bin/env/python3 /<PATH>/<TO>/forge-cli/forge/main.py -m "$@"' | sudo tee /usr/local/bin/forge > /dev/null && sudo chmod +x /usr/local/bin/forge\n```

Now in a new terminal

```forge <natural language command>```
FROM mcr.microsoft.com/devcontainers/base:ubuntu

ARG USERNAME=vscode

RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.zsh_history" \
    && echo "$SNIPPET" >> "/root/.zshrc"

# Ansible Playbooks for Development Environment Setup

This repository contains Ansible playbooks for setting up development environments. The playbooks can be used for both local containers and remote machines.

## Prerequisites

- Ansible installed on your local machine
- SSH access to the target node (for remote machines)

## Available Playbooks

1. `full_setup.yml`: Installs all needed packages, creates a user, and sets up the SSH key. Configures Bash, Neovim, and Tmux for the newly created user.
2. `vix_setup.yml`: Configures Bash, Neovim, and Tmux for the user Ansible is logging in with.

## How to Run the Playbooks

Example for full_setup.yml:
```
ansible-playbook -u arash --ask-pass --become --ask-become -i localhost:6001, full_setup.yml
```

Example for vix_setup.yml:
```
ansible-playbook -u arash --ask-pass -i localhost:6001, vim_setup.yml
```
## Available Variables

- `user_name`: The username for the development environment (default: defined in group_vars/all.yml)
- `ssh_public_key`: The public key to be set for **user_name**

## Roles

The playbooks use the following roles:

- `base_packages`: Installs basic packages
- `user_management`: Manages user creation and configuration
- `bash_config`: Configures Bash
- `tmux_config`: Configures tmux
- `neovim_config`: Configures Neovim

Each role can be customized by modifying the files in the respective role directory.

## Troubleshooting

If you encounter any issues, check the following:

1. For remote machines, ensure you have SSH access to the target node
2. Check that you have the necessary permissions on the target machine

For more detailed output, you can add the `-v` flag to the ansible-playbook command.

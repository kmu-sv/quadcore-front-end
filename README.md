# Quadcore: Serving

This repository contains serving part of Quadcore News Aggregator.

### Attention, Deployers!
You should request deploying permission to server before running `./deploy`. If you don't have your public ssh key currently, you should make one.

```
# Add your public key to server's authorized key list.
cat ~/.ssh/id_rsa.pub | ssh -i YOUR_PEM_FILE.pem ubuntu@quadcore.news "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys"
```
## GitHub Webhook Assignment

This project listens to GitHub webhook events (Push, Pull Request, Merge),
stores them in MongoDB, and displays repository activity via a polling UI.

### Tech Stack
- Flask
- MongoDB
- GitHub Webhooks
- HTML + JS

### How it works
1. GitHub sends webhook events to Flask backend
2. Backend parses and stores events in MongoDB
3. UI polls backend every 15 seconds to show updates

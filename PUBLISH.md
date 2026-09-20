# Publish AI API Atlas on GitHub

The repository is ready locally. The connected GitHub tools available to this workspace can edit an existing repository, but they cannot create a brand-new GitHub repository. Create an empty public repository named `ai-api-atlas` under `Vaibhavs25`, then run:

```bash
git remote add origin https://github.com/Vaibhavs25/ai-api-atlas.git
git push -u origin main
```

Or, with GitHub CLI installed:

```bash
gh repo create Vaibhavs25/ai-api-atlas --public --source=. --remote=origin --push
```

After the first push, enable GitHub Pages from **Settings → Pages → GitHub Actions** if GitHub has not enabled it automatically. The repository already contains the workflow that publishes `docs/`.

Do not add API keys to the repository. Optional provider secrets belong in GitHub Actions repository secrets and are used only by future verification jobs.

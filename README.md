# bean-board 🖼️

The bean-board for bean parties!

## About 💡

The UI to upload images to Daniel's bean-board!

## Usage 🔨

### Python 🐍

To run locally with Python, just do the following:

```bash
python3 app.py
```

### Docker 🐳

```bash
make run
```

## Manual Deployment 🚀

In the future, commits to this repo will automatically trigger a deployment to production in Heroku. For now, you can manually deploy by running the following commands:

```bash
heroku login # login
heroku git:remote -a bean-board # maybe needed (try without first)
git push heroku main # deploy
```

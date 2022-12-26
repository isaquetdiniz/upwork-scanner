<h1 align="center">
 Upwork-scanner
</h1>

<h3 align="center">
  A Scanner to find informations in upwork website
</h3>

<p align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/isaquetdiniz/upwork-scanner">

  <a href="https://www.linkedin.com/in/isaquediniz/">
    <img alt="Made by" src="https://img.shields.io/badge/made%20by-Isaque%20Diniz-gree">
  </a>

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/isaquetdiniz/upwork-scanner">

  <img alt="GitHub" src="https://img.shields.io/github/license/isaquetdiniz/upwork-scanner">
</p>

<p align="center">
  <a href="#-about-the-project">About the project</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-technologies">Technologies</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-getting-started">Getting Started</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>
</p>

## 👨🏻‍💻 About the project

<p>
  The Upwork Scanner is an application that was conceived as a stage in the selection process for a Scanner Enginner at Argyle.
</p>

<p>
  I started the project trying to found a way to get informations without need a simulate a user in a browser.

  My first try was open the site manually and inspect the requests that are been made, see the server endpoints, tokens, cookies and try simulate then with curl in my terminal, but it's fail. The process of login not is a simple request do a endpoint that return a jwt token, it's more complicated.

  My second try was intercept the requests that are been made by site using a [Burpsuite](https://portswigger.net/burp), that is a very common tool for security researches, but not was possible too.

  So the only away that i founded was simulate a user using a browser with [Selenium](https://selenium-python.readthedocs.io/), that is a very used browser automation tool for python. I started the challenge with a just file using selenium and navigating in the page and getting informations. Also tried to intercept the request that are been made beetwen selenium browser and upwork server with [Selenium Wire](https://pypi.org/project/selenium-wire/), but upwork blocked my automation when i did that, so i gave up on that idea.

  After simple testing the flow with selenium, i refatored the project to follow the Clean Archicture, that is my favorite code design, and improve some aspects of the code.

  The result of my last run is in jobs and user_informations.json, i used bobbybackupy user.
</p>

<p>
  My principal difficulty in this challenge was work with python ecossystem, i usually work with Node, things like the dependencies management , docker configuration, lint checks, tests, things that could be better if i got used to the standards.

  The project has improvent, like:
  - Config dockerfile
  - CI/CD with lint check
  - Unit tests
  - More resilient flow
</p>

## 🚀 Technologies

Technologies that was used to build this application

- [Python 3.10](https://www.python.org/)
- [Poetry 1.3](https://python-poetry.org/)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Webdriver manager](https://pypi.org/project/webdriver-manager/)
- [Python doetenv](https://pypi.org/project/python-dotenv/)

## 💻 Getting Started

### Requirements

- [Python 3.10](https://www.python.org/)
- [Poetry 1.3](https://python-poetry.org/)

### Run
The dockerfile image not it's working, so it's necessary have installed the python and the poetry.

You need to add a .env file follow a .env.example.

Now it's just enter in the project and run:

```python
poetry install

poetry run python src/main.py
```

and see the result in jobs.json and user_informations.json files that will be created

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with 💜 by Isaque Diniz 👋 [See my linkedin](https://www.linkedin.com/in/isaquetdiniz/)

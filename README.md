# Telegram_Bot
## Overview:
A Telegram Bot is a program that behaves like a regular chat partner with additional functions. It performs predefined tasks independently and without the user's involvement. The term bot is derived from the term for the robot. We can configure a bot for different purposes. e.g., Relevant machine data such as temperature or pressure information can be sent regularly via Telegram Bot to the department managers' tablets, smartphones, or PC workstations. This way, a complete overview of machine production is possible for this user group at any time.

The project is based on a Cloud architecture where I tried to create a basic Telegram Bot with essential functions. In the future, we can add more functionalities to this bot to get sensor data from sensors through serverless computing in real-time and store it in a NoSQL database to be easily accessible.

In the current position, the bot can suggest you exercise or work out according to the weather outside. Currently, we have to select a weather condition manually, but later we can also connect the bot to the actual sensors through serverless computing / AWS to get data from sensors & make decisions according to sensor data. 

## Installation and usage
#### 1. Docker
#### 2. Localstack
#### 3. AWS CLI
#### 4. boto3
#### 5. Telethon
#### 6. Python

## Setting up the environment
#### 1. Clone the repository 
```git clone https://github.com/waseemafzal70/Telegram_Bot.git```

#### 2. Run Localstack
```docker run --rm -it -p 4566:4566 -p 4571:4571 localstack/localstack```

#### 3. Install the requried libraries
1. ```pip install Telethon```
2. ```pip install boto3```
if you don't have pip installed already install pip first.

#### 4. Bot token
Go to telegram messenger and search for @BotFather with the help of @BotFather create your bot token and replace it with Bot_token in main.py in project root directory.
Note: The token that is already in main.py will not work.

#### 5. Run project
Open CMD and navigate to project root directory. Then run the following command:
```python3 main.py```
at this stage the project will be running and you can test it in telegram messenger.

## Future work
This bot is a base for IoT devices, we can connect actual sensors with this bot or we can also connect acctuators with this bot. We can also take make desicions on the sensor stream that we recieve from the sensors in serverless computing. 

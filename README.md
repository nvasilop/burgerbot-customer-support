# BurgerBot — Dialogflow ES Customer Support Chatbot
**Live Demo:** Try BurgerBot https://burgerbot-customer-support-1.onrender.com 
BurgerBot is a simple customer support chatbot for a fictional burger restaurant.

The goal of the project was to practice how a real conversational AI system works using Dialogflow ES, a small FastAPI backend, and manual QA testing.

## What the chatbot can do

BurgerBot can:

* show the menu
* take a burger order
* ask for missing information such as burger type or quantity
* handle order problems
* check the status of an order
* provide opening hours
* connect the user with human support
* handle unsupported questions with a fallback response

## Conversational AI

The chatbot was built with Dialogflow ES.

I created:

* intents for different user requests
* custom entities such as burger type and issue type
* parameters such as quantity and order number
* required parameters and multi-turn conversations
* fallback handling
* human escalation

Example:

User:
`I want to place an order.`

Bot:
`Which burger would you like?`

User:
`Cheeseburger`

Bot:
`How many burgers would you like?`

User:
`2`

Bot confirms the order.

## Order Status Webhook

The `order_status` intent is connected to a FastAPI webhook.

Example:

User:
`Where is order 5678?`

Flow:

`Dialogflow → FastAPI webhook → orders.json → response`

The backend finds the order status and returns:

`Order 5678 is Out for delivery.`

The FastAPI backend is deployed on Render.

## QA Testing

I created 10 manual test cases for the chatbot.

The tests cover:

* intent classification
* paraphrases
* entity and parameter extraction
* missing information
* multi-turn conversations
* order problems
* order status
* human escalation
* fallback handling

All 10 test cases passed.

The test cases are available in:

`tests/test-cases.md`

## Project Structure

```text
backend/
├── main.py
├── orders.json
├── requirements.txt
└── Procfile

tests/
└── test-cases.md
```

## Technologies

* Dialogflow ES
* Python
* FastAPI
* JSON
* Webhooks
* Render
* Git / GitHub

## What I learned

Through this project I practiced how to:

* design intents and entities
* extract parameters from user input
* build multi-turn chatbot flows
* connect Dialogflow to a backend through a webhook
* create a simple API with FastAPI
* test conversational AI behaviour
* deploy a backend online

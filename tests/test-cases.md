# BurgerBot QA Test Cases

## TC-001 — Menu question / Happy Path

**User input:** What burgers do you have?

**Expected intent:** menu_question

**Expected result:** Bot shows the available menu.

**Actual intent:** menu_question

**Actual result:** We offer Classic Burger, Cheeseburger, Bacon Burger, Veggie Burger, fries and soft drinks. What would you like?

**Status:** PASS

**Notes:** Correct intent classification and expected menu response.

## TC-002 — Menu question / Paraphrase

**User input:** What kind of food can I get here?

**Expected intent:** menu_question

**Expected result:** Bot shows the available menu.

**Actual intent:** menu_question

**Actual result:** We offer Classic Burger, Cheeseburger, Bacon Burger, Veggie Burger, fries and soft drinks. What would you like?

**Status:** PASS

**Notes:** Correctly classified a paraphrased user request that was not an exact training phrase.

## TC-003 — Place order / Happy Path

**User input:** I want two cheeseburgers.

**Expected intent:** place_order

**Expected parameters:**
- burger_type = cheeseburger
- quantity = 2

**Expected result:** Bot correctly recognizes the order and extracts the required order information.

**Actual intent:** place_order

**Actual parameters:**
- burger_type = cheeseburger
- quantity = 2

**Actual result:** Correct intent classification and parameter extraction.

**Status:** PASS

**Notes:** Dialogflow correctly extracted both burger_type and quantity.

## TC-004 — Place order / Missing Information

**User input:** I want to place an order.

**Expected intent:** place_order

**Expected conversation:**
- Bot: Which burger would you like?
- User: Cheeseburger
- Bot: How many burgers would you like?
- User: 2

**Expected result:** Bot confirms the order after collecting the missing required parameters.

**Actual intent:** place_order

**Actual result:**
- Bot asked for the missing burger type.
- After "Cheeseburger", the bot asked for quantity.
- After "2", the bot confirmed the order.

**Status:** PASS

**Notes:** Correct multi-turn slot filling for missing required parameters.

## TC-005 — Order problem / Happy Path

**User input:** My fries are missing.

**Expected intent:** order_problem

**Expected conversation:**
- Bot: Please provide your order number.
- User: 245

**Expected result:** Bot registers the issue for order 245.

**Actual intent:** order_problem

**Actual parameters:**
- issue_type = missing
- order_number = 245

**Actual result:** Thank you. I've registered the issue for order 245.

**Status:** PASS

**Notes:** Correct intent classification, issue type extraction, order number capture, and multi-turn slot filling.

## TC-006 — Order problem / Paraphrase

**User input:** There is something missing from my delivery.

**Expected intent:** order_problem

**Expected result:** Bot asks for the order number and identifies the issue as missing.

**Actual intent:** order_problem

**Actual parameters:**
- issue_type = missing
- order_number = 34

**Actual result:** Thank you. I've registered the issue for order 34.

**Status:** PASS

**Notes:** Correctly classified a paraphrased complaint and extracted the issue type as missing. The bot then captured the order number and completed the flow.

## TC-007 — Order status / Happy Path

**User input:** Where is order 5678?

**Expected intent:** order_status

**Expected parameters:**
- order_number = 5678

**Expected result:** Bot starts checking the status of order 5678.

**Actual intent:** order_status

**Actual parameters:**
- order_number = 5678

**Actual result:** Thanks! I'm checking the status of order 5678.

**Status:** PASS

**Notes:** Correct intent classification and order number extraction.

## TC-008 — Opening hours / Paraphrase

**User input:** Are you open this evening?

**Expected intent:** opening_hours

**Expected result:** Bot provides the restaurant opening hours.

**Actual intent:** opening_hours

**Actual result:** We are open every day from 12:00 PM to 11:00 PM.

**Status:** PASS

**Notes:** Correctly classified a paraphrased opening-hours question and returned the expected response.

## TC-009 — Human support / Escalation

**User input:** I need to speak to a real person.

**Expected intent:** human_support

**Expected result:** Bot offers to connect the user with a human support agent.

**Actual intent:** human_support

**Actual result:** Of course. I’ll connect you with a member of our support team.

**Status:** PASS

**Notes:** Correctly identified the request for human assistance and triggered the escalation response.

## TC-010 — Fallback / Out-of-Scope

**User input:** Can you recommend a movie?

**Expected intent:** Default Fallback Intent

**Expected result:** Bot explains that it did not understand and guides the user toward supported topics.

**Actual intent:** Default Fallback Intent

**Actual result:**
Sorry, I didn't understand that. You can ask me about the menu, place an order, check an order status, report a problem, ask about opening hours, or speak to support.

**Status:** PASS

**Notes:** Correctly rejected an out-of-scope request and triggered the fallback response.

## Test Methodology

- All tests were executed manually using the Dialogflow ES simulator.
- Each independent test case was executed with a clean Dialogflow context/session.
- Tests covered intent classification, paraphrase handling, entity extraction, parameter extraction, required parameters, multi-turn slot filling, escalation, and fallback handling.
- All 10 test cases passed.

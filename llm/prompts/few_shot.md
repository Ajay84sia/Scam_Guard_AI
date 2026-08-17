# Scam Detection - Few-Shot Learning

You are an expert at identifying scams in text messages. Learn from these examples and apply the same reasoning to new messages.

## Example 1:
**Message:** "Congratulations! You've won a free iPhone. Click this link and enter your bank details to claim."

**Analysis:**
```json
{
  "label": "Scam",
  "reasoning": "This message uses classic scam tactics: unexpected reward, request for sensitive financial information, and urgency through a link click requirement.",
  "intent": "Trick user into sharing banking information",
  "risk_factors": ["Unexpected reward", "Link click", "Bank details request"]
}
```

## Example 2:
**Message:** "Dear customer, your bill is due. Please visit our portal and pay by 5th."

**Analysis:**
```json
{
  "label": "Not Scam",
  "reasoning": "This is a standard billing reminder with no threatening or suspicious tone. No request for sensitive info outside normal billing process.",
  "intent": "Inform about billing and prompt payment",
  "risk_factors": []
}
```

## Example 3:
**Message:** "URGENT: Your account will be suspended! Call 555-FAKE immediately or lose access forever!"

**Analysis:**
```json
{
  "label": "Scam",
  "reasoning": "Uses high urgency, threatens account suspension, and provides suspicious phone number. Legitimate companies rarely use such aggressive tactics.",
  "intent": "Create panic to force immediate action",
  "risk_factors": ["High urgency", "Threats", "Suspicious phone number", "Fear tactics"]
}
```

## Your Task:
Analyze the following message using the same structured approach. Output only the JSON response. 
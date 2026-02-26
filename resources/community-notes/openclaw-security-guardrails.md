# OpenClaw - Security Guardrails (ClawBands)

## What is ClawBands?

A security layer that acts like sudo for your AI agent. It intercepts every tool call (API requests, file writes, etc.) before execution, pauses the agent, and asks for your explicit approval on anything risky. Creates an immutable audit trail of every decision.

## Installation

```bash
npm install -g clawbands
clawbands init
openclaw restart
```

## Policy Configuration

Example: Alibaba access for research without purchasing ability:

```json
{
  "policies": {
    "network": {
      "*.alibaba.com/api/search*": "ALLOW",
      "*.alibaba.com/api/product*": "ALLOW",
      "*.alibaba.com/api/createPurchaseOrder*": "ASK",
      "*.alibaba.com/api/pay*": "DENY"
    }
  }
}
```

### Policy Levels

- **ALLOW** - Agent can do this automatically
- **ASK** - Agent pauses and asks for your approval
- **DENY** - Blocked entirely

## Best Practices

### Use Read-Only APIs for Research

- Alibaba Product Scraper API via Apify (searching, extracting supplier info, monitoring prices)
- 1688 Open Platform APIs for category lookups (read-only endpoints like `category.level.attr.get`)
- These don't create orders

### Reorder Requests Without Purchasing

With the "ASK" policy, when your agent identifies a reorder need:
1. Agent drafts purchase order details using CreatePurchaseOrder API
2. ClawBands intercepts the call
3. Sends you a message: "Reorder needed for Product X. Approve? YES/NO"
4. You approve manually, then the agent proceeds

Note: Alibaba's CreatePurchaseOrder API returns an order ID but doesn't automatically process payment.

### Additional Safety Measures

- **Dedicated sub-accounts** - Use a separate Alibaba sub-account, not your primary
- **Cloud server deployment** - Deploy OpenClaw on a cloud server (DigitalOcean, Vercel, SimpleClaw) for 24/7 operation with better isolation

## Overview

This article outlines the specific quotas and pricing applicable to Gemini CLI
when using different authentication methods.

The following table summarizes the available quotas and their respective limits:

| Authentication method | Tier / Subscription             | Maximum requests per user per day |
| :-------------------- | :------------------------------ | :-------------------------------- |
| **Google account**    | Gemini Code Assist (Individual) | 1,000 requests                    |
|                       | Google AI Pro                   | 1,500 requests                    |
|                       | Google AI Ultra                 | 2,000 requests                    |
| **Gemini API key**    | Free tier (Unpaid)              | 250 requests                      |
|                       | Pay-as-you-go (Paid)            | Varies                            |
| **Vertex AI**         | Express mode (Free)             | Varies                            |
|                       | Pay-as-you-go (Paid)            | Varies                            |
| **Google Workspace**  | Code Assist Standard            | 1,500 requests                    |
|                       | Code Assist Enterprise          | 2,000 requests                    |
|                       | Workspace AI Ultra              | 2,000 requests                    |

Generally, there are three categories to choose from:

- Free Usage: Ideal for experimentation and light use.
- Paid Tier (fixed price): For individual developers or enterprises who need
  more generous daily quotas and predictable costs.
- Pay-As-You-Go: The most flexible option for professional use, long-running
  tasks, or when you need full control over your usage.

Requests are limited per user per minute and are subject to the availability of
the service in times of high demand.
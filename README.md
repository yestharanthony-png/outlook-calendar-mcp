# Outlook Calendar MCP

## Overview

Outlook Calendar MCP Server built using FastMCP and Microsoft Graph API.

This MCP server allows AI agents to manage Outlook Calendar events through Microsoft Graph.

---

## Features

- Create Calendar Event
- Update Calendar Event
- Delete Calendar Event
- List Calendar Events
- Get Calendar Schedule

---

## Project Structure

```text
outlook-calendar-mcp/
│
├── server.py
├── graph_client.py
├── config.py
├── .env
│
├── tools/
│   ├── create_event.py
│   ├── update_event.py
│   ├── delete_event.py
│   ├── list_events.py
│   └── get_schedule.py
│
├── requirements.txt
└── README.md
```

---

## Authentication

This project uses Microsoft Entra ID Client Credentials Flow.

Required credentials:

- Tenant ID
- Client ID
- Client Secret

Store them in:

```env
TENANT_ID=
CLIENT_ID=
CLIENT_SECRET=
```

---

## Installation

Create virtual environment:

```powershell
python -m venv .venv
```

Activate:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install packages:

```powershell
pip install -r requirements.txt
```

---

## Run MCP Server

```powershell
python server.py
```

---

## Workflow

1. MCP Tool receives request.
2. Graph Client generates Microsoft access token.
3. Tool calls Microsoft Graph API.
4. Microsoft Graph updates Outlook Calendar.
5. Response is returned to MCP Client.

---

## APIs Used

Microsoft Graph API

Examples:

```http
POST /users/{email}/events
GET /users/{email}/events
PATCH /users/{email}/events/{event_id}
DELETE /users/{email}/events/{event_id}
```
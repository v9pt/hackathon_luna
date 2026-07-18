# Beginner's Guide: How to Use AI Agents

If you have never used AI agents before, think of them as **AI-powered teammates** who are specialists in different jobs. 

There are two ways to use this setup depending on your preference: **Autopilot Mode** (where I do the work and you supervise) or **Manual Mode** (where you run the agents yourself in separate chats).

---

## ⚡ Autopilot Mode (Recommended)

Since I am an agentic coding assistant with full access to your workspace, **I can act as the Orchestrator and execute all these agent roles for you.** You do not need to copy-paste profiles or open different chats.

Simply tell me your goal:
> *"I want to build a [feature name]. Go into Autopilot Mode, run the planning and design steps, write the code, and test it."*

**Your role is to supervise:**
1. I will write an **Implementation Plan** and ask for your feedback.
2. Once you approve, I will run the code edits and shell commands.
3. You just review my changes and approve command executions when prompted.

---

## 👥 Manual Mode (Using Separate Chats)

If you prefer to copy-paste the profiles into separate ChatGPT/Claude/Gemini chats, you can talk to these specialized agents one by one. This guide shows you exactly how to do that step-by-step.

---

## 👥 Meet Your AI Team

In this project, under the [`.agents/`](file:///.agents/) folder, you have 7 files. Each file is a "brain profile" for a different role:

1.  **CEO (CTO / Manager)**: The planner. Tell him what you want to build, and he will write down a step-by-step list of tasks.
2.  **Architect**: The designer. He designs database schemas and writes down API contracts (how the backend and frontend talk to each other).
3.  **Research**: The googler. Ask him to find the best libraries or lookup documentation for you.
4.  **Backend**: The database & API coder. Writes the server-side logic.
5.  **Frontend**: The UI coder. Builds the pages, buttons, and visual design.
6.  **AI Engineer**: The LLM coder. Integrates models, vector search, and prompts.
7.  **QA (Tester)**: The checker. Writes tests to make sure everything works and has no bugs.

---

## 🛠️ Step-by-Step: How to Use Them

When you start a conversation with your AI assistant (e.g., ChatGPT, Claude, Gemini, Cursor, or Copilot), follow this simple workflow:

### Step 1: Start with the CEO (Planning)
Upload or copy-paste the contents of [`.agents/CEO.md`](file:///.agents/CEO.md) into your AI chat window and say:
> *"Here is your role profile. I want to build a [describe your feature, e.g., 'a simple chat app']. Please create a plan and break it down into tasks."*

### Step 2: Design with the Architect (API Contracts)
Once you have a plan, open a new chat window, load the contents of [`.agents/architect.md`](file:///.agents/architect.md), and say:
> *"Here is your role profile. Based on our plan, design the database tables and define the API endpoints we need so that our Backend and Frontend engineers can work at the same time."*

### Step 3: Code in Parallel (Backend & Frontend)
To code the app, open two separate chats or tasks:
*   **For UI**: Load [`.agents/frontend.md`](file:///.agents/frontend.md) and ask the AI to build the React/Next.js screens using the API designs from Step 2.
*   **For Server**: Load [`.agents/backend.md`](file:///.agents/backend.md) and ask the AI to code the FastAPI/Node.js endpoints.

### Step 4: Verify with QA (Testing)
Finally, load [`.agents/qa.md`](file:///.agents/qa.md) and say:
> *"Here is the code we wrote. Write automated tests using Playwright/Vitest to make sure everything works perfectly and nothing is broken."*

---

## 💡 Pro Tips for the Hackathon

*   **Load the Skills**: When an agent is coding, tell them to reference the files in the [`skills/`](file:///Users/zaif/Desktop/NEW/skills/) directory. For example, tell the Frontend agent: *"Look at `skills/frontend/ui/dark_mode.md` to see how we handle styling."*
*   **Keep Chats Separate**: Don't use one single chat window for everything. Use a new chat for each agent role so they don't get confused.
*   **No Code Placeholders**: Make sure to enforce the [Shared Engineering Rules](file:///.agents/shared_rules.md). Tell the AI: *"Do not write comments like '// TODO: implement later'. Write the complete code."*

# Recipe-Agent-App
**AI-Powered Kitchen Assistant with Database Tool Integration**

This project demonstrates a robust, data-aware agent built using the Google Gemini CLI and a custom MCP Toolbox to manage a local SQLite database. The agent translates complex natural language requests (e.g., "What can I cook?") into executable SQL queries, showcasing advanced Tool-Augmented Reasoning and seamless integration between Generative AI and structured data.

🌟 **Key Features**

**Natural Language to SQL:** Gemini accurately translates user requests into valid SELECT, INSERT, and UPDATE SQLite queries.\
**Inventory Management:** Users can update their available ingredients using simple conversation (e.g., "I bought 1kg of Onions").\
**Recipe Suggestion:** The agent performs complex SQL joins against the database to suggest recipes based on the user's current inventory and cuisine preferences.\
**Custom Tooling:** Utilizes the MCP Toolbox as a standardized execution layer, allowing the agent to perform deterministic actions (database access) reliably.\
**Schema Context Injection:** The project leverages the tool's description in the tools.yaml file to provide the LLM with the complete database schema, enabling accurate SQL generation.

🚀 **Architecture and Flow**

The agent operates on a Tool-Augmented Reasoning loop, where the Gemini LLM is the brain and the MCP Toolbox is the hand:\
**User Input (CLI):** Query sent to the Gemini CLI.\
**LLM Reasoning:** Gemini analyzes the request, references the database schema in the tool's description, and generates a valid SQL query string.\
**MCP Server Execution:** The Gemini CLI routes the query string to the running MCP Server.\
**Database Interaction:** The server executes the SQL against the local Recipes.db file.\
**Final Response:** Gemini synthesizes the clean output into a conversational answer for the user.

🛠️ **Setup and Installation**

**1. Prerequisites**\
    &nbsp;&nbsp;Python 3.8+\
    &nbsp;&nbsp;Gemini CLI (pip install gemini-cli)\
    &nbsp;&nbsp;MCP Toolbox and Server (Installation per internal instructions)\
    &nbsp;&nbsp;SQLite3 (The database engine)\
**2. Database Preparation**\
    &nbsp;&nbsp;**Create Database**: Create the file Recipes.db\
    &nbsp;&nbsp;**Define Schema**: Populate the database with the required tables (Recipes, Ingredients, Inventory, and Recipe_Ingredients) and initial data\
**3. Tool Configuration (tools.yaml)** \
    &nbsp;&nbsp;The tools.yaml file defines the bridge and provides the schema context to Gemini LLM\
**4. Running the Agent**\
    &nbsp;&nbsp;**Start MCP Server:** Run the command to start your MCP Server (this loads the tools.yaml).
    
> &nbsp;&nbsp; &nbsp;&nbsp;command to start MCP server\
> &nbsp;&nbsp; &nbsp;&nbsp;`toolbox --tools-file "tools.yaml"`

   &nbsp;&nbsp;**Configure CLI**: Use the Gemini CLI command to register the running MCP Server endpoint.
    
> &nbsp;&nbsp; &nbsp;&nbsp;command to add started MCP server to list of MCPs in CLI\
> &nbsp;&nbsp; &nbsp;&nbsp;`gemini mcp add --scope="project" --transport="http" "MCPToolbox" "http://localhost:5000/mcp"`  &nbsp; _usually MCP server picks 5000 port by default unless explicitly mentioned_

   &nbsp;&nbsp;**Interact:** Start querying the agent.

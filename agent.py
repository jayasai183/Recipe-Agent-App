from google.adk.agents.llm_agent import Agent
from toolbox_core import ToolboxSyncClient

toolbox = ToolboxSyncClient("http://127.0.0.1:5000")

tools = toolbox.load_tool('execute_sql_tool')

root_agent = Agent(
    model='gemini-2.5-flash',
    name='recipe_agent',
    description='A helpful assistant that helps user with recipes using available ingredients',
    instruction='''Answer user questions about different recipes that you know of from the local database.
    Guide them with cooking instructions and also help them with recipes based on available ingredients.
    According to the user request, Add/delete/fetch the ingredients available in the inventory''',
    tools=[tools],
)

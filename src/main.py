from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from lightbulb import BotApp

load_dotenv()

bot = BotApp(token=getenv("TOKEN"))

for path_name in Path("./commands").glob("*.py"):
    command_path = str(path_name).replace("/", ".").removesuffix(".py")
    bot.load_extensions(command_path)

bot.run(
    asyncio_debug=True,
    coroutine_tracking_depth=20,
    propagate_interrupts=True,
    check_for_updates=True,
)

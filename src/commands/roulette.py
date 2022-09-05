from hikari import MessageFlag
from lightbulb import option, implements, SlashCommand, Context, BotApp, command, Plugin

from src.utils.comp_creator import CompCreator
from src.utils.create_comp_embed import create_comp_embed

plugin = Plugin("roulette")


@plugin.command()
@option(
    name="support_count",
    description="How many supports you want.",
    type=int,
    required=True,
    max_value=20,
    autocomplete=True,
)
@option(
    name="healer_count",
    description="How many healers you want.",
    type=int,
    required=True,
    max_value=20,
    autocomplete=True,
)
@option(
    name="tank_count",
    description="How many tanks you want.",
    type=int,
    required=True,
    max_value=20,
    autocomplete=True,
)
@option(
    name="group_size",
    description="Size of your roaming party.",
    type=int,
    required=True,
    max_value=20,
    min_value=1,
    autocomplete=True,
)
@command(
    name="roulette",
    description="Starts an Albion roam roulette.",
)
@implements(SlashCommand)
async def roulette(ctx: Context) -> None:
    if ctx.options.group_size < (
            ctx.options.healer_count +
            ctx.options.tank_count +
            ctx.options.support_count
    ):
        await ctx.respond(
            content="Group size too small for role selections",
            flags=MessageFlag.EPHEMERAL
        )
        return

    comp = CompCreator(
        group_size=ctx.options.group_size,
        healer_count=ctx.options.healer_count or 0,
        tank_count=ctx.options.tank_count or 0,
        support_count=ctx.options.support_count or 0
    ).create_comp()

    embed_response = await create_comp_embed(comp)

    await ctx.respond(embed_response)


def load(bot: BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(plugin)

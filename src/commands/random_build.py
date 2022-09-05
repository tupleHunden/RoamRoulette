from random import choice

from lightbulb import option, implements, SlashCommand, Context, BotApp, command, Plugin

from src.models.healer_weapons import healer_weapons
from src.models.melee_dps_weapons import melee_dps_weapons
from src.models.ranged_dps_weapons import ranged_dps_weapons
from src.models.role import Role
from src.models.support_weapons import support_weapons
from src.models.tank_weapons import tank_weapons

plugin = Plugin("random_build")


@plugin.command()
@option(
    name="role",
    description="Which role to to play.",
    required=True,
    choices=Role.list_roles()
)
@command(
    name="random_build",
    description="Picks a random build for you to play.",
)
@implements(SlashCommand)
async def random_build(ctx: Context) -> None:
    match ctx.options.role:
        case Role.TANK.value:
            await ctx.respond(choice(tank_weapons))
            return
        case Role.HEALER.value:
            await ctx.respond(choice(healer_weapons))
            return
        case Role.SUPPORT.value:
            await ctx.respond(choice(support_weapons))
            return
        case Role.RANGED_DPS.value:
            await ctx.respond(choice(ranged_dps_weapons))
            return
        case Role.MELEE_DPS.value:
            await ctx.respond(choice(melee_dps_weapons))
            return


def load(bot: BotApp) -> None:
    bot.add_plugin(plugin)


def unload(bot: BotApp) -> None:
    bot.remove_plugin(plugin)

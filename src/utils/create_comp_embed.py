from hikari import Embed

from src.models.role import Role


async def create_comp_embed(comp: dict[Role, list[str]]) -> Embed:
    embed_response = Embed(title="Roulette Generated Comp")
    embed_response.set_footer("Send silver donations to Alchemist8")
    embed_response.add_field(
        name="Tanks",
        value="".join("{}\n".format(tank) for tank in comp.get(Role.TANK)) or "No Tanks",
        inline=True
    )
    embed_response.add_field(
        name="Healers",
        value="".join("{}\n".format(healer) for healer in comp.get(Role.HEALER)) or "No Healers",
        inline=True
    )
    embed_response.add_field(
        name="Supports",
        value="".join("{}\n".format(support) for support in comp.get(Role.SUPPORT)) or "No Supports",
        inline=True
    )
    embed_response.add_field(
        name="Melee DPS",
        value="".join(("{}\n".format(dps) for dps in comp.get(Role.MELEE_DPS))) or "No Melee DPS",
        inline=True
    )
    embed_response.add_field(
        name="Ranged DPS",
        value="".join(("{}\n".format(dps) for dps in comp.get(Role.RANGED_DPS))) or "No Ranged DPS",
        inline=True
    )
    embed_response.set_thumbnail("https://render.albiononline.com/v1/item/T7_POTION_STONESKIN.png?count=5&quality=0")
    return embed_response

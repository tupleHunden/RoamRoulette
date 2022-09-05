from enum import Enum


class Role(Enum):
    TANK = "Tank"
    HEALER = "Healer"
    SUPPORT = "Support"
    RANGED_DPS = "Ranged DPS"
    MELEE_DPS = "Melee DPS"

    @classmethod
    def list_roles(cls) -> list[str]:
        return list(str(role.value) for role in Role)

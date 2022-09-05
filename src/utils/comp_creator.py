from math import floor
from random import choices

from src.models.healer_weapons import healer_weapons
from src.models.melee_dps_weapons import melee_dps_weapons
from src.models.ranged_dps_weapons import ranged_dps_weapons
from src.models.role import Role
from src.models.support_weapons import support_weapons
from src.models.tank_weapons import tank_weapons


class CompCreator:
    _group_size: int
    _healer_count: int
    _tank_count: int
    _support_count: int
    _melee_dps_count: int
    _ranged_dps_count: int
    _tank_selections: list[str] = []
    _healer_selections: list[str] = []
    _melee_dps_selections: list[str] = []
    _ranged_dps_selections: list[str] = []
    _support_selections: list[str] = []

    def __init__(
            self,
            group_size: int = 2,
            healer_count: int = 0,
            tank_count: int = 0,
            support_count: int = 0
    ):
        self._group_size = group_size
        self._healer_count = healer_count
        self._tank_count = tank_count
        self._support_count = support_count

    def _create_tanks(self) -> None:
        self._tank_selections = choices(population=tank_weapons, k=self._tank_count)

    def _create_healers(self) -> None:
        self._healer_selections = choices(population=healer_weapons, k=self._healer_count)

    def _create_supports(self) -> None:
        self._support_selections = choices(population=support_weapons, k=self._support_count)

    def _create_dps(self) -> None:
        self._split_dps_allocations()
        self._melee_dps_selections = choices(population=melee_dps_weapons, k=self._melee_dps_count)
        self._ranged_dps_selections = choices(population=ranged_dps_weapons, k=self._ranged_dps_count)

    def _split_dps_allocations(self):
        dps_count = self._group_size - self._support_count - self._healer_count - self._tank_count
        if dps_count % 2 == 0:
            self._melee_dps_count = int(dps_count / 2)
            self._ranged_dps_count = int(dps_count / 2)
        else:
            # 9 / 2 = 4.5 melee, 4.5 ranged
            # 4.5 rounded down = 4 melee, 4 ranged
            # increase melee by one to reach 9
            self._melee_dps_count = int(floor(dps_count / 2) + 1)
            self._ranged_dps_count = int(floor(dps_count / 2))

    def create_comp(self) -> dict[Role, list[str]]:
        if self._tank_count != 0:
            self._create_tanks()

        if self._healer_count != 0:
            self._create_healers()

        if self._support_count != 0:
            self._create_supports()

        self._create_dps()

        return {
            Role.TANK: self._tank_selections,
            Role.HEALER: self._healer_selections,
            Role.SUPPORT: self._support_selections,
            Role.MELEE_DPS: self._melee_dps_selections,
            Role.RANGED_DPS: self._ranged_dps_selections
        }

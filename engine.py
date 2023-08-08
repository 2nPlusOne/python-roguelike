from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from input_handlers import EventHandler

if TYPE_CHECKING:
    from entity import Entity
    from game_map import GameMap


class Engine:
    def __init__(self, player: Entity):
        self.event_handler: EventHandler = EventHandler(self)
        self.player = player
        self.game_map: Optional[GameMap] = None
        self.fov_radius = 10

    def handle_enemy_turns(self) -> None:
        for entity in set(self.game_map.entities) - {self.player}:
            print(f"The {entity.name} wonders when it will get to take a real turn.")

    def update_fov(self) -> None:
        """Recompute the visible area based on the players point of view."""
        self.game_map.visible = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=self.fov_radius,
        )
        # If a tile is "visible" it should be added to "explored"
        self.game_map.explored |= self.game_map.visible

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)
        context.present(console)
        console.clear()

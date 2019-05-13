# TO-DO

Bugs
- [ ] Minos change at top and left
- [ ] Mino clips into the side on rotate

Architecture
- [ ] Move render from GameLogic to main Tketris class
- [ ] Rename clock_tick_update to update in GameLogic
- [ ] Rename boundaries in board tileset to more appropriately match action
    - [ ] Rename right to left and left to right
    - [ ] Rename up to down
- [ ] Replace actions with a controller mixin
- [ ] Update transform_tileset to use modulus instead of floats in transform matrix

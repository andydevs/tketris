# TO-DO

Bugs
- [x] Minos change at top and left
- [x] Mino clips into the side on rotate
- [ ] Mino clips into tiles on rotate

Game Play
- [ ] Hard drop
- [ ] Game actually speeds up at higher score

Architecture
- [ ] Move render from GameLogic to main Tketris class
- [ ] Rename clock_tick_update to update in GameLogic
- [ ] Rename boundaries in board tileset to more appropriately match action
    - [ ] Rename right to left and left to right
    - [ ] Rename up to down
- [x] Replace actions with a controller mixin
- [ ] Update transform_tileset to use modulus instead of floats in transform matrix

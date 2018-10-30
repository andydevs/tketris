# TO-DO

- Do Now
    - Add better documentation describing implementation [in progress]
        - Comments
        - README.md
    - Publish to PyPI
- Architecture
    - Move render from GameLogic to main Tketris class
    - Rename clock_tick_update to update in GameLogic
    - Rename boundaries in board tileset to more appropriately match action
        - Rename right to left and left to right
        - Rename up to down
    - Implement actions as good handlers
        - Install/Add good_handlers Dependency

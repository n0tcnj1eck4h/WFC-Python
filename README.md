# WFC-Python
[Wave Function Collapse](https://github.com/mxgmn/WaveFunctionCollapse) algorithm implemented in Python.

## Example output
```python
tiles.add(Tile('┌', [0, 1, 1, 0]))   
tiles.add(Tile('┐', [0, 0, 1, 1]))  # Example output for this tileset definition:
tiles.add(Tile('└', [1, 1, 0, 0]))  # ║│╷│╶╫┼╫┐└┬─╜└╜┌┴┘║╷└┴┐┌┤╓╫╫┐╓┴┐║╓┴┼╜ ║║╶─┘ ╶┴┐║├┘
tiles.add(Tile('┘', [1, 0, 0, 1]))  # ╜└┼┴┐║│║├─┘╶┐┌─┘╷┌╫┴┐┌┴┴┴╫╫╫┴╫─┴╜║ │  ║║ ┌┐┌┐╓┼╫┤ 
tiles.add(Tile('┼', [1, 1, 1, 1]))  # ┐╷├┐└╫┴╫┴┐╷╷├┴┐┌┴┘║╓┘│╶┐╓╫╜║┌╫┐ ╓╜╶┴┐╓╜║╶┴┴┴┘║└╫┴┬
tiles.add(Tile(' ', [0, 0, 0, 0]))  # ├┴┼┴┐║ ║╓┴┘│└─┤└─┐║║╓┴─┴╫╜┌╜├╜│╶╜  ╷├╜┌╫┐ ╷ ╓╫─╜╶┼
tiles.add(Tile('│', [1, 0, 1, 0]))  # ┤╶┘╶┴╫┐║║╶┐└┐╷└┬─┘║║║ ╓─╫┐│╓┤╶┴┬┐ ╶┴┤ ├╫┤╓┴┬╫╜┌─┐├
tiles.add(Tile('─', [0, 1, 0, 1]))  # │╓┐╷╓╫┘║║ │ ││╶┤╷╓╜║║ ║╓╫┤│║└┐ │└┐ ╓┤╶┤║└╫┐│║╶┤┌┘└
tiles.add(Tile('├', [1, 1, 1, 0]))  # ┴╜│└╫╜╓╜║ │┌┤└┬┴┴╜╓╜║╓╫╫╫┤├╜╷└┬┴┐│┌╜└┬┘║╓╜├┘║╶┘│┌─
tiles.add(Tile('┤', [1, 0, 1, 1]))  # ╓─┘ ║╓╫─╫─┤└┤╷│╶┬┬╜╓╫╫╫╫╫┘├┬┴┬┘┌┼┘├┐╷│╶╫╜╶┴┐║ ╶┴┘╶
tiles.add(Tile('┬', [0, 1, 1, 1]))  # ║╓┐╶╫╫╫┐║╓┤╓┘├┤┬├┘╶╫╫╫╫╫╫┬┼┤╓┤╷└┘╓┴┼┤│╷║╷╷╓┴╫┤╷╓┬╶
tiles.add(Tile('┴', [1, 1, 0, 1]))  # ╬╬╪═╬╬╬╪╬╬╪╬═╪╪╪╪══╬╬╬╬╬╬╪╪╪╬╪╪══╬═╪╪╪╪╬╪╪╬═╬╪╪╬╪═
tiles.add(Tile('┴', [1, 1, 0, 1]))  # ╜║│╷║║║├╜║├╜╷├┼┴┴┬┬╜║║║║║└┘├╫┼┤╷╶╜╶┘├┼┴╜├┼╫─╫┴┴╜│┌
tiles.add(Tile('╶', [0, 1, 0, 0]))  # ┐║││║║║├┐║│┌┴┴┼┐╓┘│╓╫╫╜║║╷ │║└┤├──┬─┴┴┐┌┴┼╜╓╜╷╓┬┘├
tiles.add(Tile('╷', [0, 0, 1, 0]))  # └╫┴┼╫╜║│├╜└┼─┐│└╫┬┘║║║╶╫╫┴┐└╫┐└┴┬┬┘╷  ││ │╓╜┌┴╜└┐├
tiles.add(Tile('═', [0, 2, 0, 2]))  # ┐║╷│║╷║├┤ ┌┴┐└┴┬╫┤╓╫╜║╷║║┌┤╓╫┴┬─┤└┬┼┬┐├┼─┴╫┐│╓┬┬┴┤
tiles.add(Tile('║', [2, 0, 2, 0]))  # │║│├╫┴╫┼┤ │ ├─┐│║╶╜║ ║└╜║└┼╜║ └┐└─┴┤││└┤╷╶╜││║├┴┬┴
tiles.add(Tile('╬', [2, 2, 2, 2]))  # ┴╫┴┴╫┬╫┴┴┐└┬┴┐└┼╜╷╶╫┐║  ║╷└┬╫┬┬┤╓┬─┼┤├┐├┘╷╷│├╜│┌┤╶
tiles.add(Tile('╜', [2, 0, 0, 1]))  # ┬╫┐┌╫┴╜╶┬┴┬┼┐│╶┘ ├─╫┼╜┌┐║└─┼╫┘└┴╜├─┤│└┴┘╷│└┴┤╷│└┤ 
tiles.add(Tile('╓', [0, 1, 2, 0]))  # └╜└┴╜┌┬┐├┐│└┴┴┐ ╷│ ║└┐│├╜┌┐│║┌┐╶┬┘╷├┴─┐╶┤├┐╶┼┤└┬┤╓
tiles.add(Tile('╫', [2, 1, 2, 1]))  # ╶┐╓┐╷└┴┴┘││ ╓┬┤┌┴┤ ║ │││ ├┴┴╜└┼┬┼─┴┴┐ │╓┴┴┴┬┴┼┬┘│║
tiles.add(Tile('╪', [1, 2, 1, 2]))  # ┬┴╜├┘  ╶─┴┼┬╫┘├┴─┤┌╜┌┤└┼┬┘┌┐╓┐│└┘╷╓┐│╓┤║ ╶─┘╶└└╶└╫
```
(might look slightly misformatted due to GitHub not dealing well with spaces)

The manually defined tileset uses a concept of connectors, where the elements of the list represent connection ID's of the north, east, south and west faces respectively. 


# Solving-Search-Problems-through-A*

Generic implementation of A* algorithm that is deployed to solve the popular 8-Puzzle Problem and the Jumping Frog Problem in the search domain as part of CS-351 Artifical Intelligence Assignment. Some resources for this assignment were taken from  http://ai.berkeley.edu while the implementation is done from scratch. 

## 8-Puzzle Problem

8-puzzle consists of an area divided into a 3 by 3 grid. Each cell of the grid represents a tile numbered from 1 to 8 (in any order) with one tile being empty. A tile that is next to the empty cell can be moved into the empty space, leaving its previous position empty in turn. The aim of the puzzle is to achieve a given configuration of tiles from a given (different) configuration by sliding the individual tiles around the grid as described above. 

## Jumping Frogs Problem

The puzzle involves seven rocks and six frogs. See Fig. 1. The seven rocks are laid out in a horizontal line and numbered left to right. The six frogs are evenly divided into a green trio and a brown trio. The green frogs sit on Rocks 1, 2, and 3, facing right. The brown frogs sit on Rocks 5, 6, and 7, facing left. Rock 4 is vacant. The challenge is to transpose the trios, jumping the green frogs to Rocks 5, 6, and 7 and the brown frogs to Rocks 1, 2, and 3. Their movement is restricted. A frog can only jump forward, either hopping to a vacant rock one place ahead (cost =1) or leaping over its neighbor frog to a vacant rock two places ahead (cost = 2).

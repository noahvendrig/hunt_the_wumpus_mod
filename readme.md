# Samson


## Description
Samson is a Modern Recreation of text-based adventure game Hunt the Wumpus (1973). Further details can be found [on my website](http://noahvendrig.com#portfolio)
It takes ideas from the biblical figure Samson and the player is controlling Samson, who must navigate a network of caves in hopes of escaping. The hazards present in the cave include 2 lions (pits in the original HTW), 2 groups of bats (same as original HTW) and an army of Philistines (Wumpus in HTW). 
To eliminate the army of Philistines (to win the game), Samson has a limited ability (5 uses only) – A charge which when charging into a cave full of Philistines will eliminate them all. To successfully do this, the charge must be executed from an adjacent cave to the Philistines. If the player runs out of charges, they will lose the game as the enemies can no longer be defeated. If the player accidentally walks into a cave with the Philistines or a lion, they will lose. If the player walks into a cave with bats, they will be transported to a random cave in the network.
Points are rewarded for the shortest number of moves required to eliminate the Philistine Army. 

## Screenshots
![main](https://user-images.githubusercontent.com/69784959/127539731-77e2b5c0-8572-4a60-9633-94f9bbb18917.png)

![gameplay](https://user-images.githubusercontent.com/69784959/127539738-225fd676-4418-4405-8bb6-fdf42daa7859.png)
![](https://user-images.githubusercontent.com/69784959/127314132-a218f9d0-bccc-46e1-a444-555b7192d6ed.png)
![](https://user-images.githubusercontent.com/69784959/127539742-9a2c0511-8a38-424c-8241-16b94e2d8680.png)
![](https://user-images.githubusercontent.com/69784959/127539746-ec86090f-6581-42f8-84d3-eafc09795301.png)
![](https://user-images.githubusercontent.com/69784959/127539748-85682cc6-4d00-4e32-b8d8-80fa7f7ac200.png)
![](https://user-images.githubusercontent.com/69784959/127539754-206d77d9-02e4-41fe-92d0-98eeaa5c8e4f.png)

## Requirements and Installation

Python Version >= [3.8.10](https://www.python.org/downloads/release/python-3810/)\
Pygame Verson >= [2.0.1](https://www.pygame.org/project/5409/7928)
#### Creating a new Anaconda enviroment
``` bash
conda create --name samson python=3.8.1
```
#### Activating the Anaconda Environment
###### Windows: 
```
conda activate samson
``` 
###### Linux / macOS: 
```
conda source activate samson
```

#### Pygame Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [pygame](https://pypi.org/project/pygame/).
Run the following command into the terminal or Anaconda prompt:
``` bash
pip install pygame==2.0.1
```

## Usage
Enter the following into the terminal or Anaconda prompt to run the script:
###### Windows
``` bash
python main.py
```
###### Linux / macOs:
``` bash
python3 main.py
```

## Author
[Noah Vendrig](github.com/noahvendrig)


## License
[MIT License](https://prodicus.mit-license.org/)
Copyright (c) 2021 Noah Vendrig

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

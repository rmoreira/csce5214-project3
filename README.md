# CSCE5214 - Project3
Deep-Q learning with Flappy Bird


### Use Pycharm:
If you use PyCharm, most likely you should be able to install everything from the IDE.
If not follow the instructions bellow.

### Dependencies (pygame) Installation for MacOS:
```
brew install sdl2 sdl2_gfx sdl2_image sdl2_mixer sdl2_net sdl2_ttf pkg-config gcc
git clone https://github.com/pygame/pygame.git
cd pygame
python setup.py -config -auto -sdl2
python setup.py install
```

### PIP install:
```
pip3 install -r requirements.txt
```

### Train:
```
time SDL_VIDEODRIVER=dummy python3 train.py
```

### See what the bird learned:
```
python3 play.py
```

### Sample Output Training:
```
ᐅ time SDL_VIDEODRIVER=dummy python3 train.py
pygame 2.0.1.dev1 (SDL 2.0.12, python 3.8.3)
Hello from the pygame community. https://www.pygame.org/contribute.html
DISCOUNT RATE= 0.530000
LEARNING_RATE = 0.910000

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 1 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 5 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 9 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 11 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 15 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 17 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 18 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 22 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 24 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 25 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 37 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 65 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$ NEW RECORD: 100 $$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

******** Saving Q-table(641 keys) to local file... ********
******** Q-table(641 keys) updated on local file ********

Episode: 2500, highest score: 100, average: 2.0728
SDL_VIDEODRIVER=dummy python3 train.py  91.42s user 0.88s system 99% cpu 1:32.63 total
```

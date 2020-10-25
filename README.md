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

### Run App:
```
python3 FlappyBirdNEAT.py
```


### Sample Output:
```
pygame 2.0.0.dev23 (SDL 2.0.12, python 3.8.3)
Hello from the pygame community. https://www.pygame.org/contribute.html

 ****** Running generation 0 ******

Population's average fitness: 2.40100 stdev: 0.32939
Best fitness: 3.50000 - size: (1, 3) - species 1 - id 98
Average adjusted fitness: 0.155
Mean genetic distance 1.219, standard deviation 0.378
Population of 100 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    0   100      3.5    0.155     0
Total extinctions: 0
Generation time: 2.016 sec

 ****** Running generation 1 ******

Population's average fitness: 2.41400 stdev: 0.35129
Best fitness: 3.40000 - size: (2, 4) - species 1 - id 120
Average adjusted fitness: 0.178
Mean genetic distance 1.377, standard deviation 0.462
Population of 100 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    1   100      3.4    0.178     1
Total extinctions: 0
Generation time: 1.358 sec (1.687 average)

 ****** Running generation 2 ******

Population's average fitness: 2.54800 stdev: 1.57705
Best fitness: 17.90000 - size: (2, 5) - species 1 - id 224
Average adjusted fitness: 0.022
Mean genetic distance 1.538, standard deviation 0.477
Population of 100 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    2   100     17.9    0.022     0
Total extinctions: 0
Generation time: 3.169 sec (2.181 average)

 ****** Running generation 3 ******

Population's average fitness: 2.38800 stdev: 0.30175
Best fitness: 3.40000 - size: (1, 1) - species 1 - id 334
Average adjusted fitness: 0.157
Mean genetic distance 1.650, standard deviation 0.437
Population of 100 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    3   100      3.4    0.157     1
Total extinctions: 0
Generation time: 1.359 sec (1.976 average)

 ****** Running generation 4 ******

Population's average fitness: 2.68900 stdev: 1.67128
Best fitness: 12.40000 - size: (2, 4) - species 1 - id 401
Average adjusted fitness: 0.048
Mean genetic distance 1.630, standard deviation 0.440
Population of 100 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    4   100     12.4    0.048     2
Total extinctions: 0
Generation time: 2.900 sec (2.161 average)

 ****** Running generation 5 ******

Population's average fitness: 3.25200 stdev: 4.20556
Best fitness: 32.50000 - size: (2, 4) - species 1 - id 401
Average adjusted fitness: 0.035
Mean genetic distance 1.516, standard deviation 0.450
Population of 100 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    5   100     32.5    0.035     0
Total extinctions: 0
Generation time: 6.527 sec (2.888 average)

 ****** Running generation 6 ******

Population's average fitness: 2.59700 stdev: 1.15364
Best fitness: 8.20000 - size: (1, 2) - species 1 - id 601
Average adjusted fitness: 0.066
Mean genetic distance 1.568, standard deviation 0.659
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    6    98      8.2    0.066     1
     2    0     2       --       --     0
Total extinctions: 0
Generation time: 1.481 sec (2.687 average)

 ****** Running generation 7 ******

Population's average fitness: 2.87100 stdev: 2.12350
Best fitness: 12.90000 - size: (1, 2) - species 1 - id 721
Average adjusted fitness: 0.032
Mean genetic distance 1.763, standard deviation 0.846
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    7    95     12.9    0.064     2
     2    1     5      2.2    0.000     0
Total extinctions: 0
Generation time: 2.782 sec (2.699 average)

 ****** Running generation 8 ******

Population's average fitness: 2.71000 stdev: 2.62913
Best fitness: 28.00000 - size: (1, 2) - species 1 - id 849
Average adjusted fitness: 0.018
Mean genetic distance 1.857, standard deviation 0.645
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    8    60     28.0    0.020     3
     2    2    40      3.2    0.016     0
Total extinctions: 0
Generation time: 4.986 sec (2.953 average)

 ****** Running generation 9 ******

Population's average fitness: 2.52300 stdev: 1.08202
Best fitness: 12.70000 - size: (1, 2) - species 1 - id 849
Average adjusted fitness: 0.030
Mean genetic distance 1.820, standard deviation 0.607
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    9    55     12.7    0.033     4
     2    3    45      3.4    0.027     0
Total extinctions: 0
Generation time: 3.079 sec (2.966 average)

 ****** Running generation 10 ******

Population's average fitness: 2.41000 stdev: 0.35199
Best fitness: 3.40000 - size: (2, 3) - species 2 - id 995
Average adjusted fitness: 0.177
Mean genetic distance 1.863, standard deviation 0.600
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   10    68      3.4    0.153     5
     2    4    32      3.4    0.202     1
Total extinctions: 0
Generation time: 1.305 sec (2.895 average)

 ****** Running generation 11 ******

Population's average fitness: 2.59300 stdev: 1.98858
Best fitness: 22.10000 - size: (1, 3) - species 1 - id 1150
Average adjusted fitness: 0.018
Mean genetic distance 1.912, standard deviation 0.569
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   11    53     22.1    0.024     6
     2    5    47      3.4    0.011     2
Total extinctions: 0
Generation time: 4.639 sec (3.223 average)

 ****** Running generation 12 ******

Population's average fitness: 2.64500 stdev: 2.07487
Best fitness: 22.30000 - size: (1, 3) - species 1 - id 1257
Average adjusted fitness: 0.021
Mean genetic distance 2.000, standard deviation 0.548
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   12    54     22.3    0.034     7
     2    6    46      3.3    0.009     3
Total extinctions: 0
Generation time: 4.695 sec (3.375 average)

 ****** Running generation 13 ******

Population's average fitness: 2.76200 stdev: 2.27894
Best fitness: 22.30000 - size: (1, 3) - species 1 - id 1257
Average adjusted fitness: 0.027
Mean genetic distance 1.818, standard deviation 0.655
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   13    64     22.3    0.043     8
     2    7    36      3.4    0.010     4
Total extinctions: 0
Generation time: 4.711 sec (3.711 average)

 ****** Running generation 14 ******

Population's average fitness: 3.23200 stdev: 3.23740
Best fitness: 22.90000 - size: (1, 2) - species 1 - id 1402
Average adjusted fitness: 0.041
Mean genetic distance 1.918, standard deviation 0.724
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   14    79     22.9    0.073     9
     2    8    21      3.3    0.010     5
Total extinctions: 0
Generation time: 4.600 sec (3.880 average)

 ****** Running generation 15 ******

Population's average fitness: 2.82900 stdev: 1.83713
Best fitness: 12.70000 - size: (1, 2) - species 1 - id 1402
Average adjusted fitness: 0.045
Mean genetic distance 1.874, standard deviation 0.654
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   15    85     12.7    0.071    10
     2    9    15      3.3    0.019     6
Total extinctions: 0
Generation time: 3.044 sec (3.532 average)

 ****** Running generation 16 ******

Population's average fitness: 2.95700 stdev: 2.97682
Best fitness: 22.70000 - size: (1, 2) - species 1 - id 1584
Average adjusted fitness: 0.025
Mean genetic distance 1.785, standard deviation 0.567
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   16    53     22.7    0.042    11
     2   10    47      3.2    0.007     7
Total extinctions: 0
Generation time: 4.838 sec (3.868 average)

 ****** Running generation 17 ******

Population's average fitness: 3.14700 stdev: 3.67602
Best fitness: 32.80000 - size: (4, 4) - species 1 - id 1704
Average adjusted fitness: 0.031
Mean genetic distance 1.833, standard deviation 0.337
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   17    32     32.8    0.032     0
     2   11    68     18.1    0.030     0
Total extinctions: 0
Generation time: 6.214 sec (4.211 average)

 ****** Running generation 18 ******

Population's average fitness: 2.48000 stdev: 0.37815
Best fitness: 3.40000 - size: (4, 5) - species 2 - id 1773
Average adjusted fitness: 0.241
Mean genetic distance 1.753, standard deviation 0.440
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   18    20      3.4    0.263     1
     2   12    80      3.4    0.219     1
Total extinctions: 0
Generation time: 1.314 sec (3.844 average)

 ****** Running generation 19 ******

Population's average fitness: 2.64900 stdev: 1.21684
Best fitness: 12.50000 - size: (4, 5) - species 2 - id 1863
Average adjusted fitness: 0.032
Mean genetic distance 1.854, standard deviation 0.373
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   19    23      3.3    0.012     2
     2   13    77     12.5    0.052     2
Total extinctions: 0
Generation time: 2.634 sec (3.799 average)

 ****** Running generation 20 ******

Population's average fitness: 3.31400 stdev: 2.65436
Best fitness: 12.40000 - size: (4, 3) - species 1 - id 2031
Average adjusted fitness: 0.146
Mean genetic distance 1.918, standard deviation 0.248
Population of 100 members in 2 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   20    69     12.4    0.214     3
     2   14    31     12.2    0.078     3
Total extinctions: 0
Generation time: 2.992 sec (3.968 average)

 ****** Running generation 21 ******

Population's average fitness: 3.09500 stdev: 2.45749
Best fitness: 20.90000 - size: (3, 4) - species 2 - id 2105
Average adjusted fitness: 0.050
Mean genetic distance 2.033, standard deviation 0.476
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   21    76     12.9    0.044     4
     2   15    11     20.9    0.056     0
     3    0    13       --       --     0
Total extinctions: 0
Generation time: 3.823 sec (3.886 average)

 ****** Running generation 22 ******

Population's average fitness: 2.83800 stdev: 1.76922
Best fitness: 12.10000 - size: (3, 4) - species 1 - id 2204
Average adjusted fitness: 0.044
Mean genetic distance 2.136, standard deviation 0.560
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   22    20     12.1    0.076     5
     2   16    35      3.3    0.034     1
     3    1    45      3.3    0.020     0
Total extinctions: 0
Generation time: 2.889 sec (3.706 average)

 ****** Running generation 23 ******

Population's average fitness: 2.81500 stdev: 1.80939
Best fitness: 12.20000 - size: (3, 4) - species 3 - id 2315
Average adjusted fitness: 0.058
Mean genetic distance 1.979, standard deviation 0.478
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   23     6      8.2    0.054     6
     2   17    21      8.5    0.031     2
     3    2    73     12.2    0.088     0
Total extinctions: 0
Generation time: 2.862 sec (3.521 average)

 ****** Running generation 24 ******

Population's average fitness: 3.12500 stdev: 2.59755
Best fitness: 18.40000 - size: (5, 7) - species 3 - id 2355
Average adjusted fitness: 0.037
Mean genetic distance 1.952, standard deviation 0.502
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   24    24      3.3    0.025     7
     2   18    14      3.3    0.014     3
     3    3    62     18.4    0.072     0
Total extinctions: 0
Generation time: 3.331 sec (3.394 average)

 ****** Running generation 25 ******

Population's average fitness: 3.21100 stdev: 2.50667
Best fitness: 18.20000 - size: (5, 8) - species 3 - id 2443
Average adjusted fitness: 0.059
Mean genetic distance 1.996, standard deviation 0.513
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   25    19     12.2    0.058     8
     2   19    30     12.1    0.052     4
     3    4    51     18.2    0.068     1
Total extinctions: 0
Generation time: 3.255 sec (3.415 average)

 ****** Running generation 26 ******

Population's average fitness: 3.70800 stdev: 3.25216
Best fitness: 18.40000 - size: (4, 7) - species 2 - id 2461
Average adjusted fitness: 0.080
Mean genetic distance 2.035, standard deviation 0.454
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   26    47     11.6    0.040     9
     2   20    15     18.4    0.082     5
     3    5    38     12.7    0.119     2
Total extinctions: 0
Generation time: 3.291 sec (3.260 average)

 ****** Running generation 27 ******

Population's average fitness: 5.10800 stdev: 6.62668
Best fitness: 42.20000 - size: (6, 11) - species 3 - id 2660
Average adjusted fitness: 0.065
Mean genetic distance 2.035, standard deviation 0.442
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   27    37     18.1    0.046    10
     2   21    22     12.1    0.024     6
     3    6    41     42.2    0.125     0
Total extinctions: 0
Generation time: 8.163 sec (3.455 average)

 ****** Running generation 28 ******

Population's average fitness: 4.67700 stdev: 6.73436
Best fitness: 57.80000 - size: (6, 11) - species 1 - id 2773
Average adjusted fitness: 0.043
Mean genetic distance 2.066, standard deviation 0.386
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   28    46     57.8    0.056     0
     2   22    18     12.6    0.031     7
     3    7    36     18.1    0.042     1
Total extinctions: 0
Generation time: 10.176 sec (4.342 average)

 ****** Running generation 29 ******

Population's average fitness: 5.91500 stdev: 5.64584
Best fitness: 22.00000 - size: (6, 12) - species 3 - id 2858
Average adjusted fitness: 0.164
Mean genetic distance 2.156, standard deviation 0.424
Population of 99 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   29    36     21.2    0.225     1
     2   23    20     17.9    0.066     8
     3    8    43     22.0    0.201     2
Total extinctions: 0
Generation time: 4.552 sec (4.533 average)

 ****** Running generation 30 ******

Population's average fitness: 4.13232 stdev: 5.66169
Best fitness: 42.40000 - size: (6, 11) - species 3 - id 2773
Average adjusted fitness: 0.041
Mean genetic distance 2.281, standard deviation 0.408
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   30    25     22.4    0.039     2
     2   24     3      8.5    0.011     9
     3    9    72     42.4    0.073     0
Total extinctions: 0
Generation time: 8.303 sec (5.064 average)

 ****** Running generation 31 ******

Population's average fitness: 2.71800 stdev: 2.32019
Best fitness: 22.50000 - size: (6, 11) - species 3 - id 2773
Average adjusted fitness: 0.018
Mean genetic distance 2.369, standard deviation 0.404
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   31    36      8.4    0.022     3
     2   25     6      2.4    0.005    10
     3   10    58     22.5    0.027     1
Total extinctions: 0
Generation time: 4.770 sec (5.159 average)

 ****** Running generation 32 ******

Population's average fitness: 5.75000 stdev: 12.30191
Best fitness: 97.10000 - size: (6, 11) - species 3 - id 2773
Average adjusted fitness: 0.027
Mean genetic distance 2.328, standard deviation 0.370
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   32     7     22.1    0.019     4
     2   26     3      8.1    0.011    11
     3   11    90     97.1    0.052     0
Total extinctions: 0
Generation time: 16.923 sec (6.563 average)

 ****** Running generation 33 ******

Population's average fitness: 4.30000 stdev: 5.34032
Best fitness: 22.60000 - size: (7, 11) - species 3 - id 3256
Average adjusted fitness: 0.088
Mean genetic distance 2.393, standard deviation 0.504
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   33    80     22.2    0.146     5
     2   27    14      3.1    0.016    12
     3   12     6     22.6    0.102     1
Total extinctions: 0
Generation time: 4.822 sec (6.759 average)

 ****** Running generation 34 ******

Population's average fitness: 3.82100 stdev: 8.54353
Best fitness: 81.60000 - size: (6, 11) - species 1 - id 2773
Average adjusted fitness: 0.012
Mean genetic distance 2.261, standard deviation 0.528
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   34    49     81.6    0.024     0
     2   28    42      8.4    0.009    13
     3   13     9      3.3    0.004     2
Total extinctions: 0
Generation time: 14.971 sec (7.923 average)

 ****** Running generation 35 ******

Population's average fitness: 4.31200 stdev: 6.12000
Best fitness: 48.20000 - size: (6, 11) - species 1 - id 2773
Average adjusted fitness: 0.035
Mean genetic distance 2.091, standard deviation 0.543
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   35    57     48.2    0.066     1
     2   29    17     18.3    0.031    14
     3   14    26      3.3    0.007     3
Total extinctions: 0
Generation time: 8.526 sec (8.450 average)

 ****** Running generation 36 ******

Population's average fitness: 4.62100 stdev: 6.69530
Best fitness: 40.70000 - size: (7, 15) - species 1 - id 3526
Average adjusted fitness: 0.056
Mean genetic distance 2.218, standard deviation 0.405
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   36    49     40.7    0.075     2
     2   30    31     22.0    0.042     0
     3   15    20     27.9    0.050     4
Total extinctions: 0
Generation time: 7.226 sec (8.843 average)

 ****** Running generation 37 ******

Population's average fitness: 3.96600 stdev: 3.01742
Best fitness: 12.10000 - size: (7, 14) - species 1 - id 3590
Average adjusted fitness: 0.170
Mean genetic distance 2.323, standard deviation 0.515
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   37    42     12.1    0.198     3
     2   31    18     11.3    0.175     1
     3   16    40     11.2    0.136     5
Total extinctions: 0
Generation time: 2.859 sec (8.313 average)

 ****** Running generation 38 ******

Population's average fitness: 4.04700 stdev: 6.58860
Best fitness: 42.40000 - size: (3, 7) - species 3 - id 3641
Average adjusted fitness: 0.041
Mean genetic distance 2.322, standard deviation 0.632
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   38    57     42.0    0.068     4
     2   32    11      8.3    0.020     2
     3   17    32     42.4    0.035     6
Total extinctions: 0
Generation time: 8.092 sec (8.104 average)

 ****** Running generation 39 ******

Population's average fitness: 6.05500 stdev: 8.87696
Best fitness: 37.70000 - size: (8, 14) - species 1 - id 3728
Average adjusted fitness: 0.090
Mean genetic distance 2.345, standard deviation 0.600
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   39    38     37.7    0.124     5
     2   33    28     12.5    0.044     3
     3   18    34     32.5    0.104     7
Total extinctions: 0
Generation time: 6.593 sec (8.309 average)

 ****** Running generation 40 ******

Population's average fitness: 5.44800 stdev: 5.55562
Best fitness: 28.20000 - size: (7, 13) - species 1 - id 3830
Average adjusted fitness: 0.126
Mean genetic distance 2.364, standard deviation 0.568
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   40    67     28.2    0.136     6
     2   34    10     28.0    0.147     0
     3   19    23     12.4    0.095     8
Total extinctions: 0
Generation time: 5.005 sec (7.979 average)

 ****** Running generation 41 ******

Population's average fitness: 6.41200 stdev: 7.05748
Best fitness: 28.10000 - size: (8, 15) - species 1 - id 3971
Average adjusted fitness: 0.144
Mean genetic distance 2.351, standard deviation 0.550
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   41    40     28.1    0.181     7
     2   35    15     27.8    0.124     1
     3   20    45     27.8    0.127     9
Total extinctions: 0
Generation time: 4.933 sec (7.995 average)

 ****** Running generation 42 ******

Population's average fitness: 6.03900 stdev: 9.37855
Best fitness: 52.00000 - size: (8, 14) - species 3 - id 4084
Average adjusted fitness: 0.064
Mean genetic distance 2.409, standard deviation 0.497
Population of 101 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   42    82     51.9    0.089     8
     2   36     9     12.3    0.016     2
     3   21    10     52.0    0.087    10
Total extinctions: 0
Generation time: 9.809 sec (7.284 average)

 ****** Running generation 43 ******

Population's average fitness: 9.56634 stdev: 13.20599
Best fitness: 47.70000 - size: (7, 12) - species 1 - id 4131
Average adjusted fitness: 0.182
Mean genetic distance 2.240, standard deviation 0.606
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   43    54     47.7    0.155     9
     2   37    35     37.9    0.309     0
     3   22    11     37.7    0.082    11
Total extinctions: 0
Generation time: 8.269 sec (7.628 average)

 ****** Running generation 44 ******

Population's average fitness: 6.41000 stdev: 10.08566
Best fitness: 42.20000 - size: (7, 11) - species 2 - id 4221
Average adjusted fitness: 0.090
Mean genetic distance 2.364, standard deviation 0.631
Population of 101 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   44    43     42.1    0.097    10
     2   38    42     42.2    0.142     0
     3   23    16      8.2    0.031    12
Total extinctions: 0
Generation time: 8.167 sec (6.948 average)

 ****** Running generation 45 ******

Population's average fitness: 5.23960 stdev: 6.40605
Best fitness: 42.40000 - size: (7, 12) - species 2 - id 4371
Average adjusted fitness: 0.074
Mean genetic distance 2.226, standard deviation 0.539
Population of 101 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   45    38     18.3    0.072    11
     2   39    40     42.4    0.083     0
     3   24    23     12.2    0.066    13
Total extinctions: 0
Generation time: 8.220 sec (6.917 average)

 ****** Running generation 46 ******

Population's average fitness: 7.94653 stdev: 10.95017
Best fitness: 38.20000 - size: (7, 12) - species 2 - id 4371
Average adjusted fitness: 0.165
Mean genetic distance 2.169, standard deviation 0.563
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   46    28     37.9    0.154    12
     2   40    27     38.2    0.143     1
     3   25    45     32.5    0.197    14
Total extinctions: 0
Generation time: 6.691 sec (6.864 average)

 ****** Running generation 47 ******

Population's average fitness: 8.29400 stdev: 12.63673
Best fitness: 62.10000 - size: (7, 12) - species 2 - id 4371
Average adjusted fitness: 0.111
Mean genetic distance 2.123, standard deviation 0.599
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   47    23     38.3    0.071    13
     2   41    44     62.1    0.198     0
     3   26    33     32.2    0.063    15
Total extinctions: 0
Generation time: 11.200 sec (7.698 average)

 ****** Running generation 48 ******

Population's average fitness: 5.82000 stdev: 8.97362
Best fitness: 82.00000 - size: (6, 6) - species 2 - id 4644
Average adjusted fitness: 0.047
Mean genetic distance 2.175, standard deviation 0.492
Population of 100 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   48    32     18.2    0.051    14
     2   42    38     82.0    0.039     0
     3   27    30     18.0    0.050    16
Total extinctions: 0
Generation time: 15.078 sec (8.397 average)

 ****** Running generation 49 ******

Population's average fitness: 5.81500 stdev: 8.05638
Best fitness: 32.50000 - size: (11, 20) - species 1 - id 4713
Average adjusted fitness: 0.120
Mean genetic distance 2.164, standard deviation 0.539
Population of 101 members in 3 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1   49    42     32.5    0.184    15
     2   43    37     32.4    0.098     1
     3   28    22     28.1    0.078    17
Total extinctions: 0
Generation time: 6.473 sec (8.385 average)

Best genome:
Key: 4713
Fitness: 32.50000000000012
Nodes:
	0 DefaultNodeGene(key=0, bias=-0.48530113864852853, response=1.0, activation=tanh, aggregation=sum)
	144 DefaultNodeGene(key=144, bias=-1.2074706448186414, response=1.0, activation=tanh, aggregation=sum)
	161 DefaultNodeGene(key=161, bias=0.2475373906602863, response=1.0, activation=tanh, aggregation=sum)
	418 DefaultNodeGene(key=418, bias=0.3657350975666344, response=1.0, activation=tanh, aggregation=sum)
	492 DefaultNodeGene(key=492, bias=-2.28569679245945, response=1.0, activation=tanh, aggregation=sum)
	574 DefaultNodeGene(key=574, bias=-2.3147620392938375, response=1.0, activation=tanh, aggregation=sum)
	657 DefaultNodeGene(key=657, bias=2.4985249093872164, response=1.0, activation=tanh, aggregation=sum)
	705 DefaultNodeGene(key=705, bias=0.9574337637221569, response=1.0, activation=tanh, aggregation=sum)
	766 DefaultNodeGene(key=766, bias=-0.2229499673978434, response=1.0, activation=tanh, aggregation=sum)
	781 DefaultNodeGene(key=781, bias=-0.438499658052231, response=1.0, activation=tanh, aggregation=sum)
	866 DefaultNodeGene(key=866, bias=0.4769264242421102, response=1.0, activation=tanh, aggregation=sum)
Connections:
	DefaultConnectionGene(key=(-3, 0), weight=-2.5342099631713877, enabled=True)
	DefaultConnectionGene(key=(-3, 161), weight=-0.012252099912192782, enabled=True)
	DefaultConnectionGene(key=(-3, 657), weight=0.21523065438476147, enabled=False)
	DefaultConnectionGene(key=(-3, 866), weight=1.0306262462512827, enabled=True)
	DefaultConnectionGene(key=(-2, 0), weight=7.1254364521308124, enabled=True)
	DefaultConnectionGene(key=(-2, 144), weight=-2.909193119800828, enabled=False)
	DefaultConnectionGene(key=(-2, 161), weight=1.9648522374952666, enabled=True)
	DefaultConnectionGene(key=(-2, 492), weight=0.059176566479174936, enabled=True)
	DefaultConnectionGene(key=(-2, 705), weight=0.5279874533855575, enabled=True)
	DefaultConnectionGene(key=(-2, 766), weight=-0.06531158517475702, enabled=True)
	DefaultConnectionGene(key=(-1, 0), weight=2.8530575667757074, enabled=True)
	DefaultConnectionGene(key=(-1, 574), weight=1.3243499510356513, enabled=True)
	DefaultConnectionGene(key=(0, 144), weight=0.9377700412660643, enabled=False)
	DefaultConnectionGene(key=(161, 657), weight=2.193264624281889, enabled=True)
	DefaultConnectionGene(key=(418, 161), weight=0.41526550114163074, enabled=True)
	DefaultConnectionGene(key=(492, 144), weight=0.31246327653943307, enabled=True)
	DefaultConnectionGene(key=(574, 0), weight=0.037346446757148495, enabled=True)
	DefaultConnectionGene(key=(574, 418), weight=-1.9579545366869517, enabled=False)
	DefaultConnectionGene(key=(574, 781), weight=0.3254645807067176, enabled=True)
	DefaultConnectionGene(key=(657, 492), weight=0.6347570657037086, enabled=True)
	DefaultConnectionGene(key=(766, 418), weight=-1.6130264017106075, enabled=True)
	DefaultConnectionGene(key=(781, 418), weight=1.0178035525722726, enabled=True)
	DefaultConnectionGene(key=(781, 705), weight=1.8959792704647649, enabled=True)
	DefaultConnectionGene(key=(866, 657), weight=-0.4096714920717623, enabled=True)
```
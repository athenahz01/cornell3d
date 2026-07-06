# Campus layout, source of truth

World axes: +x east, -x west (slope, Cayuga), +z south, -z north (Fall Creek). 1 unit is roughly 2.5 m.
Overall compression: the real campus is squeezed about 3:1, so street blocks are shorter and some
real adjacencies are represented by direction rather than distance.

## Streets
| Street | World line | Note |
|---|---|---|
| Tower Road | z 24, x 10..200 | main east-west axis |
| East Avenue | x 81, z -56..118 | real one curves; ours is straight |
| Campus Road | z 121 with a north jog around Phillips (x 30..58) | jog is a compression artifact |
| Central Avenue | x -42 (z 44..84) bending southwest to the Cascadilla bridge at x -24 | Ho Plaza is its closed pedestrian stretch |

## Buildings
| Building | Extents (x0,z0,x1,z1) | Anchor | Deviation note |
|---|---|---|---|
| McGraw Tower | -57,-11,-47,-1 | Arts Quad SW | attached to Uris by link wing |
| Uris Library | -77,18,-35,42 | Arts Quad S edge | west apse bay faces the slope |
| Olin Library | -28,44,-6,58 | head of Ho Plaza, east flank | real one sits square to the plaza axis |
| Willard Straight | -74,48,-48,72 | Ho Plaza west | correct |
| Cornell Store | -40,74,-30,84 | Ho Plaza west, below the Straight | correct |
| Sage Chapel | -22,60,-6,88 | Ho Plaza east | entry faces west to the plaza |
| Barnes Hall | -10,92,4,106 | Ho Plaza east, south of the chapel | correct relationship |
| Anabel Taylor | -34,92,-12,116 | law precinct east | correct |
| Myron Taylor | -74,88,-40,120 | Central Ave / law precinct | north face treated as the Central Ave front |
| Sage Hall | 27,46,45,78 | East Avenue | Johnson School, on the chapel's old site |
| Goldwin Smith | 50,-22,76,4 | Arts Quad east, portico west | correct |
| Uris Hall | 56,3,70,21 | Tower Rd south | correct |
| Day Hall | 84,4,100,20 | East Ave x Tower Rd NE corner, door west | real one is SE of the junction; Barton owns that corner here |
| Rockefeller | 84,-16,102,2 | East Ave | correct |
| Barton Hall | 84,28,118,64 | East Ave x Tower Rd SE | enterable drill hall |
| Statler | 54,44,78,72 | East Ave | real one anchors East x Campus; our Campus Rd is far south (compression) |
| Bailey Hall | 108,2,128,22 | Tower Rd north, portico south | correct relationship |
| Old Stone Row | -74,-46..10,-60 | Arts Quad west, doors east | three blocks, McGraw Hall keeps its west tower |
| Sibley | -28,-68,28,-50 | Arts Quad north | dome centered |
| Tjaden / Lincoln | -46..-32 / 30..48, -64..-46 | quad NW / NE | correct |
| Stimson | 40,7,54,21 | Tower Rd north | nudged north for the road |
| Johnson Museum | -76,-68,-58,-50 | slope crest NW | correct |
| Risley | -16,-95,32,-73 | north of the quad | correct |
| Suspension Bridge | x -4, z -104..-142 | Fall Creek crossing | correct |
| Beebe Lake | 22,-146,112,-116 | behind the dam | correct |
| Klarman | 76,-16,80,-2 | behind Goldwin | correct |
| Engineering Quad | 2..62, 120..174 | south of Campus Rd | Duffield atrium faces the green |
| Gates Hall | 60,92,82,116 | north of Campus Rd | moved north of the road (real one is south) |
| Cascadilla Gorge | z 186..212 | south boundary | stair at x -5, bridge at x -24 |
| Schoellkopf | 60,214,110,252 | across Cascadilla | skyline only, not walkable |
| Big Red Barn | 68,-56,80,-42 | graduate quarter | correct |
| A.D. White House | 50,-56,64,-40 | east of the quad | correct |
| Mann / Bradfield | 148,42,172,68 | Ag Quad stub | facade only |

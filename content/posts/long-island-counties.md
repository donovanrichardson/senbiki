+++
date = '2025-11-01T15:31:31-04:00'
draft = true
title = "Redrawing the Boundaries of Long Island's Counties"
+++

Long Island has four counties: Kings, Queens, Nassau, and Suffolk. I am always thinking of whether the lines between these counties make sense. Some of them seem anachronistic -- for example, the border between Nassau and Queens cuts some houses in half. The border between the towns of Huntington and Smithtown in Suffolk County, according to legend, was determined by how far someone could ride on horseback with just bread and cheese to eat. And the border between Nassau and Suffolk is mostly just a straight line through an area that is much more densely populated now than it was in the late 17th century when the border was drawn. Recently I decided that maybe I can redraw these lines with my computer and some census data.

My steps to do this included:

- Collecting census tract geography and population data for the four counties of Long Island
- Converting census tracts into centroid points and creating an _Urquhart graph_ using the centroids of these tracts, ensuring that small island tracts are connected to the rest of the graph by at least one edge while eliminating most long edges that cross water or are not useful to the algorithm.
- Assigning the edge weights of the Urquhart graph using the formula described below
- Creating an all-nodes distance matrix and input this into a K-Medoids clustering algorithm to split the tracts into four clusters

### Edge Weight/Cost calculation formula

| Cost calculation                                                | Assumption that this calculation reflects.                                                                                                                                                                      |                                                                                                                                            |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| dist or dist/2 + dist/2                                         | the cost of traveling from tract A to B, and therefore their disconnectedness, is proportional to the distance needed to get there                                                                              | used haversine formula to calculate greate circle distance                                                                                 |
| dist/2 (sqrt(pop_a)) + dist/2 (sqrt(pop_b))                     | the average distance between people on a path from A to B is proportionate to sqrt(population) for equal area places (interpolating the disconnectedness between tract A and tract B based on tract population) | pop_a is the population of census tract A and pop_b is the population of census tract B, when these tracts are considered to be neighbors. |
| (dist/2 (sqrt(pop_a)) + dist/2 (sqrt(pop_b)))^2                 | the frequency of going between tract A and tract B is inversely related to the resources spent getting there. the above disconnectedness measure is squared.                                                    |                                                                                                                                            |
| ((dist/2 (sqrt(pop_a)) + dist/2 (sqrt(pop_b)))^2)/(pop_a/pop_b) | the frequency of connections between tract A and B is related to the combined population of the tracts, i.e. the disconnectedness is inversely related to population.                                           |                                                                                                                                            |
|                                                                 |                                                                                                                                                                                                                 |                                                                                                                                            |

Thus the final cost calculation is `((dist/2 (sqrt(pop_a)) + dist/2 (sqrt(pop_b)))^2)/(pop_a/pop_b)`

The intention in creating such a cost calculation is to induce the k-medioids algorithm to cluster locations together when they are likely to have a higher amount of traffic between them. The borders between two clusters should then in theory be areas of lower population or more separation between populations.

## K medioids result

The K-medioids is useful as a sort of voronoi algorithm for graphs. It iteratively selects "medioids" (central nodes) and assigns other nodes to the cluster of the nearest medioid based on the distance matrix provided. Then whichever node in this cluster has the shortest cumulative weight to every other edge in the cluster becomes the new medioid for the next iteration. This continues until convergence or until a set number of iterations is reached.

After running the K-Medioids algorithm with k=4, I obtained the following clusters for the census tracts of Long Island:

![Four "new" counties for Long Island. Base Map is Esri Topographical map](medioids-result.png)

By design, the K-medioids algorithm will give a medioid: a centrally located node that for the purposes of this algorithm can be thought of as the "county seat" of each of these new counties.

Here are the populations and seats of these "New Counties" as of the 2020 Census, from west to east:

| New County                      | New County Seat                     | Population |
|---------------------------------|-------------------------------------|------------|
| New Brooklyn (New Kings County) | Prospect-Leffert Gardens / Flatbush | 2,963,981  |
| New Queens                      | Kew Gardens Hills                   | 2,607,754  |
| New Nassau                      | Levittown                           | 1,506,479  |
| New Suffolk                     | Farmingville                        | 985,018    |

![We can see here that the "new" counties are all moved eastward such that "new" Suffolk is significantly smaller than the real Suffolk County.](moved-eastward.png)
We can see here that the "new" counties are all moved eastward such that "new" Suffolk is significantly smaller than the real Suffolk County.

This was mostly just a fun project for me, but similar principles and algorithms can be used for applications like redistricting or subdividing organizations and clubs geographically.

Will make Git repo available soon!
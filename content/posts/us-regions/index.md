In my last post I demonstrated an algorithm that splits areas of the United States into subregions based on US Census population and boundary data. 
A main feature of that is using k-medoids to cluster adjacent census geographies, where adjacency was determined by a delaunay triangulation of polygon centroids rather than by physical adjacency.
Additionally, edge weights for the k-medoid calculation were re-weighted so that edge weights increased proportionally with real-world distance, but decrease quadratically as the populations of the linked nodes increase.
This weighting is designed to capture the real world effect of lower distance increasing the likelihood of connection.
Though the previous post focused on the counties of Long Island, this one will focus on actually separating the whole US into regions.

I used approximately the same algo as Long Island, where the differences were errors I found in the impl, or things I wanted to enhance my intention and impl.
I used counties to break up the US.
Some I broke up further because I thought they were too big.
I had actually used the results of this algo to break the regions into subregions using census tract as the target geography, and when census tracts in these regions were too many, the algo took too long to run so I decided in these cases to split further.

In all I created 42 regions of the US based on my algorithm.

- "Boston and Providence"
- "New York and Philadelphia"
- Washington and Baltimore
- South Delmarva
- Richmond and Norfolk
- Raleigh and Charlotte
- Charleston and Augusta
- Jacksonville and Miami
- New Orleans and Mobile
- Atlanta and Birmingham
- Charlottesville and Lynchburg
- Indianapolis and Cleveland
- Pittsburgh and Altoona
- Scranton and Williamsport
- Buffalo and Syracuse
- Chicago and Detroit
- Minneapolis and Eau Claire
- Peoria and Champaign
- Louisville and Nashville
- Memphis and Jonesboro
- Alexandria and Hattiesburg
- Little Rock and Shreveport
- Lake Ozark and Mountain Home
- Kansas City and Topeka
- Des Moines and Cedar Rapids
- Omaha and Sioux Falls
- Wichita and Salina


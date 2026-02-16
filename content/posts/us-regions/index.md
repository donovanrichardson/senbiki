In my last post I demonstrated an algorithm that splits areas of the United States into subregions based on US Census population and boundary data. 
A main feature of that is using k-medoids to cluster adjacent census geographies, where adjacency was determined by a delaunay triangulation of polygon centroids rather than by physical adjacency.
Additionally, edge weights for the k-medoid calculation were re-weighted so that edge weights increased proportionally with real-world distance, but decrease quadratically as the populations of the linked nodes increase.
This weighting is designed to capture the real world effect of lower distance increasing the likelihood of connection.
Though the previous post focused on the counties of Long Island, this one will focus on actually separating the whole US into regions.

I used approximately the same algo as Long Island, where the differences were errors I found in the impl, or things I wanted to enhance my intention and impl.
I used counties to break up the US.
Some I broke up further because I thought they were too big.
I had actually used the results of this algo to break the regions into subregions using census tract as the target geography, and when census tracts in these regions were too many, the algo took too long to run so I decided in these cases to split further.

![img.png](img.png)

In all I created 42 regions of the US based on my algorithm. They were clustered together based on centroids representing individual counties or county-equivalents. Below I am grouping them roughly by their incorporation of their territories into the The United States or their thirteen predecessor colonies; I've tried to name the regions based on the two major cities within their limits. In future posts I plan to go through these 42 clustered regions in order.

- Thirteen Colonies
  - Boston MA and Providence RI
  - New York NY and Philadelphia PA
  - Scranton PA and Williamsport PA
  - Washington DC and Baltimore MD
  - Sussex County DE and St. Mary's County MD
  - Charlottesville and Lynchburg, VA
  - Richmond and Norfolk, VA
  - Raleigh and Charlotte, NC
  - Charleston SC and Augusta GA
  - Atlanta GA and Birmingham AL
- Old West
  - Buffalo and Syracuse NY
  - Pittsburgh PA and Altoona PA
  - Louisville KY and Nashville TN
  - Memphis TN and Jonesboro AR
  - Indianapolis IN and Cleveland OH
  - Peoria IL and Champaign IL
  - Chicago IL and Detroit MI
- Louisiana Purchase and Florida
  - Alexandria LA and Hattiesburg MS
  - New Orleans LA and Mobile AL
  - Hannibal MO and Saint Louis MO
  - Lake Ozark MO and Mountain Home AR
  - Little Rock AR and Shreveport LA
  - Jacksonville and Miami FL
  - Des Moines IA and Cedar Rapids IA
  - Minneapolis MN and Eau Claire WI
  - Kansas City MO and Topeka KS
  - Garden City and Dodge City KS
  - Wichita and Salina KS
  - Denver and Grand Junction CO
  - Omaha NE and Sioux Falls SD
  - Bismarck ND and Williston ND
  - Tulsa OK and Springfield MO
  - Oklahoma City OK and Wichita Falls TX
- Texas
  - Dallas and Houston TX
  - Albuquerque NM and El Paso TX
- Oregon Country
  - Portland and Salem OR
  - Seattle and Spokane WA
- Mexican Cession
  - Sacramento and San Jose CA
  - Medford OR and Eureka CA
  - Reno and Carson City NV
  - Salt Lake City UT and Missoula MT
  - Los Angeles CA and Phoenix AZ


---
title: "US Regions"
date: 2026-02-16T20:01:11-05:00
params:
  author: "Donovan Richardson"
---

In my last post I demonstrated an algorithm that splits areas of the United States (lower 48) into subregions based on US Census population and boundary data. 
A main feature of that is using k-medoids to cluster adjacent census geographies, where adjacency was determined by a Delaunay triangulation of polygon centroids rather than by physical adjacency.
Additionally, edge weights for the k-medoid calculation were re-weighted so that edge weights increased proportionally with real-world distance, but decreased quadratically as the populations of the linked nodes increase.
This weighting is designed to capture the real-world effect of lower distance increasing the likelihood of real-world connections.
Though the previous post focused on the counties of Long Island, this one will focus on actually separating the whole US into regions.

I used approximately the same algorithm as I had used in my previous Long Island post, but I did tweak the algorithm a bit after rethinking some assumptions I had made before.
The inputs of this run of my algorithm were individual counties or county-equivalents of the lower 48 states.
Additionally, I broke up a few regions at my own discretion because I thought they were too large: all of California except the very northern part had previously been in one region together with Phoenix, AZ. Most of Florida had also been included with most of South Carolina and all of Coastal Georgia. I decided to further break up those regions into two each, which are included in the map of all regions below.

{{< figure
src="regions-map.png"
alt="42 generated regions of the United States"
caption="42 generated regions of the United States based on k-medoids clustering algorithm. Baselayer data (c) OpenStreetMap contributors, Microsoft, Facebook, Google, Esri Community Maps contributors, Map layer by Esri"
>}}

In all I created 42 regions of the US based on my algorithm. Below I am grouping them roughly by their incorporation of their territories into the The United States or their thirteen predecessor colonies; I've tried to name the regions based on the two major cities within their limits. In future posts I plan to go through these 42 clustered regions in order.

| Thirteen Colonies                         | Old West | Louisiana Purchase and Florida | Texas | Oregon Country | Mexican Cession |
|-------------------------------------------|----------|--------------------------------|-------|----------------|-----------------|
| Boston MA and Hartford CT                 | Buffalo and Syracuse NY | Alexandria LA and Hattiesburg MS | Dallas and Houston TX | Portland and Salem OR | Sacramento and San Jose CA |
| New York NY and Philadelphia PA           | Pittsburgh PA and Altoona PA | New Orleans LA and Mobile AL | Albuquerque NM and El Paso TX | Seattle and Spokane WA | Medford OR and Eureka CA |
| Scranton PA and Williamsport PA           | Louisville KY and Nashville TN | Hannibal MO and Saint Louis MO | | | Reno and Carson City NV |
| Washington DC and Baltimore MD            | Memphis TN and Jonesboro AR | Lake Ozark MO and Mountain Home AR | | | Salt Lake City UT and Missoula MT |
| Sussex County DE and St. Mary's County MD | Indianapolis IN and Cleveland OH | Little Rock AR and Shreveport LA | | | Los Angeles CA and Phoenix AZ |
| Charlottesville and Lynchburg, VA         | Peoria IL and Champaign IL | Jacksonville and Miami FL | | | |
| Richmond and Norfolk, VA                  | Chicago IL and Detroit MI | Des Moines IA and Cedar Rapids IA | | | |
| Raleigh and Charlotte, NC                 | | Minneapolis MN and Eau Claire WI | | | |
| Charleston SC and Augusta GA              | | Kansas City MO and Topeka KS | | | |
| Atlanta GA and Birmingham AL              | | Garden City and Dodge City KS | | | |
|                                           | | Wichita and Salina KS | | | |
|                                           | | Denver and Grand Junction CO | | | |
|                                           | | Omaha NE and Sioux Falls SD | | | |
|                                           | | Bismarck ND and Williston ND | | | |
|                                           | | Tulsa OK and Springfield MO | | | |
|                                           | | Oklahoma City OK and Wichita Falls TX | | | |


Moving from graph algorithm to a transportation network

[TITLE: still describes the blog, not the content; a specific, searchable title is open]

WHAT THE READER SHOULD TAKE AWAY
- It is possible to make timetables in this format, and I made one.
- They can use it to find trains that leave their desired station for a desired destination, or from their desired station inbound or outbound.
- This format is a potential and useful format for transit timetables outside Japan.

========================================
INTRO
========================================

I built a departure board for the LIRR in the Japanese timetable format: https://bit.ly/lirrboard

This far I have done graph algorithms, this time I will switch to something related but not algorithm. Transportation network. 

LIRR, one of the commuter rail networks

========================================
BACKGROUND
========================================

--- The Japanese format ---

I have interest in transit network

I've been to Japan

Japanese rail timetables are often presented in jikokuhyou format. 

Include image of Japan timetable: nishi-ooi-weekday.png (JR East, Nishi-Ooi Station, weekday, with both legend rows). Optionally nishi-ooi-saturday-holiday.png (same station, Saturday and holiday, which adds a third legend row ■=時刻変更, schedule change).

Wanted to do this for LIRR

--- The LIRR network ---

Graphs before have been more dense. LIRR is more of a tree structure. 

Four western terminals Penn Atlantic gct and Long Island City. Eastward they branch into 8 major branches [east of Jamaica per Wikipedia's list, excluding the seasonal Belmont Park Branch and counting Babylon and Montauk as one line: Far Rockaway, Hempstead, Long Beach, Babylon/Montauk, Oyster Bay, Port Jefferson, Ronkonkoma, West Hempstead]. The farthest east of these are Port Jefferson in the north shore, the main line which runs through the center of the island but ends at the north fork, at Greenport, and the Montauk terminal. 

It is mostly a tree structure, with a few cycles such as the Central Branch between the Main Line and the Babylon/Montauk line. Almost all trains stop at Jamaica, a through station in Queens. But east of Jamaica, there are 8 major branch lines. 

Include a simple diagram of the LIRR: LIRR_schematic.svg (Wikimedia Commons, File:LIRR_schematic.svg, public domain; schematic as of 2013, current version 2023 by ComplexRational, original by NE2). It shows the terminals at left, Jamaica as the hub, one color per branch, and the Central Branch as the diagonal from the Ronkonkoma line to Babylon. Credit is not required; give it anyway.

--- The problem: destinations ---

One difference between LIRR and many Japanese railroads may be the extensive branching of the LIRR. Trains heading eastward at Mineola may continue to Oyster Bay, Huntington, Port Jefferson, Ronkonkoma, or Patchogue. Similarly, trains westward from Port Jefferson typically terminate at Huntington, but many commuters also take trains that terminate at Jamaica or Penn Station. Because of this it will be necessary when constructing a train timetable to indicate train destinations. 

However many Japanese train timetables do branch, marking each departure with a destination character and printing a legend on the page (for example, JR East's timetable for Nishi-Ooi Station, Shonan-Shinjuku Line toward Yokohama and Ofuna, southbound: the legend row 行き先・経由 reads 無印=逗子 大=大船, and a separate row 列車種別・列車名 reads 無印=普通 快=快速, so each minute can carry a destination mark and a train-type mark)

========================================
BODY: THE BOARD
========================================

How the board does this: each departure is labeled with the destination of its own trip (from the GTFS trip data) as a colored pill next to the minute; a destination picker filters to the trains that stop at a chosen station; hours continue past 23 for trips after midnight.

Include image of mine: board-mineola-outbound.png (Mineola, Outbound, 24h, with destination pills HUN, OBY, PGE, PJN, RON and a 24 row).

Include images of mine, Ronkonkoma Inbound (board-ronkonkoma-inbound-full.png is the whole day; board-ronkonkoma-inbound-top.png is the header with the "Trips toward" filter showing Penn Station labeled "Unlabeled", Atlantic Terminal ATL, and Grand Central GCT; board-ronkonkoma-inbound-scrolled.png is the 01 to 17 rows). Use these to show that only ATL and GCT trips carry a pill and Penn Station trips are unmarked, the same convention as 無印 in the Nishi-Ooi legend.

[GAP: design decisions and what was hard, in the author's words]

--- How it got here ---

Include image of the 2019 Word document (lirrschedule.docx, Port Jefferson Branch weekday, Huntington) as the earlier hand-made version.

first attempt (2019, the Word document: LIRR Port Jefferson Branch weekday service at Huntington, and a weekday S1 bus table Halesite to Amityville) I manually copied from the official MTA timetable of September 2019

then generated from GTFS (2020, 2021), now the board built on OneBusAway

========================================
FINAL WORDS
========================================

Try it at https://bit.ly/lirrboard. Feedback from LIRR commuters welcome.

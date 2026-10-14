# Japanese-Style Timetables for the LIRR

## What the reader should take away

- It is possible to make timetables in this format, and I made one.
- They can use it to find trains that leave their desired station for a desired destination, or from their desired station inbound or outbound.
- This format is a potential and useful format for transit timetables outside Japan.

## Intro

I built a departure board for the LIRR in the Japanese timetable format: <https://bit.ly/lirrboard>

This far I have done graph algorithms, this time I will switch to something related but not algorithm. Transportation network.

LIRR, one of the commuter rail networks

## Background

### The Japanese format

I have interest in transit network

I've been to Japan

Japanese rail timetables are often presented in jikokuhyou format.

Include image of Japan timetable: nishi-ooi-weekday-cropped.png (JR East, Nishi-Ooi Station, weekday, with both legend rows). Optionally nishi-ooi-saturday-holiday-cropped.png (same station, Saturday and holiday, which adds a third legend row ■=時刻変更, schedule change). Caption for that image: "The same station's Saturday and holiday timetable. It adds a third legend row, 変更・注意マーク, where ■=時刻変更 flags a time that has changed; here it marks the 8:30 train." Credit under the image: JR East timetable, Nishi-Ooi Station, timetables.jreast.co.jp. Caption: "JR East's weekday timetable for Nishi-Ooi Station, southbound. A small mark under a minute shows where that train goes or what type it is. The legend at the bottom explains the marks: 無印=逗子 and 大=大船 for destinations, 無印=普通 and 快=快速 for train type."

Wanted to do this for LIRR

### The LIRR network

The neighbor graphs in my earlier posts have many cycles. LIRR is more of a tree structure.

Four western terminals: Penn Station, Atlantic Terminal, Grand Central and Long Island City. Eastward from Jamaica they branch into 8 major branches.[^branches] The branches reach as far as Port Jefferson on the north shore; the main line, which runs through the center of the island, ends at Greenport on the north fork; and the Montauk line ends at Montauk.

It is mostly a tree structure, with a few cycles such as the Central Branch between the Main Line and the Babylon/Montauk line. Almost all trains stop at Jamaica, a through station in Queens; the Port Washington Branch is the exception. But east of Jamaica, there are 8 major branch lines.

Include a simple diagram of the LIRR: LIRR_schematic.svg.[^diagram] It shows the terminals at left, Jamaica as the hub, one color per branch, and the Central Branch as the diagonal from the Ronkonkoma line to Babylon. Caption: "A schematic of the LIRR. Each color is a branch; east of Jamaica they fan out toward the east end of the island. The diagonal from Hicksville to Babylon is the Central Branch."

### The problem: destinations

One difference between LIRR and many Japanese railroads is the extensive branching of the LIRR. Trains heading eastward at Jamaica may continue to 16 destinations on 9 branches (board-jamaica-outbound.png). Similarly, trains westward from Port Jefferson often terminate at Huntington, but many commuters also take trains that terminate at Jamaica or Penn Station. Because of this it will be necessary when constructing a train timetable to indicate train destinations.

However many Japanese train timetables also carry trains with different destinations, marking each departure with a destination character and printing a legend on the page. For example:

- JR East, Nishi-Ooi Station, Shonan-Shinjuku Line toward Yokohama and Ofuna, southbound: the legend row 行き先・経由 reads 無印=逗子 大=大船, and a separate row 列車種別・列車名 reads 無印=普通 快=快速, so each minute can carry a destination mark and a train-type mark.
- JR East, Tachikawa Station, Chuo Line Rapid toward Tokyo and Shinjuku, weekday: 無印=東京 新=新宿 三=三鷹 武=武蔵小金井 大=大宮 千=千葉 (six destinations).
- JR East, Omiya Station, Saikyo and Kawagoe Lines toward Shinjuku and Osaki, weekday: 無印=新木場 新=新宿 海=海老名 池=池袋 大=大崎.
- JR East, Tokyo Station, Chuo Line Rapid toward Shinjuku, Hachioji, Kofu and Matsumoto, Saturday and holiday: 無印=高尾 青=青梅 豊=豊田 大=大月 立=立川 武=武蔵小金井 八=八王子 甲=甲府 松=松本 竜=竜王 河=河口湖 国=国分寺 (twelve destinations). Contrast with Jamaica: nine of these twelve (高尾, 豊田, 大月, 立川, 武蔵小金井, 八王子, 甲府, 竜王, 国分寺) are on the Chuo Line itself; 青梅 is on the Ome Line, which branches at Tachikawa; 河口湖 is on the Fujikyuko Line, another company's line reached by through service from Otsuki; 松本 is on the Shinonoi Line, beyond the Chuo Main Line. So most of Tokyo's destinations lie along one line, while Jamaica's sixteen are spread across nine branches.

Since the LIRR branches this much, I adopted the LIRR's convention instead of single-character marks: the destination written out or abbreviated, color-coded by branch.

### How it got here

Include image of the 2019 Word document (lirrschedule.docx, Port Jefferson Branch weekday, Huntington) as the earlier hand-made version. [Word screenshot to be supplied by the author.] Caption: "My first attempt, from 2019: the Port Jefferson Branch weekday timetable at Huntington, made by hand in Word from the MTA's September 2019 timetable."

First attempt (2019, the Word document: LIRR Port Jefferson Branch weekday service at Huntington, and a weekday S1 bus table Halesite to Amityville): I manually copied it from the official MTA timetable of September 2019.

Then generated from GTFS: a Node.js API in 2020 (deparch-api, from December 2020) and a Vue front end in the Japanese style in 2021 (deparch, from January 2021). Now the board is built on OneBusAway.

Why OneBusAway: I can avoid reinventing the wheel.

What OneBusAway provides: import, persist, and query GTFS data. They have designed an optimized data structure for GTFS data that I never attempted.[^oba]

## Body: the board

How the board does this: each departure is labeled with the destination of its own trip (from the GTFS trip data) as a colored pill next to the minute; a destination picker filters to the trains that stop at a chosen station; hours continue past 23 for trips after midnight.

Include image of mine: board-mineola-outbound.png (Mineola, Outbound, 24h, with destination pills HUN, OBY, PGE, PJN, RON and a 24 row). [Caption: to be written; the author wants it simpler.]

Include image of mine: board-ronkonkoma-inbound-top.png (Ronkonkoma, Inbound, with the "Trips toward" filter showing Penn Station labeled "Unlabeled", Atlantic Terminal ATL, and Grand Central GCT). Use this to show that only ATL and GCT trips carry a pill and Penn Station trips are unmarked, the same convention as 無印 in the Nishi-Ooi legend. Caption: "The board for Ronkonkoma, inbound. Trains to Atlantic Terminal (ATL) and Grand Central (GCT) carry a pill; trains to Penn Station carry none, like 無印 on the Japanese timetable."

Goal: I wanted riders to create Japan-style departure timetables through a web interface. I also wanted these to be potentially usable by an agency that may want to mass-produce departure timetables for each station.

Pills: a simple clean design. Their shape also mimics that of the headsigns shown on the sides of LIRR cars.

What was hard: coming up with the terminal abbreviations that appear in the pills was up to my discretion. In September 2026, the beginning of a new schedule used terminal stations that had not been used before, which caused buggy behavior. Trips with destinations that had no abbreviation went unlabeled. So if most trains from Bethpage eastward terminate in Ronkonkoma, the Central Islip trains would appear to be Ronkonkoma trains, since both are shown with the "Unlabeled" label. This was fixed by adding new abbreviations for Central Islip and Farmingdale, plus ten "(Bus)" headsign variants.[^bug]

Destination filter: this is a fundamental part of the design. If someone commutes between two stations, this is a useful feature, because not all trains that pass through a station actually stop there. LIRR branching already adds a level of complexity to the timetable, so by replacing the express/local signing that Japanese timetables tend to do with origin-destination choosing, I can still allow users to create useful timetables.

Hours past 23: the LIRR is not the best example of how this is beneficial, because it tends to publish its GTFS data from midnight to midnight, since the MTA runs its subway and LIRR 24 hours a day. Boston's trains run from about 5 AM to 1 AM (0500 to 2500). Counting past 23 gives clarity on what service day is indicated. It is probably not useful for a Saturday commuter to see the last few trains of "Friday night" (1 AM) and then four hours of blank lines before the trains start at 5 AM again.

For an agency: all that is necessary is for the agency to choose an origin station and then inbound or outbound.

New terminals: new GTFS data becomes available several days or weeks before that part of the schedule becomes current. Currently I have a script that watches for new termini so that I can create abbreviations as they come up.[^terminals]

Japanese language: since this format was inspired by timetables I saw in Japan, I wanted a Japanese-language option. Perhaps people visiting from Japan would find it familiar.

Not yet implemented: one thing the LIRR might want to do is indicate on the timetable which trips are timed for onward travel. This is something the LIRR prominently indicates on timetables and station signage, but it is not something I have seen in Japanese timetables. An inbound train from Montauk will usually have a transfer at its terminus of Jamaica that allows onward westward travel. An outbound train to Huntington will often arrive a few minutes before a Port Jefferson train so that eastbound passengers can transfer to the Port Jefferson train. This kind of indication is not yet implemented in my app.

## Final words

Try it at <https://bit.ly/lirrboard>. Feedback from LIRR commuters welcome: comment on my LinkedIn post about the board, <https://lnkd.in/p/gvgmEXC4>.

## Notes

[^branches]: East of Jamaica per Wikipedia's list, excluding the seasonal Belmont Park Branch and counting Babylon and Montauk as one line: Far Rockaway, Hempstead, Long Beach, Babylon/Montauk, Oyster Bay, Port Jefferson, Ronkonkoma, West Hempstead.
[^diagram]: Wikimedia Commons, File:LIRR_schematic.svg, public domain; schematic as of 2013, current version 2023 by ComplexRational, original by NE2. Credit is not required; give it anyway.
[^bug]: Git: 54d1120, 2026-09-11, transit-board#3. The commit also added a coverage check that flags missing abbreviations.
[^terminals]: Git: 2c100b8, 2026-09-11, check_headsign_coverage in the GTFS updater.
[^oba]: From the OneBusAway source: the bundle builder reads GTFS into a transit graph, an object graph of agencies, stops, trips, blocks and routes, serialized to disk as TransitGraph.obj, alongside block-based stop-time indices (BlockTripIndices.obj) and a spatial index (an STRtree) over stop locations. Sources: TransitGraphImpl and FederatedTransitDataBundle in onebusaway-application-modules. The docs only say "a series of files and optimized data structures".

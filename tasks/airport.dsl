~ A start '~' is used for commenting.

~ This is the file, that contains my dsl language.
~ The idea behind this dsl, is to write a small interpreter which converts some text to a kind of database. In this scenario
~ we are at the airport. And the airport vehicle manager always wants to know how many vehicles (planes, helicopters, cars, busses)
~ are at the airport. So he just counts how many vehicles arrived / landed on the airport and how many departed within one hour.
~ If he asks then the system how many vehicles there are at the airport he always get the amount from the last error.
~ It starts with an empty airport in the morning:

~ 06:00 AM
12 cars arrive
2 planes land
3 busses arrive
3 cars leave
10 taxis arrive
3 taxis leave



~ 07:00 AM
42 cars arrive
7 planes land
2 busses arrive
15 cars leave
4 busses leave
3 planes depart
10 taxis arrive
3 taxis leave



~ 08:00 AM
58 cars arrive
5 planes land
3 busses arrive
3 cars leave
1 helicopters arrive
6 planes depart
10 taxis arrive
3 taxis leave


~ 09:00 AM
108 cars arrive
10 planes land
5 busses arrive
73 cars leave
2 helicopters arrive
3 planes depart
10 taxis arrive
3 taxis leave
4 busses leave


~ 10:00 AM
81 cars arrive
4 planes land
6 busses arrive
35 cars leave
3 helicopters arrive
8 planes depart
10 taxis arrive
3 taxis leave


~ 11:00 AM
31 cars arrive
7 planes land
10 busses arrive
61 cars leave
4 helicopters arrive
10 planes depart
10 taxis arrive
3 taxis leave



~ 12:00 AM
~ lunch break for all
60 cars leave



~ 01:00 PM
60 cars arrive
4 planes land
6 busses arrive
90 cars leave
2 helicopters leave
5 planes depart
3 taxis arrive
10 taxis leave



~ 02:00 PM
55 cars arrive
4 planes land
8 busses arrive
78 cars leave
2 helicopters leave
7 planes depart
3 taxis arrive
10 taxis leave



~ 03:00 PM
7 planes land
2 busses arrive
50 cars arrive
1 helicopters leave
6 planes depart
3 taxis arrive
10 taxis leave




~ 04:00 PM
21 cars arrive
6 planes land
3 busses arrive
64 cars leave
1 helicopters leave
5 planes depart
3 taxis arrive
10 taxis leave
15 busses leave


~ 05:00 PM
41 cars arrive
15 busses leave
5 planes land
43 cars leave
1 helicopters leave
5 planes depart
3 taxis arrive
10 taxis leave



~ 06:00 PM
16 cars arrive
1 planes land
10 busses leave
49 cars leave
2 helicopters leave
4 planes depart
3 taxis arrive
10 taxis leave

How many cars are at the airport?
How many taxis are at the airport?
How many busses are at the airport?
How many planes are at the airport?
How many helicopters are at the airport?

~ Now the airport parking manager wonders whose helicopter is this... He puts a parking ticket at the windshield and
~ drives home.

~ 06:15 PM
1 cars leave
How many cars are at the airport?

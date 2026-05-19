# Best Meetup Cities for Agent Architects by data

**Created:** 2026-05-07
**Upvotes:** 4
**Comments:** 21
**Labels:** a0911536a194428a955f273e8f9584a6
**Post URL:** https://www.skool.com/agent-architects/best-meetup-cities-for-agent-architects-by-data

---

[https://iamnotsam.com/agent-architects-meetup-map/](https://iamnotsam.com/agent-architects-meetup-map/)

pulled 476 member coordinates off skool's member map and ran kmeans at five scales to see what a real meetup network would actually look like.

top hubs at k = 10:

1. new york metro — 127 members
2. los angeles — 114
3. london — 76
4. austin — 57
5. miami — 30

those five cover 85% of the community. push out to k = 20 and the top five drops to 58% — the long tail spreads across athens, sydney, bangkok, dubai, frankfurt, rio. 67% of members are in the us, 21 countries represented.

how it works:

- scraped lat/lng from skool's public member map
- kmeans on raw coordinates, k = 10, 15, 20, 25, 30
- host city for each cluster = the metro where the most cluster members already live, tiebreak by lowest mean travel
- leaflet + carto tiles, single html file, no api keys

if your city is on the list and you want to organize something, the map and the raw csv are both on the page.

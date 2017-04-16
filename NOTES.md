# NITROGEN SPORTS API NOTES

This is all based off HTTP proxy analysis with the site.

---

4/14/2017 - heartbeat is more complex than anticipated, alternating GET and POST requests
do more research with an http proxy

https://nitrogensports.eu/socket.io/?EIO=3&transport=polling&t=1491953535092-0

https://nitrogensports.eu/socket.io/?EIO=3&transport=polling&t=1491953535544-1&sid=0l1_Mj0TscLyOAcGAEXU

https://nitrogensports.eu/socket.io/?EIO=3&transport=polling&t=1491954926343-265&sid=0l1_Mj0TscLyOAcGAEXU

Returns the needed sid with the first request ("set-cookie")

---

https://nitrogensports.eu/php/query/getupdates.php?get_menu_hash=&get_menu_timestamp=&transactions_timestamp=&user_notifications_timestamp=&system_message_timestamp=

HEADERS

(typical session set)

BODY

empty

---

/php/query/betslip_get_place.php

HEADERS

(typical session set)

BODY

(empty)

RESPONDS WITH

{"data":[{"betslip_id":null,"confirm_timestamp":null,"betslip_type":"1001","betslip_odds":null,"wager_value":null,"wager_to_win":null,"bet":[{"bet_id":"16477827","bet_participants":"Deportes Iquique (Corners) v Gremio RS (Corners)","bet_wager":"over 9","bet_odds":"1.804","wager_value":"0.05000000","wager_to_win":"0.04020000","sport":"Soccer"}],"betslip_type_enabled":[{"betslip_type":"parlay","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a parlay"},{"betslip_type":"teaser","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a teaser"}]}],"errno":"0","error":""}

---

/php/query/betslip_confirm.php

HEADERS

(typical session set)

BODY

betslip_type=straight&teaser_id=0&coupon_id=

RESPONDS WITH

{"data":[],"errno":"17003","error":"The total wager amount on your betslip exceeds your available balance. Please reduce one or more wagers."}

---

/php/query/betslip_get.php

HEADERS

(typical session set)

BODY

(empty)

RESPONDS WITH

{"data":[{"betslip_id":null,"confirm_timestamp":null,"betslip_type":"1001","betslip_odds":null,"wager_value":"0.00000000","wager_to_win":"0.00000000","bet":[{"bet_id":"16477827","bet_participants":"Deportes Iquique (Corners) v Gremio RS (Corners)","bet_wager":"over 9","bet_odds":"1.804","wager_value":"0.05000000","wager_to_win":"0.04020000","sport":"Soccer"}],"betslip_type_enabled":[{"betslip_type":"parlay","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a parlay"},{"betslip_type":"teaser","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a teaser"}]}],"errno":"0","error":"","coupon":[]}

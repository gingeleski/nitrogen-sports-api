# NITROGEN SPORTS API NOTES

This is all based off HTTP proxy analysis with the site.

---

https://nitrogensports.eu/socket.io/?EIO=3&transport=polling&t=1491953535092-0

https://nitrogensports.eu/socket.io/?EIO=3&transport=polling&t=1491953535544-1&sid=0l1_Mj0TscLyOAcGAEXU

https://nitrogensports.eu/socket.io/?EIO=3&transport=polling&t=1491954926343-265&sid=0l1_Mj0TscLyOAcGAEXU

Returns the needed sid with the first request ("set-cookie")

---

https://nitrogensports.eu/php/login/login.php

HEADERS

cf_clearance
login_link
PHPSESSID
x-csrftoken

BODY

username=<username>&password=<password>&otp=&captcha_code=

RESPONDS WITH

{"errno":0,"error":"","user_id":"1698869","user_name":"flot989","login_mode":"2","login_link":"6945d012567a2b80ec38e0a66a732d78fcdfdff3d13a66b6304dc76f36caa0b8","bitcoin_address":"1EjbPpbSs98dZRX57fy7Zo26tM7heuDPv","chat_nickname":"flot989","odds_format":"decimal","chat_token":"52be463787323f3b424053effcc12e1c","poker_token":null,"balance":"0.00000300","inplay":"0.00000000","csrf_token":"oDyenLkSe6xJG3FVkin+Y6ds3NjlYcCKHokXlUBybYTdnJWgFyQgyvF+1FtDwRRBQMuh+3Xjj8tLu4r+88FDV7YLPo3T8bRIs4y3tDo6fN1csAx15dGffmqB+gj96ETiXdewUdYvSI+4sLItQ\/N9H0h680j+QHTXeVYvdoxA7TJIhLWPXVkx+W7HaNRUSsH2u5wHdiB6wiZhCY9PZVsfTg==|m+kwrxOrzJEtOqGauW2FEMSXL8vN9dJnIchfDXHDqes=|MzQ3ODIwNTY=|NTYzNzAwNjc="}

---

https://nitrogensports.eu/php/query/getupdates.php?get_menu_hash=&get_menu_timestamp=&transactions_timestamp=&user_notifications_timestamp=&system_message_timestamp=

HEADERS

(same set as above)

BODY

empty

---

https://nitrogensports.eu/php/query/betslip_get.php

HEADERS

(same set as above)

BODY

empty

RESPONDS WITH

{"data":[],"errno":0,"error":"","coupon":[]}

---

https://nitrogensports.eu/php/query/findgames_upcomming.php

HEADERS

(same set as above)

BODY

sport=Soccer

RESPONDS WITH
 
{"errno":0,"error":"","tabs":[],"data":[{"event_id":"713342575","startDateTime":1491955200,"drawRotNum":"0","awayTeam_name":"Barcelona (Ecu) (Corners)","awayTeam_rotNum":"30661","awayTeam_pitcher":"","homeTeam_name":"Estudiantes (Corners)","homeTeam_rotNum":"30660","homeTeam_pitcher":"","sport":"Soccer - CONMEBOL - Copa Libertadores Corners","period":[{"event_id":"713342575","period_id":"385553373","period_description":"Match","cutoffDateTime":1491955200,"spread":null,"moneyLine":null,"total":[{"event_id":"713342575","period_id":"385553373","total_id":"-1","points":"9","overPrice":"1.983","underPrice":"1.804"}],"teamTotal":[{"event_id":"713342575","period_id":"385553373","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"0.00","maxBetAmount_moneyLine":"0.00","maxBetAmount_totalPoints":"0.18"}]},{"event_id":"713124089","startDateTime":1491955200,"drawRotNum":"6307","awayTeam_name":"Club Leon","awayTeam_rotNum":"6306","awayTeam_pitcher":"","homeTeam_name":"Chiapas F.C","homeTeam_rotNum":"6305","homeTeam_pitcher":"","sport":"Soccer - Mexico - Primera Division","period":[{"event_id":"713124089","period_id":"385561445","period_description":"Match","cutoffDateTime":1491955200,"spread":[{"event_id":"713124089","period_id":"385561445","spread_id":"1647210956","awaySpread":"-0.5","awayPrice":"2.291","homeSpread":"+0.5","homePrice":"1.670"},{"event_id":"713124089","period_id":"385561445","spread_id":"1647210958","awaySpread":"+0","awayPrice":"1.643","homeSpread":"+0","homePrice":"2.331"}],"moneyLine":[{"event_id":"713124089","period_id":"385561445","moneyLine_id":-1,"awayPrice":"2.286","homePrice":"3.241","drawPrice":"3.530"}],"total":[{"event_id":"713124089","period_id":"385561445","total_id":"1647210955","points":"2.5","overPrice":"1.571","underPrice":"2.440"},{"event_id":"713124089","period_id":"385561445","total_id":"-1","points":"3","overPrice":"1.945","underPrice":"1.927"},{"event_id":"713124089","period_id":"385561445","total_id":"1647210961","points":"3.5","overPrice":"2.459","underPrice":"1.561"}],"teamTotal":[{"event_id":"713124089","period_id":"385561445","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"4.20","maxBetAmount_moneyLine":"2.10","maxBetAmount_totalPoints":"4.20"}]},{"event_id":"710036603","startDateTime":1491955200,"drawRotNum":"30662","awayTeam_name":"Barcelona (Ecu)","awayTeam_rotNum":"30661","awayTeam_pitcher":"","homeTeam_name":"Estudiantes","homeTeam_rotNum":"30660","homeTeam_pitcher":"","sport":"Soccer - CONMEBOL - Copa Libertadores","period":[{"event_id":"710036603","period_id":"385563652","period_description":"Match","cutoffDateTime":1491955200,"spread":[{"event_id":"710036603","period_id":"385563652","spread_id":"1647230990","awaySpread":"+0.5","awayPrice":"2.608","homeSpread":"-0.5","homePrice":"1.507"},{"event_id":"710036603","period_id":"385563652","spread_id":"-1","awaySpread":"+1","awayPrice":"1.936","homeSpread":"-1","homePrice":"1.954"},{"event_id":"710036603","period_id":"385563652","spread_id":"1647230984","awaySpread":"+1.5","awayPrice":"1.499","homeSpread":"-1.5","homePrice":"2.638"}],"moneyLine":[{"event_id":"710036603","period_id":"385563652","moneyLine_id":-1,"awayPrice":"8.398","homePrice":"1.511","drawPrice":"4.010"}],"total":[{"event_id":"710036603","period_id":"385563652","total_id":"1647230985","points":"1.5","overPrice":"1.436","underPrice":"2.826"},{"event_id":"710036603","period_id":"385563652","total_id":"-1","points":"2","overPrice":"1.804","underPrice":"2.073"},{"event_id":"710036603","period_id":"385563652","total_id":"1647230991","points":"2.5","overPrice":"2.430","underPrice":"1.575"}],"teamTotal":[{"event_id":"710036603","period_id":"385563652","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"4.20","maxBetAmount_moneyLine":"2.10","maxBetAmount_totalPoints":"4.20"}]},{"event_id":"713342574","startDateTime":1491957900,"drawRotNum":"0","awayTeam_name":"Deportes Iquique (Corners)","awayTeam_rotNum":"30658","awayTeam_pitcher":"","homeTeam_name":"Gremio RS (Corners)","homeTeam_rotNum":"30657","homeTeam_pitcher":"","sport":"Soccer - CONMEBOL - Copa Libertadores Corners","period":[{"event_id":"713342574","period_id":"385553320","period_description":"Match","cutoffDateTime":1491957900,"spread":null,"moneyLine":null,"total":[{"event_id":"713342574","period_id":"385553320","total_id":"-1","points":"9","overPrice":"1.804","underPrice":"1.983"}],"teamTotal":[{"event_id":"713342574","period_id":"385553320","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"0.00","maxBetAmount_moneyLine":"0.00","maxBetAmount_totalPoints":"0.18"}]},{"event_id":"710034762","startDateTime":1491957900,"drawRotNum":"30659","awayTeam_name":"Deportes Iquique","awayTeam_rotNum":"30658","awayTeam_pitcher":"","homeTeam_name":"Gremio RS","homeTeam_rotNum":"30657","homeTeam_pitcher":"","sport":"Soccer - CONMEBOL - Copa Libertadores","period":[{"event_id":"710034762","period_id":"385561835","period_description":"Match","cutoffDateTime":1491957900,"spread":[{"event_id":"710034762","period_id":"385561835","spread_id":"1647214552","awaySpread":"+0.5","awayPrice":"2.816","homeSpread":"-0.5","homePrice":"1.438"},{"event_id":"710034762","period_id":"385561835","spread_id":"-1","awaySpread":"+1","awayPrice":"2.142","homeSpread":"-1","homePrice":"1.766"},{"event_id":"710034762","period_id":"385561835","spread_id":"1647214546","awaySpread":"+1.5","awayPrice":"1.619","homeSpread":"-1.5","homePrice":"2.360"}],"moneyLine":[{"event_id":"710034762","period_id":"385561835","moneyLine_id":-1,"awayPrice":"8.644","homePrice":"1.445","drawPrice":"4.490"}],"total":[{"event_id":"710034762","period_id":"385561835","total_id":"1647214549","points":"2","overPrice":"1.488","underPrice":"2.648"},{"event_id":"710034762","period_id":"385561835","total_id":"1647214551","points":"2.5","overPrice":"2.013","underPrice":"1.854"}],"teamTotal":[{"event_id":"710034762","period_id":"385561835","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"4.20","maxBetAmount_moneyLine":"2.10","maxBetAmount_totalPoints":"4.20"}]},{"event_id":"710779715","startDateTime":1491958800,"drawRotNum":"39065","awayTeam_name":"Sporting San Miguel","awayTeam_rotNum":"39064","awayTeam_pitcher":"","homeTeam_name":"Santa Gema FC","homeTeam_rotNum":"39063","homeTeam_pitcher":"","sport":"Soccer - Panama - Primera Division","period":[{"event_id":"710779715","period_id":"385555594","period_description":"Match","cutoffDateTime":1491958800,"spread":null,"moneyLine":null,"total":[{"event_id":"710779715","period_id":"385555594","total_id":"-1","points":"2.5","overPrice":"2.498","underPrice":"1.465"}],"teamTotal":[{"event_id":"710779715","period_id":"385555594","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"0.07","maxBetAmount_moneyLine":"0.00","maxBetAmount_totalPoints":"0.07"}]},{"event_id":"710846691","startDateTime":1491958800,"drawRotNum":"0","awayTeam_name":"Plaza Amador","awayTeam_rotNum":"39076","awayTeam_pitcher":"","homeTeam_name":"Atletico Veraguense","homeTeam_rotNum":"39075","homeTeam_pitcher":"","sport":"Soccer - Panama - Primera Division","period":[{"event_id":"710846691","period_id":"385333009","period_description":"Match","cutoffDateTime":1491958800,"spread":null,"moneyLine":null,"total":null,"teamTotal":[{"event_id":"710846691","period_id":"385333009","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"0.00","maxBetAmount_moneyLine":"0.00","maxBetAmount_totalPoints":"0.00"}]},{"event_id":"710062447","startDateTime":1491962400,"drawRotNum":"6280","awayTeam_name":"Puebla FC","awayTeam_rotNum":"6279","awayTeam_pitcher":"","homeTeam_name":"Veracruz","homeTeam_rotNum":"6278","homeTeam_pitcher":"","sport":"Soccer - Mexico - Primera Division","period":[{"event_id":"710062447","period_id":"385561433","period_description":"Match","cutoffDateTime":1491962400,"spread":[{"event_id":"710062447","period_id":"385561433","spread_id":"1647210856","awaySpread":"-0.5","awayPrice":"2.856","homeSpread":"+0.5","homePrice":"1.434"},{"event_id":"710062447","period_id":"385561433","spread_id":"-1","awaySpread":"+0","awayPrice":"2.013","homeSpread":"+0","homePrice":"1.877"},{"event_id":"710062447","period_id":"385561433","spread_id":"1647210851","awaySpread":"+0.5","awayPrice":"1.497","homeSpread":"-0.5","homePrice":"2.658"}],"moneyLine":[{"event_id":"710062447","period_id":"385561433","moneyLine_id":-1,"awayPrice":"2.883","homePrice":"2.695","drawPrice":"3.210"}],"total":[{"event_id":"710062447","period_id":"385561433","total_id":"1647210850","points":"2","overPrice":"1.542","underPrice":"2.509"},{"event_id":"710062447","period_id":"385561433","total_id":"-1","points":"2.5","overPrice":"2.083","underPrice":"1.791"},{"event_id":"710062447","period_id":"385561433","total_id":"1647210857","points":"3","overPrice":"2.955","underPrice":"1.394"}],"teamTotal":[{"event_id":"710062447","period_id":"385561433","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"2.80","maxBetAmount_moneyLine":"2.10","maxBetAmount_totalPoints":"2.80"}]},{"event_id":"710060318","startDateTime":1491962400,"drawRotNum":"6277","awayTeam_name":"Guadalajara","awayTeam_rotNum":"6276","awayTeam_pitcher":"","homeTeam_name":"Tigres","homeTeam_rotNum":"6275","homeTeam_pitcher":"","sport":"Soccer - Mexico - Primera Division","period":[{"event_id":"710060318","period_id":"385561035","period_description":"Match","cutoffDateTime":1491962400,"spread":[{"event_id":"710060318","period_id":"385561035","spread_id":"1647209004","awaySpread":"+0","awayPrice":"3.153","homeSpread":"+0","homePrice":"1.364"},{"event_id":"710060318","period_id":"385561035","spread_id":"-1","awaySpread":"+0.5","awayPrice":"1.945","homeSpread":"-0.5","homePrice":"1.945"},{"event_id":"710060318","period_id":"385561035","spread_id":"1647208998","awaySpread":"+1","awayPrice":"1.432","homeSpread":"-1","homePrice":"2.886"}],"moneyLine":[{"event_id":"710060318","period_id":"385561035","moneyLine_id":-1,"awayPrice":"4.494","homePrice":"1.950","drawPrice":"3.400"}],"total":[{"event_id":"710060318","period_id":"385561035","total_id":"1647209001","points":"2","overPrice":"1.695","underPrice":"2.212"},{"event_id":"710060318","period_id":"385561035","total_id":"1647209003","points":"2.5","overPrice":"2.271","underPrice":"1.652"}],"teamTotal":[{"event_id":"710060318","period_id":"385561035","teamTotal_id":-1,"awayTeamTotal_total":null,"awayTeamTotal_overPrice":null,"awayTeamTotal_underPrice":null,"homeTeamTotal_total":null,"homeTeamTotal_overPrice":null,"homeTeamTotal_underPrice":null}],"maxBetAmount_spread":"2.80","maxBetAmount_moneyLine":"2.10","maxBetAmount_totalPoints":"2.80"}]}]}

---

https://nitrogensports.eu/php/query/betslip_bet_adjustRisk.php

HEADERS

(the usual)

BODY

bet_id=16477827&risk=0.05000

RESPONDS WITH

{"errno":"0","error":""}

---

/php/query/betslip_get_place.php

HEADERS

(the usual)

BODY

(empty)

RESPONDS WITH

{"data":[{"betslip_id":null,"confirm_timestamp":null,"betslip_type":"1001","betslip_odds":null,"wager_value":null,"wager_to_win":null,"bet":[{"bet_id":"16477827","bet_participants":"Deportes Iquique (Corners) v Gremio RS (Corners)","bet_wager":"over 9","bet_odds":"1.804","wager_value":"0.05000000","wager_to_win":"0.04020000","sport":"Soccer"}],"betslip_type_enabled":[{"betslip_type":"parlay","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a parlay"},{"betslip_type":"teaser","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a teaser"}]}],"errno":"0","error":""}

---

/php/query/betslip_confirm.php

HEADERS

(the usual)

BODY

betslip_type=straight&teaser_id=0&coupon_id=

RESPONDS WITH

{"data":[],"errno":"17003","error":"The total wager amount on your betslip exceeds your available balance. Please reduce one or more wagers."}

---

/php/query/betslip_get.php

HEADERS

(the usual)

BODY

(empty)

RESPONDS WITH

{"data":[{"betslip_id":null,"confirm_timestamp":null,"betslip_type":"1001","betslip_odds":null,"wager_value":"0.00000000","wager_to_win":"0.00000000","bet":[{"bet_id":"16477827","bet_participants":"Deportes Iquique (Corners) v Gremio RS (Corners)","bet_wager":"over 9","bet_odds":"1.804","wager_value":"0.05000000","wager_to_win":"0.04020000","sport":"Soccer"}],"betslip_type_enabled":[{"betslip_type":"parlay","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a parlay"},{"betslip_type":"teaser","enabled":"70800","reason":"You need at least 2 bets on your betslip to make a teaser"}]}],"errno":"0","error":"","coupon":[]}

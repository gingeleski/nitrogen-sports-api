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
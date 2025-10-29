import datetime
d= datetime.datetime
# PS C:\Users\Arsa Diwangsa> curl.exe -i -X GET https://cbt-omi.kemenag.go.id/api/exams/is-active
# HTTP/1.1 200 OK
# Server: nginx/1.24.0 (Ubuntu)
# Date: Sun, 31 Aug 2025 10:33:20 GMT
# Content-Type: application/json; charset=utf-8
# Content-Length: 258
# Connection: keep-alive
# X-Powered-By: Express
# Access-Control-Allow-Origin: *
# ETag: W/"102-bMwVaBJRl4197+Q3EfwExS1crHY"
# Set-Cookie: cookiesession1=678B2A5E338CC1F21614118A7A0723DC;Expires=Mon, 31 Aug 2026 10:33:20 GMT;Path=/;HttpOnly
# X-Frame-Options: SAMEORIGIN
# X-Content-Type-Options: nosniff
# X-XSS-Protection: 1; mode=block

# {"total":1,"data":[{"_id":"68b146cede9796511114c8cc","name":"UJI COBA - OMI","description":"SOAL UJI COBA - OMI 2025","scheduling":{"start":1756362300000,"end":1756659600000,"allocation":60,"allowDoneAfter":0},"participants":198544,"doneParticipants":1878}]}
# PS C:\Users\Arsa Diwangsa>
# PS C:\Users\Arsa Diwangsa>

print(d.fromtimestamp(1756362300))
print(d.fromtimestamp(1756659600))
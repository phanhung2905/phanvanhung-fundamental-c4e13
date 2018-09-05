from gmail import GMail, Message
import datetime

mail = GMail("hube88kg@gmail.com", "hunghanh2905")
body = """
<p style="text-align: center;">cộng h&ograve;a x&atilde; hội chủ nghĩa việt nam</p>
<p style="text-align: center;">độc lập-tự do-hạnh ph&uacute;c</p>
<h1 style="text-align: center;"><span style="text-decoration: underline;">đơn xin nghỉ ốm</span></h1>
<p>t&ecirc;n t&ocirc;i l&agrave;: phan văn h&ugrave;ng</p>
<p>v&igrave; s&aacute;ng nay t&ocirc;i bị ốm n&ecirc;n ko thể đi l&agrave;m được</p>
<p>t&ocirc;i xin cảm ơn.</p>
<p style="text-align: right;">k&yacute; t&ecirc;n</p>
<p style="text-align: right;">phan văn h&ugrave;ng</p>
"""
msg = Message("hungpv - xin nghi om", to="hunghanh2905@gmail.com", html=body)
mail.send(msg)


loop = True
while loop:
    now = datetime.datetime.now().hour
    if now == 7:
        mail.send(msg)
        loop = False
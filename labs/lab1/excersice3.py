

from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["posts"]





haids = {
    "title": "karazy-andree",
    "author": "pvh",
    "content":
"""
    Verse 1: Binz] 
Anh hỏi nè 
Bạn trai cũ của em sao? (sao?) 
Thôi không cần nói ừ nó tệ thật (khỏi!) 
Wow người ta bỏ em, how? (how?) 
Tiếp cận được em đã là nghệ thuật 
Anh nói xinh cỡ em vậy là đủ rồi 
Thí sinh The Face không đủ tuổi (ey) 
Đừng để anh nói "Đệt? uôiii" 
Như xuất thân từ Hà Nội 
Nếu em thích lạ, anh đổi flow 
Nếu em thích high, anh đủ cỏ 
So call your girl, get comfortable 
Dẫn bạn đi theo xe anh đủ chỗ 
So baby fuck with me 
Con trai quanh em thiếu gì 
But I know you like me 
'Cause you know I'm drama free 

[Chorus: Binz, Evy] 
I said I'm crazy 'bout you 
I'm crazy about you 
I'm crazy about you 
I'm crazy about you 
I'm crazy about you 
I'm crazy 'bout you 
I know you like me (I'm crazy about you) 
You know I'm drama free (I'm cra... cra... cra...) 
I said I'm crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
I'm cra... cra... cra... 
(Hol'up) 

[Verse 2: Andree Right Hand] 
Mắt to 
Môi đỏ 
Mùi hương làm anh chú ý một ai đó 
Làn mi cong cùng mascara 
Hôm nay đâu phải thứ 6 ngày 13 (hahhh) 
Gọi giúp anh 115 đi này 
Bởi vì tim anh đang loạn nhịp (Ah hah hah hah hah) 
Đường cong thân thể em làm anh thở không kịp (nah nah nah) 
Đầu hướng bắc, phần còn lại hướng nam 
Nếu em ích kỷ, anh là kẻ tham lam 
Anh là con nghiện, em là chất kích thích 
Đêm nay sử sách ghi lại như trận Xích Bích (yeah) 
Nếu em là mơ, anh mãi chìm vào giấc ngủ (Ah) 
Nếu anh là nhà thơ, viết về em chưa bao giờ là đủ 
Xe chở Binz ghế sau chưa biết chở ai đang thừa đến 3 chỗ 
Gọi thêm cả bạn em đi, sở trường của anh là Bi-a lỗ 
Em nói em sợ trai Bắc "không sao anh sẽ nói thử tiếng Sài Gòn" 
Em nghĩ anh đùa em chắc dành cả tuổi thanh xuân theo đuổi em vì không thích "Tôi cô đơn" 



[Chorus: Binz, Evy] 
Yeah I said I'm crazy 'bout you 
I'm crazy about you 
I'm crazy about you 
I'm crazy about you 
I'm crazy about you 
I'm crazy 'bout you 
I know you like me (I'm crazy about you) 
You know I'm drama free (I'm cra... cra... cra...) 
I said I'm crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
Crazy about you 
I'm cra... cra... cra... 

[Bridge: Binz, Andree Right Hand] 
Người ta nói em so bad nhưng mà anh thích em baby so what? 
Người ta nói anh so fly, nếu có em bên cạnh người ta đâu sai 
Mấy cô gái chửi em, anh chắc là câu like 
Fuck túp lều tranh em xứng với lâu đài 
Trên cổ anh nghe là Chanel Nº5 
Nếu mà anh không xứng với em thì đâu ai 
Anh đếm 1, em đếm 2, nhịp cuối cả hai cùng đếm 3 (ah hah) 
Hơi thở hòa quyện vào nhau đêm nay thế giới này chỉ còn có hai ta (brrr brrr) 
Lại gần anh thêm nữa đi 
Son môi hôm nay có phải dùng mùi cherry 
Anh thích như vậy, thì thầm vào tai những điều bí mật em còn che đậy 
Nhưng em ơi em ơi đừng dụ dỗ anh 
Vì nếu em cưa anh sẽ đổ nhanh 
Em ơi em ơi đừng làm khổ anh 
Anh chỉ muốn chân em ở trên cổ anh 
Em ơi em ơi em đừng thả tay 
Em không được tỉnh khi anh đang say 
Em ơi em ơi hãy ở lại đây 
Get high get crazy với anh đêm nay 
"""
}


posts.insert_one(haids)





label op2:
    $ quick_menu = True
    scene bg sc1_4 with normal
    show v3
    v "Alo, Ngân ơi, tôi nghĩ là trong trường mình có chuyện gì đó."

    v "Bà đến trụ sở xin tiếp viện cho tôi nhé. Không thì một mình bà cũng được."

    scene bg sc1_3
    show n2 zorder 3 

    n "Ơ kìa, sao thế?"

    scene bg sc1_4
    show v3 
    stop music fadeout 5.0
    v "Tôi cúp máy đây."
    play music bgm4
    scene bg op1_2 with fadeout
    play sound foot loop volume 0.5 fadein 0.3
    "Cậu rất tin vào linh cảm của mình, đặc biệt hơn khi bẩm sinh cậu lại là khắc tinh của các sinh vật siêu nhiên"

    "Dù biết nếu đi muộn thì phải xếp hàng đợi rất lâu nhưng trường học của cậu cũng quan trọng không kém."

    "Mạnh dạn bước chân qua cổng trường. Cậu cẩn thận quan sát xung quanh."

    scene bg op2_1 with normal

    "Mọi thứ trông có vẻ bình thường. "

    "Quang cảnh xung quanh vẫn như lần gần nhất cậu đến là chiều thứ sáu vừa rồi."

    

    "Có điều..."

    "... trong này có sự hiện diện của nguồn ma lực cao bất thường."

    "Nếu chủ nhân của nó là một pháp sư thì quả là đáng gờm còn nếu là một sinh vật siêu nhiên nào đó, thật không ngoa khi gọi đó là một thảm họa."

    "Cậu tiến thêm vào bên trong trong sự dè chừng."

    stop sound
    scene bg op2_2 with normal
    
    "..."
    
    scene bg op2_3 
    
    $ renpy.music.play("sound/hit_sound.mp3", channel="sfx1", relative_volume = 0.2, fadeout = 0.5, loop = False)

    "Một viên đạn ma thuật sượt qua người, cậu né được trong gang tấc."

    "Với uy lực như thế kia, không né được thì chỉ có banh xác."

    "Dù cho có cường hóa cơ thể thì chấn thương vẫn là điều không thể tránh khỏi."

    "Là ai, hay thứ gì đã tấn công cậu?"

    scene bg op2_4 with normal

    "Chưa kịp hoàn hồn. Có cái gì đó đang lao lại phía cậu."

    "Là người hay thứ gì khác?"

    scene bg op2_5 with normal
    $ renpy.music.play("sound/hit_sound.mp3", channel="sfx1", relative_volume = 0.2, fadeout = 0.5, loop = False)
    "..."

    "Một cú đá nhắm thẳng vào Việt, cậu thoát được trong đường tơ kẽ tóc."

    "Trực giác đã cứu cậu thêm một lần nữa."

    "Uy lực không kém gì viên đạn hồi nãy. Bình tĩnh lại đôi chút, cậu nhận ra trước mặt mình là con người. "

    "Không để cậu kịp trở tay, người phía trước liên tục tấn công, buộc cậu phải vào thế thủ."

    scene bg op2_6
    "Việt thường xuyên tham gia lớp tập huấn võ thuật vào cuối tuần ở trụ sở dưới sự huấn luyện của các võ sư hàng đầu."

    "Điều này cốt là là để khắc phục điểm yếu về ma lực và khả năng triển khai ma thuật."

    "Xét về cận chiến, cậu không phải tay mơ. Thể lực và kỹ thuật của cậu đều thuộc vào loại tốt."

    "Vậy mà kẻ trước mặt đang liên tục tấn công vào chỗ hiểm, dồn cậu vào thế bí."

    "Cậu cố gắng lùi về phía sau, kéo dãn khoảng cách và quan sát đối phương."

    scene bg op2_7 with normal

    "Thân thủ nhanh nhẹn, dáng vóc quen thuộc."

    "Mái tóc dài với sắc lam ánh lên. Không lẽ ...?"

    scene bg op2_8
    stop music fadeout 2

    play music audio.bgm2
    v "Hoàng Giang ?"
    
    scene bg op2_9
    v "Khoan đã... "

    v "Tôi đây. Việt đây."

    scene bg op2_10
    show g1 zorder 3
    "Đối phương dừng lại, vẻ mặt ngạc nhiên sau đó chuyển qua bối rối."

    g "Việt... đấy à?"

    scene bg op2_9
    v "Tôi đây."

    scene bg op2_10
    show g3 zorder 3
    "Giờ cô lại chuyển qua cười trừ."

    g "Ha ha... xin lỗi nhé, tôi tưởng ông là con rối nên là... ha ha... xin lỗi."

    hide g3
    show v6 zorder 3
    "Cậu cũng không biết nói gì hơn."

    "“Xin lỗi á?” Nội tâm cậu thét lên."

    "Cậu suýt mất mạng vì sự nhầm lẫn của cô ta. Thật không ngờ là lại gặp kẻ phá hoại này ở đây."

    # tillup
    scene bg op2_11 

    "Mang dáng vẻ của một thiếu nữ đôi mươi, khó mà tin được cô ta là một pháp sư cực kỳ xuất sắc. "

    "Xuất thân mơ hồ, như thể từ hư không mà xuất hiện ra."

    "Là bạn học cùng lớp nhưng cậu khó mà nắm bắt được cô ta."

    "Một pháp sư tự do, chủ một xưởng búp bê khi vẫn còn là sinh viên, chuyên gia chế tạo và điều khiển rối, thành thạo ngũ đại nguyên tố."

    "Là kẻ có năng lực phá hoại vô biên."

    "Dẫu cho không thuộc bất kỳ tổ chức nào nhưng cô ta luôn được các tổ chức để mắt tới."

    "Ở cô ta luôn có một sức hút nào đó khiến cho giới pháp sư thèm khát."

    scene bg op2_10
    show v7 zorder 3

    v "Bà đang làm gì ở đây? Con rối là sao?"

    hide v7
    show g3 zorder 3
    g "Ờ thì... ờ..."

    hide g3
    show v6 zorder 3
    "Sự ấp úng của cô ta khiến cậu nảy sinh nghi hoặc."

    v "Hửm?"
    
    hide v6
    show g4 zorder 3
    g "Ờ thì là mà..."

    g "Mất rồi."

    hide g4
    show v6 zorder 3
    v "Cái gì mất"

    hide v6
    show g4 zorder 3
    g "Con rối cao cấp mà khách vip của tôi đặt hàng?"

    hide g4
    show v7 zorder 3
    v "Hả?"

    hide v7
    show g4 zorder 3
    g "Cả mấy con rối khác cũng bị lấy mất rồi."

    hide g4
    show v6 zorder 3
    v "Tôi có nghe nhầm không đấy?"

    "Cậu không thể tin vào tai mình, kẻ như cô ta cũng có phút bất cẩn làm mất đồ ."

    hide v6
    show g4 zorder 3
    g "Sao mà tôi nghĩ được là một con yêu tinh nhỏ như vậy có đủ sức trộm con rối to như thế chứ"

    hide g4
    show v7 zorder 3
    v "Yêu tinh? Ăn trộm?"

    hide v7
    show g4 zorder 3
    g "Đã thế lại còn ở dạng linh hồn, mà nó còn thó được của tôi thêm mấy con rối nữa chứ."

    hide g4
    show v7 zorder 3
    v "Từ từ."

    v "Giải thích lại từ đầu đi. Tôi không hiểu."

    hide v7
    show g4 zorder 3
    g "Sáng sớm nay, tầm 4 giờ sáng ấy, tôi đến xưởng để làm tiếp con rối hình người cao cấp cho khách vip."
    
    g "Vừa mở cửa tôi thấy một con yêu tinh chui tọt vào ngực con rối đó..."

    g "... một lúc sau con rối tự động cựa quậy mắt mở to, đảo như rang lạc..."

    g "... tôi cưỡng chế nó đứng yên nhưng nó kháng lại được lệnh."

    g "Nó còn điều khiển lại mấy con rối tấn công tôi nữa chứ."

    g "Chớp mắt một cái nó chạy đi mất, tôi đuổi theo nó đến tận đây. Giờ mất hút, không thấy đâu."

    hide g4
    show v8 zorder 3
    v "Kết giới do bà dựng ?"

    hide v8
    show g5 zorder 3
    g "Tất nhiên, sao tôi có thể để cho dân thường lại gần đây được."

    hide g5
    show v6 zorder 3
    v "Haizz. Rắc rối rồi đây."

    "Vụ này không dễ, con yêu tinh đó chiếm được cơ thể của con rối do Giang làm. Mà cô ta nổi tiếng làm rối một cách hoàn hảo.."

    "Khách đặt hàng của cô ta đều là những thành phần có máu mặt. Cỡ như cậu không tới lượt."

    "Một con yêu tinh có ý thức cướp một con rối làm cơ thể cũng không thể tầm thường."

    "Nếu nó nằm trong hồ sơ của Hiệp hội trừ tà thì cũng phải từ cấp B trở lên."

    "Hai thứ này kết hợp với nhau thật khó hình dung nó sẽ thành cái thể loại gì."

    hide v6
    show v8
    v "Cao cấp à? Này, con rối đó có gì mà cao cấp thế?"

    hide v8
    show g5 
    g "Nó có tim là viên đá ma thuật. Đắt lắm đấy."
    
    g "Viên đá đó là lõi năng lượng của con rối."

    hide g5
    show v4
    v "Sự cố này lần đầu tôi gặp."

    "Việt rút điện thoại ra nhắn vài dòng đến bạn của mình."

    "Những lúc thế này, cậu cần có thêm thông tin từ kho lưu trữ hồ sơ ở trụ sở."

    "Hai người chìm vào khoảng lặng."

    hide v4
    show g5 
    "Chợt Giang lóe lên một ý tưởng."

    g "Tôi có một đề nghị."

    hide g5
    show v8
    v "Hửm?"

    hide v8
    show g5 
    g "Chúng ta sẽ hợp tác tiêu diệt con yêu tinh này."

    hide g5
    show v7 
    v "Sao tôi phải hợp tác với một kẻ phá hoại?"
    
    hide v7
    show g2 
    g "Ơ kìa"

    hide g2
    show g5
    g "Nếu thành công ông sẽ được khen thưởng, còn tôi sẽ thu hồi lại được đám rối."

    g "Tệ nhất thì có thể tiêu hủy luôn đám rối của tôi cũng được."

    g "Ít ra tôi không thể để danh tiếng của mình tụt dốc vì con yêu tinh kia."

    hide g5
    show v6
    "“Danh tiếng bà cũng có tốt đâu.” Cậu định nói như vậy nhưng lại thôi."

    "Tuy không có mấy thiện cảm nhưng vẫn phải công nhận cô ta rất mạnh, đáng để hợp tác."

    "Nhưng cứ nhớ lại những lần theo sau dọn dẹp rắc rối sau lưng cô ta, cậu lại thấy hơi chùn bước."

    v "Hửm? Mình bà thừa sức cho nó bay màu mà."

    hide v6
    show g5
    g "Còn ông là khắc tinh của nó và tôi nghĩ thổi bay cả trường không phải là ý kiến hay."

    hide g5
    show v6
    "Giờ đây cậu thấy cô ta có chút nguy hiểm. Cảm giác như cô ta đang thao túng cậu vậy. "

    "Có điều nếu kẻ thù là yêu tinh thì cậu không thể không nhúng tay vào. "

    v "Được rồi. Nhưng đừng phá tan hoang trường chúng ta, tôi không muốn gián đoạn lịch học vì lý do vớ vẩn này đâu."

    hide v6
    show g5
    g "Được thôi. Hứa đấy."
    stop music fadeout 5
    call op3

return
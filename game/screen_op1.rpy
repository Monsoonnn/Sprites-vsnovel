
define btv = Character("Biên tập viên")

label op1:
    
    scene bg sc1_4
    show v3
    v "Ờm, đợi chút, tôi chạy đến ngay."
    " “Mình sẽ báo cáo lại cho Hiệp hội”Cậu thầm nghĩ "
    hide v3
    show v4
    "Vấn đề này vẫn nên đợi chỉ thị thì hơn. Nếu tự ý hành động, xử lý êm đẹp thì không sao nhưng có vấn đề dây mơ rễ má gì phía sau e là cậu khó yên ổn."

    "Nghĩ đến đây, cậu lại nhớ tới một kẻ không nằm trong tổ chức nào nhưng chuyên phá hoại và để các tổ chức theo theo sau dọn dẹp."

    "Thỉnh thoảng, công cuộc dọn dẹp đó lại có cậu. Nghĩ lại đến giờ sống mũi vẫn còn còn cay."

    scene bg op1_1 with normal
    
    $ renpy.music.play("sound/running.mp3", channel="sfx1", relative_volume = 0.3, fadeout=0.5)
    $ renpy.music.play("sound/vehicles.mp3", channel="sfx2", relative_volume = 0.7, fadeout=0.5)
    
    "Dứt lời, cậu nhanh chân chạy đến điểm hẹn ."

    "Bọn họ hẹn nhau sẽ cùng đến trụ sở từ sáng sớm, trước giờ hành chính để điền phiếu trước, tránh chen chúc."

    "Cậu băng băng trên con đường vắng vẻ, dù rằng ngày thường ở đây đông như quân Nguyên."

    "..." 
    scene bg op1_2 with fadein
    $ renpy.music.play("sound/heavy_breathing.mp3", channel="sfx2", relative_volume = 0.2, fadeout=0.5)
    "Vừa chạy vừa thở gấp, cậu thấy hôm nay sức mình đuối hơn so với mọi ngày."

    "Dù sao thì chủ nhật các tuần phải là ngày cậu hồi sức chứ không phải là chạy như bay rồi ngồi chờ cả tiếng thế này."

    scene bg op1_3 with normal

    "Thấp thoáng từ xa, cậu thấy bóng dáng bạn mình."

    "Cậu vẫy tay gọi bạn."
 

    scene bg op1_4 with normal 
    stop music fadeout 1
    play music audio.bgm4 fadein 1

    $ renpy.music.set_pause(True,"sfx1")
    $ renpy.music.set_pause(True,"sfx2")
    v " Hự."
    $ renpy.music.play("sound/heart_beat.mp3", channel="sfx2", relative_volume = 0.3, fadeout=0.5)
    "Cậu đột nhiên không còn sức và khụy gối xuống."

    "Cảm giác như ai đó rút cạn hết năng lượng của cậu vậy."

    "Cơ thể cậu tựa như chiếc đồng hồ sắp hết pin."

    scene bg op1_5 with normal

    "Trời đất như xoay vòng."

    scene bg op1_6 with normal
    $ renpy.music.play("sound/heavy_breathing.mp3", channel="sfx1", relative_volume = 0.5, fadeout = 0.5)
    "Định thần lại một chút, cậu không tin vào mắt mình."

    "Mọi người phía trước đang lảo đảo, đi đứng không vững."

    v "Mình hoa mắt đấy à ?"

    scene bg op1_7 with normal
    $ renpy.music.set_pause(True,"sfx1")
    $ renpy.music.play("sound/heart_beat.mp3", channel="sfx2", relative_volume = 1, fadeout = 0.5)
    "Cơn đau đầu dồn đến dữ dội hơn. Cậu nheo mắt lại, cảm giác gần giống với lúc đang đứng ở cổng trường."

    "Khi cậu mở mắt ra, mọi người đã gục hết xuống đất. Cậu thấy xung quanh mình như nhuộm một màu đỏ."

    "Ngực cậu thắt lại, khó thở hơn và dường như đây là giới hạn chịu đựng của cơ thể cậu."

    stop music fadeout 4.0
    $ renpy.music.set_pause(True,"sfx2")
    $ renpy.music.play("sound/body_fall.mp3", channel="sfx1", relative_volume = 1, fadeout = 0.5, loop=False)
    "Cậu nằm gục dưới mặt đất."
    
    scene bg op1_8 with fadeout
    play sound breaking_new volume 0.1
    "12 giờ trưa"

    "Bản tin thời sự trưa"

    btv "Sáng hôm nay, một sự cố đã xảy ra. Người dân ở quận A đột nhiên lăn ra ngất hàng loại, một số người đã tử vong."

    btv "Nguyên nhân đang được điều tra và làm rõ."
    
    
return

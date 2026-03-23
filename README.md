# 안면인식 도어락(간의) 

실수로 6년전꺼 날려버림.....

opencv packege install : git clone https://github.com/opencv/opencv.git 

pip install pillow : PLI 가 필수로 있어야 하니 설치



1. cam_test_webcam.py : 카메라 췍!
2. face_filter.py : 필터(인식기)췎!!

#여기서 부터 찐 시작

3. ID_face_pic.py : ID 입력하고 내 사진들 찍기 (사진이 많으면 좋긴 하지만 시간이 어~~~~~~~~~~~~~~~~~~~ㅁ 청 오래 걸림...)
4. train_img.py : 내 사진 갖고 학습 시작!!
5. OPR_faceid.py, testfaceAD.py : activate!!! 지금 버전은 로어락의 솔레노이드 작동용으로 만듦, testfaceAD는 광고가 뜨게 바꾼버전


# PS . 이거 말고 하고 이벤트가 있을 경우, OPR_faceid.py의 if (confidence < 100):
            name_id = names[id]
            conf_label = "  {0}%".format(round(100 - confidence))  이부분을 찾아서 바꾸면됨
if (100 - confidence) > 40:  이부분이 지금은 40%이상의 일치율일 때 작동되게 되있음
일치율은 맘!대!로! 바꾸면 됩니다.



작동환경 : raspberry_pi3b+, Asus tinker_board, jetson_nano(약간 가공이 필요함)

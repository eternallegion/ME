# 안면인식 도어락(간의) 

실수로 6년전꺼 날려버림.....

opencv packege install : git clone https://github.com/opencv/opencv.git 

pip install pillow : PLI 가 필수로 있어야 하니 설치


mkdir FacialRecognitionProject 햇갈림 방지용 작업 파일
mkdir dataset 내사진(+id) 박제용

mkdir trainer학습결과 저장용




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






# Face recognition door lock (on the liver) 

I accidentally blew my old one six years ago...

opencv packege install : git clone https://github.com/opencv/opencv.git 

pip install pillow : PLI must be installed


mkdir FacialRecognitionProject Anti-Hack Job File
mkdir dataset picture (+id) stuffed

For storing mkdir trainer learning results




1. cam_test_webcam.py : camera check!
2. face_filter.py : filter!!

#Let's start from here

3. ID_face_pic.py : Enter ID and take my pictures (it's nice to have a lot of pictures, but it takes a long time...)
4. train_img.py: Start learning with my picture!!
5. OPR_faceid.py, testfaceAD.py : activate!!! The current version is made for lower lock's solenoid operation, testfaceAD is the version that the ad changed to float


# PS. If (confidence < 100) in OPR_faceid.py:
            name_id = names[id]
            conf_label = "{0%".format(round(100 - confidence) ) Find and replace this part
if (100 - confidence) > 40: This part is now operated at a match rate of 40% or higher
You can change the matching rate to Mom! Dae.




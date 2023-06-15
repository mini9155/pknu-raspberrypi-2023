import cv2
# 일반 이미지
# img = cv2.imread('./Day07/panda.png')


#컬러 이미지
img = cv2.imread('./Day07/panda.png',cv2.IMREAD_GRAYSCALE)

#원본을 두고 흑백을 추가
img = cv2.imread('./Day07/panda.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#03.이미지 사이즈 축소
# img_small = cv2.resize(img,(200,120))
# cv2.imshow('Small', img_small)


# #05 이미지 자르기
height, width, channel = img.shape
print(height, width, channel)

img_crop = img[: , :int(width / 2)] # height width
gray_crop = gray[: , :int(width / 2)] # height width

#이미지 불러
img_blur = cv2.blur(img_crop, (30,30))

# cv2.imshow('Gray', gray)
# cv2.imshow('Original', img)
# cv2.imshow('Original',img)

cv2.imshow('originalHalf', img_crop)
cv2.imshow('gray harf',gray_crop)
cv2.imshow('img_blur',img_blur)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
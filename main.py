import cv2
from PIL import Image
image_path = 'human.jpg'
human_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
human_face = human_face_cascade.detectMultiScale(image, 1.4)
# cat_face = cat_face_cascade.detectMultiScale(image,
#                                              scaleFactor=1.4,
#                                              minNeighbors=5,
#                                              minSize=(10, 10)
#                                              )
print(human_face)
#Створимо об’єкти зображень для кота та окулярів
cat = Image.open(image_path)
glasses = Image.open('icho.png')
boroda = Image.open('ichoo.png')
#альфа-канал дає змогу зробити маску (використати прозорий фон)
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
boroda = boroda.convert("RGBA")
for (x,y,w,h) in human_face:
#Підпасуємо розмір окулярів до мордочки
#зображення прямокутнt, для втримання пропорції поділимо висоту на 3
   glasses = glasses.resize((w, int(h/3)))
   boroda = boroda.resize((w, int(h/4)))
#до y додамо значення h/4, бо висота зображення рівна h/3,
#а очі кота розташовані вище середини мордочки.
   cat.paste(glasses, (x, int(y+h/1.8)),glasses)
   cat.paste(boroda, (x, int(y+h/2)), boroda)
   cat.save("cat_with_glasses.png")
   cat_with_glasses = cv2.imread("cat_with_glasses.png")
   cv2.imshow("Cat_with_glasses", cat_with_glasses)
   cv2.waitKey()
#cv2.imshow("Cat", image)
#cv2.waitKey()

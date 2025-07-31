import cv2
import numpy as np

# تحميل الصورة
image_path = 'FruitColors.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: الصورة غير موجودة.")
    exit()

# تحويل الصورة إلى HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# نطاق اللون الأحمر
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# إنشاء قناع
mask = cv2.inRange(hsv, lower_red, upper_red)

# إيجاد الحدود (Contours)
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# رسم مستطيل حول كل منطقة حمراء
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 300:  # تجاهل الضجيج
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# عرض النتائج
cv2.imshow('Detected Red Areas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


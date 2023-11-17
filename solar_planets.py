import cv2

img=cv2.imread("solar-system.jpg")

cv2.imshow("Display Image",img)

cv2.putText(img,
            "SUN",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "MERCURY",
            (25,350),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "VENUS",
            (30,400),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "EARTH",
            (35,450),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "MARS",
            (40,500),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "JUPITER",
            (45,550),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "SATURN",
            (50,600),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "NEPTUNE",
            (55,650),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.putText(img,
            "URANUS",
            (60,700),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),
            )

cv2.imwrite("solar_planets.jpg",img)

cv2.waitKey(0)
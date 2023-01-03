import cv2
import mediapipe as mp
import numpy as np
import random
import os
import shutil

class DotUtility:

    # FOR FACEMESH LIBRARY
    MOUTH_LEFT_POINT = 61
    MOUTH_TOP_POINT = 0
    MOUTH_BOTTOM_POINT = 16
    MOUTH_RIGHT_POINT = 409
    NOSE_BRIDGE_CENTER_POINT = 195
    NOSE_CENTER_POINT = 1
    NOSE_LEFT_POINT = 102
    NOSE_RIGHT_POINT = 358
    LEFT_CHEEK_CENTER_POINT = 50
    LEFT_CHEEKBONE_POINT = 234
    LEFT_JAW_CORNER_POINT = 213
    LEFT_JAW_CENTER_POINT = 136
    RIGHT_CHEEK_CENTER_POINT = 280
    RIGHT_CHEEKBONE_POINT = 356
    RIGHT_JAW_CORNER_POINT = 433
    RIGHT_JAW_CENTER_POINT = 364
    LEFT_CHIN_POINT = 176
    RIGHT_CHIN_POINT = 400
    BOTTOM_CHIN_POINT = 152
    CHIN_CENTER_POINT = 199
    EYEBROW_MIDPOINT = 9
    EYE_MIDPOINT = 6
    CENTER_FOREHEAD_POINT = 10
    LEFT_TEMPLE_HAIRLINE_POINT = 162
    RIGHT_TEMPLE_HAIRLINE_POINT = 368
    LEFT_EYEBROW_RIGHT_POINT = 55
    LEFT_EYEBROW_TRANSITION_POINT = 63
    LEFT_EYEBROW_LEFT_POINT = 70
    RIGHT_EYEBROW_LEFT_POINT = 285
    RIGHT_EYEBROW_TRANSITION_POINT = 283
    RIGHT_EYEBROW_RIGHT_POINT = 276
    RIGHT_EYE_LEFT_POINT = 362
    RIGHT_EYE_RIGHT_POINT = 112
    RIGHT_EYE_BOTTOM_POINT = 145
    RIGHT_EYE_TOP_POINT = 158
    LEFT_EYE_LEFT_POINT = 33
    LEFT_EYE_RIGHT_POINT = 249
    LEFT_EYE_BOTTOM_POINT = 374
    LEFT_EYE_TOP_POINT = 158
    
    #GENERATES HTML FILE IN ./output/html/dotfinder.html TO HELP FIND DOTS
    @classmethod
    def generate_dot_html(self, face):
        face_mesher = mp.solutions.face_mesh
        face_mesh = face_mesher.FaceMesh()

        try:
            shutil.rmtree(f'{os.environ["FACEPROJECTDIR"]}/output/image-output')
        except:
            print("image-output does not exist")

        os.mkdir(f'{os.environ["FACEPROJECTDIR"]}/output/image-output')

        test = []
        offset = 0
        dot_num = 15

        while offset < dot_num:

            i = 0 + offset

            image = cv2.imread(f'{os.environ["FACEPROJECTDIR"]}/faces/{face.image}')
            height, width, nan = image.shape

            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            result = face_mesh.process(rgb_image)

            for landmarks in result.multi_face_landmarks:

                while i < 467:
                    
                    pt1 = landmarks.landmark[i]

                    x = int(pt1.x * width)
                    y = int(pt1.y * height)

                    color = (255, 255, 255)
                    cv2.circle(image, (x, y), 2, color, -1)

                    text = f'{i}'
                    org = (x - 2, y - 2)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_size = .3
                    thickness = 1
                    lineType = cv2.LINE_AA
                    cv2.putText(image, text, org, font, font_size, color, thickness, lineType)
                    
                    if i == 151:
                        x = int(pt1.x * width)
                        y = int(pt1.y * height) - 50

                        color = (255, 255, 255)
                        cv2.circle(image, (x, y), 2, color, -1)

                        text = f'{i}'
                        org = (x - 2, y - 2)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        font_size = .3
                        thickness = 1
                        lineType = cv2.LINE_AA
                        cv2.putText(image, "HERE", org, font, font_size, color, thickness, lineType)

                    i+= dot_num
                    test.append(i)


            cv2.imshow("Image", image)
            cv2.imwrite(f'{os.environ["FACEPROJECTDIR"]}/output/image-output/{offset}.jpeg', image)
            cv2.waitKey(50)
            offset+=1

        print(len(test))
        os.system(f'bash "$FACEPROJECTDIR/scripts/htmlgen.sh" > {os.environ["FACEPROJECTDIR"]}/output/html/dotfinder.html')
                
#    @classmethod
#    def generate_coordinates(self, face):
#
#            face_mesher = mp.solutions.face_mesh
#            face_mesh = face_mesher.FaceMesh()
#            result = face_mesh.process(face.rgb_image)
#
#            for landmarks in result.multi_face_landmarks:
#
#                for i in face.dot_names:
#
#                    pt1 = landmarks.landmark[i]
#                    
#                    x = int(pt1.x * face.width)
#                    y = int(pt1.y * face.height)
#                    coord_tuple = (x,y)
#                    face.coordinates[face.dot_names.get(i)] = coord_tuple
#
#                   color = (random.randint(1, 100), 255, random.randint(20, 255))
#                   cv2.circle(face.image, (x, y), 2, color, -1)

    @classmethod
    def draw_coordinates(self, face):
        for coord in face.coordinates:
            color = (random.randint(1, 100), 255, random.randint(20, 255))
            cv2.circle(face.image, (coord[0], coord[1]), 1, color, -1)
            print(coord)


    @classmethod
    def generate_coordinates(self, face):

            face_mesher = mp.solutions.face_mesh
            face_mesh = face_mesher.FaceMesh()
            result = face_mesh.process(face.rgb_image)

            for landmarks in result.multi_face_landmarks:
                    
                    face.MOUTH_LEFT_TUPLE = [int(landmarks.landmark[DotUtility.MOUTH_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_LEFT_POINT].y * face.height)]
                    face.MOUTH_TOP_TUPLE = [int(landmarks.landmark[DotUtility.MOUTH_TOP_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_TOP_POINT].y * face.height)]
                    face.MOUTH_BOTTOM_TUPLE = [int(landmarks.landmark[DotUtility.MOUTH_BOTTOM_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_BOTTOM_POINT].y * face.height)]
                    face.MOUTH_RIGHT_TUPLE = [int(landmarks.landmark[DotUtility.MOUTH_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_RIGHT_POINT].y * face.height)]
                    face.NOSE_BRIDGE_CENTER_TUPLE = [int(landmarks.landmark[DotUtility.NOSE_BRIDGE_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_BRIDGE_CENTER_POINT].y * face.height)]
                    face.NOSE_CENTER_TUPLE = [int(landmarks.landmark[DotUtility.NOSE_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_CENTER_POINT].y * face.height)]
                    face.NOSE_LEFT_TUPLE = [int(landmarks.landmark[DotUtility.NOSE_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_LEFT_POINT].y * face.height)]
                    face.NOSE_RIGHT_TUPLE = [int(landmarks.landmark[DotUtility.NOSE_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_RIGHT_POINT].y * face.height)]
                    face.LEFT_CHEEK_CENTER_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_CHEEK_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_CHEEK_CENTER_POINT].y * face.height)]
                    face.LEFT_CHEEKBONE_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_CHEEKBONE_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_CHEEKBONE_POINT].y * face.height)]
                    face.LEFT_JAW_CORNER_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_JAW_CORNER_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_JAW_CORNER_POINT].y * face.height)]
                    face.LEFT_JAW_CENTER_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_JAW_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_JAW_CENTER_POINT].y * face.height)]
                    face.RIGHT_CHEEK_CENTER_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_CHEEK_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_CHEEK_CENTER_POINT].y * face.height)]
                    face.RIGHT_CHEEKBONE_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_CHEEKBONE_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_CHEEKBONE_POINT].y * face.height)]
                    face.RIGHT_JAW_CORNER_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_JAW_CORNER_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_JAW_CORNER_POINT].y * face.height)]
                    face.RIGHT_JAW_CENTER_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_JAW_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_JAW_CENTER_POINT].y * face.height)]
                    face.LEFT_CHIN_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_CHIN_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_CHIN_POINT].y * face.height)]
                    face.RIGHT_CHIN_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_CHIN_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_CHIN_POINT].y * face.height)]
                    face.BOTTOM_CHIN_TUPLE = [int(landmarks.landmark[DotUtility.BOTTOM_CHIN_POINT].x * face.width), int(landmarks.landmark[DotUtility.BOTTOM_CHIN_POINT].y * face.height)]
                    face.CHIN_CENTER_TUPLE = [int(landmarks.landmark[DotUtility.CHIN_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.CHIN_CENTER_POINT].y * face.height)]
                    face.EYEBROW_MIDPOINT_TUPLE = [int(landmarks.landmark[DotUtility.EYEBROW_MIDPOINT].x * face.width), int(landmarks.landmark[DotUtility.EYEBROW_MIDPOINT].y * face.height)]
                    face.EYE_MIDPOINT_TUPLE = [int(landmarks.landmark[DotUtility.EYE_MIDPOINT].x * face.width), int(landmarks.landmark[DotUtility.EYE_MIDPOINT].y * face.height)]
                    face.CENTER_FOREHEAD_TUPLE = [int(landmarks.landmark[DotUtility.CENTER_FOREHEAD_POINT].x * face.width), int(landmarks.landmark[DotUtility.CENTER_FOREHEAD_POINT].y * face.height)]
                    face.LEFT_TEMPLE_HAIRLINE_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_TEMPLE_HAIRLINE_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_TEMPLE_HAIRLINE_POINT].y * face.height)]
                    face.RIGHT_TEMPLE_HAIRLINE_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_TEMPLE_HAIRLINE_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_TEMPLE_HAIRLINE_POINT].y * face.height)]
                    face.LEFT_EYEBROW_RIGHT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_EYEBROW_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYEBROW_RIGHT_POINT].y * face.height)]
                    face.LEFT_EYEBROW_TRANSITION_POINT_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_EYEBROW_TRANSITION_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYEBROW_TRANSITION_POINT].y * face.height)]
                    face.LEFT_EYEBROW_LEFT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_EYEBROW_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYEBROW_LEFT_POINT].y * face.height)]
                    face.RIGHT_EYEBROW_LEFT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_EYEBROW_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYEBROW_LEFT_POINT].y * face.height)]
                    face.RIGHT_EYEBROW_TRANSITION_POINT_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_EYEBROW_TRANSITION_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYEBROW_TRANSITION_POINT].y * face.height)]
                    face.RIGHT_EYEBROW_RIGHT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_EYEBROW_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYEBROW_RIGHT_POINT].y * face.height)]
                    face.RIGHT_EYE_LEFT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_EYE_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_LEFT_POINT].y * face.height)]
                    face.RIGHT_EYE_RIGHT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_EYE_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_RIGHT_POINT].y * face.height)]
                    face.RIGHT_EYE_BOTTOM_POINT_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_EYE_BOTTOM_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_BOTTOM_POINT].y * face.height)]
                    face.RIGHT_EYE_TOP_POINT_TUPLE = [int(landmarks.landmark[DotUtility.RIGHT_EYE_TOP_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_TOP_POINT].y * face.height)]
                    face.LEFT_EYE_LEFT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_EYE_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_LEFT_POINT].y * face.height)]
                    face.LEFT_EYE_RIGHT_POINT_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_EYE_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_RIGHT_POINT].y * face.height)]
                    face.LEFT_EYE_BOTTOM_POINT_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_EYE_BOTTOM_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_BOTTOM_POINT].y * face.height)]
                    face.LEFT_EYE_TOP_POINT_TUPLE = [int(landmarks.landmark[DotUtility.LEFT_EYE_TOP_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_TOP_POINT].y * face.height)]
    
                    
                    color = (random.randint(1, 100), 255, random.randint(20, 255))
                    cv2.circle(face.image, (face.LEFT_EYE_TOP_POINT_TUPLE[0], face.LEFT_EYE_TOP_POINT_TUPLE[1]), 1, color, -1)

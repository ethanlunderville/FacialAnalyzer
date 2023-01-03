import cv2
import dlib
import mediapipe as mp
import numpy as np
import random
import os
import shutil
from imutils import face_utils

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
    CHIN_CENTER_POINT = 199
    EYEBROW_MIDPOINT = 9
    EYE_MIDPOINT = 6
    CENTER_FOREHEAD_POINT = 10
    RIGHT_EYE_LEFT_POINT = 362
    RIGHT_EYE_RIGHT_POINT = 112
    RIGHT_EYE_BOTTOM_POINT = 145
    RIGHT_EYE_TOP_POINT = 158
    LEFT_EYE_LEFT_POINT = 33
    LEFT_EYE_RIGHT_POINT = 249
    LEFT_EYE_BOTTOM_POINT = 374
    LEFT_EYE_TOP_POINT = 158
    
    #GENERATES HTML FILE IN ./output/html/dotfinder.html TO HELP FIND DOTS FOR THE FACEMASHER LIBRARY
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
    @classmethod
    def draw_coordinates(self, face):
        color = (random.randint(1, 100), 255, random.randint(20, 255))
        for coord in face.coordinates:
            print(hex(id(coord)))
            cv2.circle(face.image, (coord[0], coord[1]), 1, color, -1)
            print(coord)
        for coord in face.FACE_OUTLINE:
            cv2.circle(face.image, (face.FACE_OUTLINE[coord][0], face.FACE_OUTLINE[coord][1]), 1, color, -1)
            print(coord)
    @classmethod
    def generate_coordinates(self, face):

            face_mesher = mp.solutions.face_mesh
            face_mesh = face_mesher.FaceMesh()
            result = face_mesh.process(face.rgb_image)

            landmarks = result.multi_face_landmarks[-1]
                
            face.MOUTH_LEFT_COORD = [int(landmarks.landmark[DotUtility.MOUTH_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_LEFT_POINT].y * face.height)]
            print(hex(id(face.MOUTH_LEFT_COORD)))
            face.MOUTH_TOP_COORD = [int(landmarks.landmark[DotUtility.MOUTH_TOP_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_TOP_POINT].y * face.height)]
            face.MOUTH_BOTTOM_COORD = [int(landmarks.landmark[DotUtility.MOUTH_BOTTOM_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_BOTTOM_POINT].y * face.height)]
            face.MOUTH_RIGHT_COORD = [int(landmarks.landmark[DotUtility.MOUTH_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.MOUTH_RIGHT_POINT].y * face.height)]
            face.NOSE_BRIDGE_CENTER_COORD = [int(landmarks.landmark[DotUtility.NOSE_BRIDGE_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_BRIDGE_CENTER_POINT].y * face.height)]
            face.NOSE_CENTER_COORD = [int(landmarks.landmark[DotUtility.NOSE_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_CENTER_POINT].y * face.height)]
            face.NOSE_LEFT_COORD = [int(landmarks.landmark[DotUtility.NOSE_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_LEFT_POINT].y * face.height)]
            face.NOSE_RIGHT_COORD = [int(landmarks.landmark[DotUtility.NOSE_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.NOSE_RIGHT_POINT].y * face.height)]
            face.CHIN_CENTER_COORD = [int(landmarks.landmark[DotUtility.CHIN_CENTER_POINT].x * face.width), int(landmarks.landmark[DotUtility.CHIN_CENTER_POINT].y * face.height)]
            face.EYEBROW_MIDPOINT_COORD = [int(landmarks.landmark[DotUtility.EYEBROW_MIDPOINT].x * face.width), int(landmarks.landmark[DotUtility.EYEBROW_MIDPOINT].y * face.height)]
            face.EYE_MIDPOINT_COORD = [int(landmarks.landmark[DotUtility.EYE_MIDPOINT].x * face.width), int(landmarks.landmark[DotUtility.EYE_MIDPOINT].y * face.height)]
            face.CENTER_FOREHEAD_COORD = [int(landmarks.landmark[DotUtility.CENTER_FOREHEAD_POINT].x * face.width), int(landmarks.landmark[DotUtility.CENTER_FOREHEAD_POINT].y * face.height)]
            face.RIGHT_EYE_LEFT_POINT_COORD = [int(landmarks.landmark[DotUtility.RIGHT_EYE_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_LEFT_POINT].y * face.height)]
            face.RIGHT_EYE_RIGHT_POINT_COORD = [int(landmarks.landmark[DotUtility.RIGHT_EYE_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_RIGHT_POINT].y * face.height)]
            face.RIGHT_EYE_BOTTOM_POINT_COORD = [int(landmarks.landmark[DotUtility.RIGHT_EYE_BOTTOM_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_BOTTOM_POINT].y * face.height)]
            face.RIGHT_EYE_TOP_POINT_COORD = [int(landmarks.landmark[DotUtility.RIGHT_EYE_TOP_POINT].x * face.width), int(landmarks.landmark[DotUtility.RIGHT_EYE_TOP_POINT].y * face.height)]
            face.LEFT_EYE_LEFT_POINT_COORD = [int(landmarks.landmark[DotUtility.LEFT_EYE_LEFT_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_LEFT_POINT].y * face.height)]
            face.LEFT_EYE_RIGHT_POINT_COORD = [int(landmarks.landmark[DotUtility.LEFT_EYE_RIGHT_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_RIGHT_POINT].y * face.height)]
            face.LEFT_EYE_BOTTOM_POINT_COORD = [int(landmarks.landmark[DotUtility.LEFT_EYE_BOTTOM_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_BOTTOM_POINT].y * face.height)]
            face.LEFT_EYE_TOP_POINT_COORD = [int(landmarks.landmark[DotUtility.LEFT_EYE_TOP_POINT].x * face.width), int(landmarks.landmark[DotUtility.LEFT_EYE_TOP_POINT].y * face.height)]
    
            image = face.image
            detector = dlib.get_frontal_face_detector()
            model_68 = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
            model_81 = dlib.shape_predictor('./shape_predictor_81_face_landmarks.dat')

            faces = detector(face.image, 1)

            if len(faces) == 1:

                bottom_face_dots = face_utils.shape_to_np(model_68(image, faces[0]))
                # Get 81 landmark points
                top_face_dots = face_utils.shape_to_np(model_81(image, faces[0]))
                face_dots = np.concatenate((bottom_face_dots, top_face_dots[68:]))

                x,y,x2,y2 = (face_dots[69,0]-10, face_dots[68,1], face_dots[80,0]+10, face_dots[23, 1])
                foreheadRegion = image[y:y2,x:x2]
                foreheadHeight = foreheadRegion.shape[0]

                # FOREHEAD ESTIMATION
                face_dots[70,1] -= foreheadHeight * 0.2
                face_dots[71,1] -= foreheadHeight * 0.3
                face_dots[80,1] -= foreheadHeight * 0.2

                bottom_face = face_dots[0:18]
                left_brow = face_dots[17:22]
                right_brow = face_dots[22:27]
                top_face = face_dots[68:81]

                dlib_dots = face_dots

                for i in range(bottom_face.__len__()):
                    face.FACE_OUTLINE[i] = dlib_dots[i]
                for i in range(top_face.__len__()):
                    face.FACE_OUTLINE[i+68] = dlib_dots[i+68]

                face.LEFT_BROW_1_COORD = left_brow[0]
                face.LEFT_BROW_2_COORD = left_brow[1]
                face.LEFT_BROW_3_COORD = left_brow[2]
                face.LEFT_BROW_4_COORD = left_brow[3]
                face.LEFT_BROW_5_COORD = left_brow[4]

                face.RIGHT_BROW_1_COORD = right_brow[0]
                face.RIGHT_BROW_2_COORD = right_brow[1]
                face.RIGHT_BROW_3_COORD = right_brow[2]
                face.RIGHT_BROW_4_COORD = right_brow[3]
                face.RIGHT_BROW_5_COORD = right_brow[4]
            
            else:
                return None                          
    @classmethod
    def tester(self, face):

        image = face.image
        detector = dlib.get_frontal_face_detector()
        model_68 = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
        model_81 = dlib.shape_predictor('./shape_predictor_81_face_landmarks.dat')

        faces = detector(face.image, 1)

        if len(faces) == 1:

            bottom_face_dots = face_utils.shape_to_np(model_68(image, faces[0]))
            # Get 81 landmark points
            top_face_dots = face_utils.shape_to_np(model_81(image, faces[0]))
            face_dots = np.concatenate((bottom_face_dots, top_face_dots[68:]))
            
            x,y,x2,y2 = (face_dots[69,0]-10, face_dots[68,1], face_dots[80,0]+10, face_dots[23, 1])
            foreheadRegion = image[y:y2,x:x2]
            foreheadHeight = foreheadRegion.shape[0]
            
            # FOREHEAD ESTIMATION
            face_dots[70,1] -= foreheadHeight * 0.2
            face_dots[71,1] -= foreheadHeight * 0.3
            face_dots[80,1] -= foreheadHeight * 0.2

            bottom_face = face_dots[0:18]
            left_brow = face_dots[17:22]
            right_brow = face_dots[22:27]
            top_face = face_dots[68:81]

            dlib_dots = face_dots

            for i in range(bottom_face.__len__()):
                face.FACE_OUTLINE[i] = dlib_dots[i]
            for i in range(top_face.__len__()):
                face.FACE_OUTLINE[i+68] = dlib_dots[i+68]

            face.LEFT_BROW_1_COORD = left_brow[0]
            face.LEFT_BROW_2_COORD = left_brow[1]
            face.LEFT_BROW_3_COORD = left_brow[2]
            face.LEFT_BROW_4_COORD = left_brow[3]
            face.LEFT_BROW_5_COORD = left_brow[4]

            face.RIGHT_BROW_1_COORD = right_brow[0]
            face.RIGHT_BROW_2_COORD = right_brow[1]
            face.RIGHT_BROW_3_COORD = right_brow[2]
            face.RIGHT_BROW_4_COORD = right_brow[3]
            face.RIGHT_BROW_5_COORD = right_brow[4]

            
            for i in range(dlib_dots.__len__()):
                # POINTS NEEDED FOR BOTTOM FACE ANF BROWS
                x,y = dlib_dots[i]
                print(i)
                image = cv2.circle(image, (x,y), 1, (255,255,255), -1)
                text = f'{i}'
                org = (x - 2, y - 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_size = .3
                thickness = 1
                lineType = cv2.LINE_AA
                cv2.putText(image, text, org, font, font_size, (255,255,255), thickness, lineType)

            cv2.imshow("Image", image)
            cv2.waitKey(0)
            
        else:
            return None

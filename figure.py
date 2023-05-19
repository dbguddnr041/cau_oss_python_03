"""
모듈의 설명은 최상단에 위치해야합니다.
보통 LICENSE에 대해 기술하곤 합니다.

figure 모듈은 글미과 관련된 함수 및 클래스를 제공하는 모듈입니다.
line class를 이용하여 선의 길이를 설정/참조를 수행하며
area_square, area_circle, area_regular_triangle 함수로
각각 정사각형, 원, 정삼각형의 넓이를 반환합니다.
"""

import math
class line:

    __length = 0
    def __init__(self, length):
        self.__length = length

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length
    
def area_square(length):
        return length * length
    
def area_circle(length):
        return length & length * math.pi
    
def area_regular_triangle(length):
        return length * length * math.sqrt(3)/4
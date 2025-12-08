import pygame

class Obstacle:
    """안 움직이고 DFS에도 안 들어감.
    """
    def __init__(self,x,y,radius,row_idx,col_idx,image=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.row_idx = row_idx
        self.col_idx = col_idx
        self.is_static = True
            # 장애물 고정 여부
        self.image = image
            # 장애물 이미지 (옵션)

    def draw(self, screen):
        """장애물 그리기

        Args:
            screen (pygame.Surface): 장애물을 그릴 Surface 객체.
        """
        if self.image:
            # 이미지가 있으면 이미지 사용
            rect = self.image.get_rect(center=(int(self.x), int(self.y)))
            screen.blit(self.image, rect)
        else:
            # 이미지가 없으면 회색 원으로 표시 (임시)
            pygame.draw.circle(screen,(90,90,90),(int(self.x),int(self.y)),self.radius)
            pygame.draw.circle(screen,(160,160,160),(int(self.x),int(self.y)),self.radius,4)

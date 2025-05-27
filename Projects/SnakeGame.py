import pygame
import sys
import random
import time

# --- 常量 ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 102)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

PLAYER_COLOR = GREEN
AI_COLORS = [BLUE, PURPLE, ORANGE]
FOOD_COLOR = RED

# 方向向量
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 速度 (数值越小越快，表示移动间隔时间)
BASE_MOVE_INTERVAL = 0.15  # 基础移动间隔 (秒)
ACCELERATED_MOVE_INTERVAL = 0.05 # 加速时移动间隔
AI_MOVE_INTERVAL = 0.20 # AI 移动间隔

# --- 辅助函数 ---
def draw_grid(surface):
    """绘制背景网格(可选)"""
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(surface, GRAY, (0, y), (SCREEN_WIDTH, y))
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(surface, GRAY, (x, 0), (x, SCREEN_HEIGHT))

def get_random_position(occupied_positions):
    """获取一个不在占用位置列表中的随机网格位置"""
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in occupied_positions:
            return pos

# --- 蛇类 ---
class Snake:
    def __init__(self, start_pos, start_dir, color, is_ai=False):
        self.body = [start_pos]
        self.direction = start_dir
        self.next_direction = start_dir # 缓冲下一个方向，防止180度掉头
        self.color = color
        self.is_ai = is_ai
        self.alive = True
        self.last_move_time = time.time()
        self.move_interval = AI_MOVE_INTERVAL if is_ai else BASE_MOVE_INTERVAL
        self.ate_food_in_last_move = False # 用于AI判断是否刚吃完

    def get_head_position(self):
        return self.body[0]

    def change_direction(self, new_direction):
        """改变蛇的下一个移动方向，防止180度掉头"""
        # 检查是否是反方向
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.next_direction = new_direction

    def move(self, food_position, all_snake_bodies):
        """移动蛇，并返回是否吃到食物"""
        if not self.alive:
            return False

        current_time = time.time()
        # AI 和非加速状态下的玩家使用固定的时间间隔
        # 加速状态由主循环控制 move_interval
        if current_time - self.last_move_time < self.move_interval and not self.is_ai:
             # 如果是玩家且未到移动时间，则不移动 (加速状态由外部调整interval)
             return False
        elif self.is_ai and current_time - self.last_move_time < self.move_interval:
             # 如果是AI且未到移动时间，则不移动
             return False


        self.last_move_time = current_time
        self.direction = self.next_direction # 更新实际方向

        head = self.get_head_position()
        new_head = ((head[0] + self.direction[0]) % GRID_WIDTH,
                    (head[1] + self.direction[1]) % GRID_HEIGHT) # 环绕边界

        # 检查碰撞 (墙壁 - 已通过取模处理，自身，其他蛇)
        if new_head in self.body[1:]: # 撞到自己
            self.alive = False
            return False
        # 在主循环中检查与其他蛇的碰撞

        # 移动
        self.body.insert(0, new_head)
        self.ate_food_in_last_move = False

        # 检查是否吃到食物
        if new_head == food_position:
            self.ate_food_in_last_move = True
            return True # 吃到了食物，不移除尾巴
        else:
            self.body.pop() # 没吃到食物，移除尾巴
            return False

    def ai_decide_direction(self, food_position, all_snake_bodies_excluding_self):
        """简单的AI决策逻辑：优先向食物移动，尝试避开障碍物"""
        if not self.alive:
            return

        head = self.get_head_position()
        possible_moves = {} # {direction: distance_to_food}

        # --- 1. 计算所有可行方向到食物的距离 ---
        for move_dir in [UP, DOWN, LEFT, RIGHT]:
            # 排除180度转弯
            if (move_dir[0] * -1, move_dir[1] * -1) == self.direction:
                continue

            next_head_potential = ((head[0] + move_dir[0]) % GRID_WIDTH,
                                   (head[1] + move_dir[1]) % GRID_HEIGHT)

            # 检查潜在的下一步是否会撞到自己或其他蛇
            if next_head_potential in self.body or \
               next_head_potential in all_snake_bodies_excluding_self:
                continue # 这个方向不安全，不考虑

            # 计算到食物的曼哈顿距离
            distance = abs(next_head_potential[0] - food_position[0]) + \
                       abs(next_head_potential[1] - food_position[1])
            possible_moves[move_dir] = distance

        # --- 2. 选择最佳方向 ---
        if not possible_moves:
            # 如果没有安全的方向可选 (可能被包围)，尝试继续当前方向（如果安全）
            next_head_potential = ((head[0] + self.direction[0]) % GRID_WIDTH,
                                   (head[1] + self.direction[1]) % GRID_HEIGHT)
            if next_head_potential not in self.body and \
               next_head_potential not in all_snake_bodies_excluding_self:
                 self.change_direction(self.direction) # 保持原方向
            else:
                # 实在没办法了，随机选一个非反方向 (可能会撞)
                valid_dirs = [d for d in [UP, DOWN, LEFT, RIGHT] if (d[0] * -1, d[1] * -1) != self.direction]
                if valid_dirs:
                     self.change_direction(random.choice(valid_dirs))
                # else: 保持当前方向，下一帧可能会死

        else:
            # 选择离食物最近的安全方向
            best_direction = min(possible_moves, key=possible_moves.get)
            self.change_direction(best_direction)

            # --- 增加一点随机性：偶尔不走最优路径 ---
            # (如果刚吃完食物，或者随机概率发生)
            if self.ate_food_in_last_move or random.random() < 0.1:
                 safe_non_optimal_moves = [d for d in possible_moves if d != best_direction]
                 if safe_non_optimal_moves and random.random() < 0.3: # 有30%概率走次优
                     self.change_direction(random.choice(safe_non_optimal_moves))


    def draw(self, surface):
        """绘制蛇"""
        if not self.alive:
            # 可以选择画一个不同的标记表示死亡的蛇
            # for segment in self.body:
            #     r = pygame.Rect((segment[0] * GRID_SIZE, segment[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            #     pygame.draw.rect(surface, GRAY, r) # 用灰色表示死亡
            return

        for i, segment in enumerate(self.body):
            r = pygame.Rect((segment[0] * GRID_SIZE, segment[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            # 让蛇头颜色稍微亮一点
            segment_color = tuple(min(c + 40, 255) for c in self.color) if i == 0 else self.color
            pygame.draw.rect(surface, segment_color, r)
            pygame.draw.rect(surface, BLACK, r, 1) # 添加黑色边框

# --- 游戏主类 ---
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("贪吃蛇大战 (Pygame)")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 25) # 使用系统字体
        self.score = 0
        self.game_over = False
        self.accelerating = False

        # 获取所有蛇可能初始占用的位置，避免重叠和食物生成在蛇身上
        occupied = set()

        # 创建玩家蛇
        player_start_pos = (GRID_WIDTH // 4, GRID_HEIGHT // 2)
        occupied.add(player_start_pos)
        self.player_snake = Snake(player_start_pos, RIGHT, PLAYER_COLOR)

        # 创建AI蛇
        self.ai_snakes = []
        ai_start_positions = [
            (GRID_WIDTH * 3 // 4, GRID_HEIGHT // 4),
            (GRID_WIDTH * 3 // 4, GRID_HEIGHT // 2),
            (GRID_WIDTH * 3 // 4, GRID_HEIGHT * 3 // 4)
        ]
        ai_start_dirs = [LEFT, LEFT, LEFT] # 让AI开始向左移动

        for i in range(3):
            pos = ai_start_positions[i]
            if pos not in occupied:
                 ai_snake = Snake(pos, ai_start_dirs[i], AI_COLORS[i % len(AI_COLORS)], is_ai=True)
                 self.ai_snakes.append(ai_snake)
                 occupied.add(pos)
            # (如果起始位置已被占用，则这条AI蛇不会被创建)

        # 获取所有蛇的身体位置
        all_bodies = set(self.player_snake.body)
        for ai in self.ai_snakes:
            all_bodies.update(ai.body)

        # 创建食物
        self.food_position = get_random_position(all_bodies)


    def run(self):
        """游戏主循环"""
        while not self.game_over:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(60) # 限制最大帧率

        self.show_game_over_screen()

    def handle_input(self):
        """处理用户输入"""
        self.accelerating = False # 每帧开始时重置加速状态
        keys_pressed = pygame.key.get_pressed() # 获取当前按下的所有键

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # elif event.type == pygame.KEYDOWN: # 处理方向改变
            #     if event.key == pygame.K_UP or event.key == pygame.K_w:
            #         self.player_snake.change_direction(UP)
            #     elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            #         self.player_snake.change_direction(DOWN)
            #     elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            #         self.player_snake.change_direction(LEFT)
            #     elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            #         self.player_snake.change_direction(RIGHT)

        # --- 使用 get_pressed 实现方向改变和加速 ---
        new_dir = None
        if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            new_dir = UP
        elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
            new_dir = DOWN
        elif keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            new_dir = LEFT
        elif keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            new_dir = RIGHT

        if new_dir:
            self.player_snake.change_direction(new_dir)
            # 如果按下的方向键与当前蛇行进方向一致，则加速
            if new_dir == self.player_snake.direction:
                self.accelerating = True

        # 根据是否加速调整玩家蛇的移动间隔
        if self.accelerating:
            self.player_snake.move_interval = ACCELERATED_MOVE_INTERVAL
        else:
            self.player_snake.move_interval = BASE_MOVE_INTERVAL


    def update(self):
        """更新游戏状态"""
        if not self.player_snake.alive:
            self.game_over = True
            return

        # --- 获取所有蛇的位置信息 (用于碰撞检测和AI决策) ---
        all_snake_bodies = set(self.player_snake.body)
        all_ai_bodies = set()
        for ai in self.ai_snakes:
            if ai.alive:
                all_snake_bodies.update(ai.body)
                all_ai_bodies.update(ai.body)


        # --- 移动玩家蛇 ---
        player_ate = self.player_snake.move(self.food_position, all_ai_bodies) # 玩家只检查与AI的碰撞

        if not self.player_snake.alive: # 移动后检查是否死亡 (撞自己)
             self.game_over = True
             return

        # 检查玩家是否撞到AI
        if self.player_snake.get_head_position() in all_ai_bodies:
            self.player_snake.alive = False
            self.game_over = True
            return

        # --- 移动AI蛇 ---
        active_ai_snakes = []
        for ai in self.ai_snakes:
            if not ai.alive:
                continue

            # AI 决策
            other_bodies_for_ai = set(self.player_snake.body) # AI需要考虑玩家蛇
            for other_ai in self.ai_snakes:
                 if other_ai is not ai and other_ai.alive:
                      other_bodies_for_ai.update(other_ai.body)
            ai.ai_decide_direction(self.food_position, other_bodies_for_ai)

            # AI 移动
            ai_ate = ai.move(self.food_position, other_bodies_for_ai) # AI也检查与其他所有蛇的碰撞

            # AI 死亡检查 (撞墙已处理，撞自己，撞其他蛇包括玩家)
            ai_head = ai.get_head_position()
            if not ai.alive or ai_head in other_bodies_for_ai:
                ai.alive = False # AI死亡后不再活动
            else:
                active_ai_snakes.append(ai) # 记录仍然存活的AI

            # 如果AI吃了食物
            if ai_ate:
                # 食物被AI吃了，也需要重新生成
                all_bodies_now = set(self.player_snake.body)
                for a in active_ai_snakes: # 使用更新后的存活AI列表
                     all_bodies_now.update(a.body)
                self.food_position = get_random_position(all_bodies_now)
                # 注意：这里AI吃食物不加分

        self.ai_snakes = active_ai_snakes # 更新存活的AI列表

        # --- 处理玩家吃食物 ---
        if player_ate:
            self.score += 1
            # 重新生成食物，需要考虑所有当前蛇的位置
            all_bodies_now = set(self.player_snake.body)
            for ai in self.ai_snakes: # 使用最新的存活AI列表
                all_bodies_now.update(ai.body)
            self.food_position = get_random_position(all_bodies_now)


    def render(self):
        """渲染游戏画面"""
        self.screen.fill(BLACK) # 黑色背景
        # draw_grid(self.screen) # 可选：绘制网格

        # 绘制所有蛇
        self.player_snake.draw(self.screen)
        for ai in self.ai_snakes:
            ai.draw(self.screen)

        # 绘制食物
        food_rect = pygame.Rect((self.food_position[0] * GRID_SIZE, self.food_position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(self.screen, FOOD_COLOR, food_rect)
        pygame.draw.rect(self.screen, WHITE, food_rect, 1) # 食物边框

        # 绘制分数
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (5, 5))

        # 如果加速，显示提示
        if self.accelerating:
             accel_text = self.font.render("Accelerating!", True, YELLOW)
             self.screen.blit(accel_text, (SCREEN_WIDTH - accel_text.get_width() - 5, 5))


        pygame.display.flip() # 更新整个屏幕

    def show_game_over_screen(self):
        """显示游戏结束画面"""
        while True:
            self.screen.fill(BLACK)
            title_font = pygame.font.SysFont("Arial", 50)
            info_font = pygame.font.SysFont("Arial", 30)

            game_over_text = title_font.render("GAME OVER", True, RED)
            score_text = info_font.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = info_font.render("Press R to Restart or Q to Quit", True, WHITE)

            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))

            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(score_text, score_rect)
            self.screen.blit(restart_text, restart_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_r:
                        # --- 重置游戏 ---
                        new_game = Game()
                        new_game.run()
                        # run() 结束后会再次进入 show_game_over_screen
                        # 需要退出当前这个 game over 循环
                        return # 退出当前的 show_game_over_screen


# --- 启动游戏 ---
if __name__ == "__main__":
    game = Game()
    game.run()
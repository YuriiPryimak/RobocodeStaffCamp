import tkinter as tk
import random

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Гра з бонусами та антибонусами")

        self.canvas = tk.Canvas(root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.score = 0
        self.game_over = False

        self.character = self.canvas.create_rectangle(290, 370, 310, 390, fill="blue")
        self.bonuses = [self.create_bonus()]
        self.antibonuses = [self.create_antibonus()]

        self.score_label = tk.Label(root, text=f"Бал: {self.score}", font=("Helvetica", 14))
        self.score_label.pack()

        self.root.bind("<KeyPress-Left>", self.move_left)
        self.root.bind("<KeyPress-Right>", self.move_right)

        self.update_game()

    def create_bonus(self):
        x = random.randint(10, 590)
        y = -20  # Початкова позиція бонусу над екраном
        return self.canvas.create_oval(x, y, x+20, y+20, fill="green")

    def create_antibonus(self):
        x = random.randint(10, 590)
        y = -20  # Початкова позиція антибонусу над екраном
        return self.canvas.create_oval(x, y, x+20, y+20, fill="red")

    def move_left(self, event):
        if not self.game_over:
            coords = self.canvas.coords(self.character)
            if coords[0] > 0:  # Перевірка межі лівої сторони
                self.canvas.move(self.character, -20, 0)

    def move_right(self, event):
        if not self.game_over:
            coords = self.canvas.coords(self.character)
            if coords[2] < 600:  # Перевірка межі правої сторони
                self.canvas.move(self.character, 20, 0)

    def check_collision(self, item):
        char_coords = self.canvas.coords(self.character)
        item_coords = self.canvas.coords(item)
        overlap = self.canvas.find_overlapping(*char_coords)
        return item in overlap

    def update_game(self):
        if not self.game_over:
            for bonus in self.bonuses:
                self.canvas.move(bonus, 0, 5)
                if self.check_collision(bonus):
                    self.canvas.delete(bonus)
                    self.bonuses.remove(bonus)
                    self.bonuses.append(self.create_bonus())
                    self.score += 1
                    self.score_label.config(text=f"Бал: {self.score}")
                elif self.canvas.coords(bonus)[1] > 400:  # Видалити бонус, якщо він вийшов за екран
                    self.canvas.delete(bonus)
                    self.bonuses.remove(bonus)
                    self.bonuses.append(self.create_bonus())

            for antibonus in self.antibonuses:
                self.canvas.move(antibonus, 0, 5)
                if self.check_collision(antibonus):
                    self.canvas.delete(antibonus)
                    self.antibonuses.remove(antibonus)
                    self.game_over = True
                    self.score_label.config(text="Гра завершена!")
                    self.root.after(2000, self.restart_game)
                elif self.canvas.coords(antibonus)[1] > 400:  # Видалити антибонус, якщо він вийшов за екран
                    self.canvas.delete(antibonus)
                    self.antibonuses.remove(antibonus)
                    self.antibonuses.append(self.create_antibonus())

            self.root.after(50, self.update_game)

    def restart_game(self):
        self.canvas.delete("all")
        self.score = 0
        self.game_over = False
        self.character = self.canvas.create_rectangle(290, 370, 310, 390, fill="blue")
        self.bonuses = [self.create_bonus()]
        self.antibonuses = [self.create_antibonus()]
        self.score_label.config(text=f"Бал: {self.score}")
        self.update_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

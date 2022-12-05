"""
# USING NUMPY
import numpy as np
import pygame as pg

# setting
res = width, height = 640, 480
offset = np.array([1.3 * width, height]) // 2
max_iter = 30
zoom = 2.2 / height

# texture
texture = pg.image.load('texture.jpeg')
texture_size = min(texture.get_size()) - 1
texture_array = pg.surfarray.array3d(texture)


class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((width, height, 3), [0, 0, 0], dtype=np.uint8)
        self.x = np.linspace(0, width, num=width, dtype=np.float32)
        self.y = np.linspace(0, height, num=height, dtype=np.float32)

    def render(self):
        x = (self.x - offset[0]) * zoom
        y = (self.y - offset[1]) * zoom
        c = x + 1j * y[:, None]

        num_iter = np.full(c.shape, max_iter)
        z = np.empty(c.shape, np.complex64)
        for i in range(max_iter):
            mask = (num_iter == max_iter)
            z[mask] = z[mask] ** 2 + c[mask]
            num_iter[mask & (z.real**2 + z.imag**2 > 4.0)] = i + 1

        col = (num_iter.T * texture_size / max_iter).astype(np.uint8)
        self.screen_array = texture_array[col, col]

    def update(self):
        self.render()

    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res, pg.SCALED)  # позволит аппаратно увеличить изображение по разрешения экр.
        self.clock = pg.time.Clock()
        self.fractal = Fractal(self)

    def run(self):
        while True:
            self.screen.fill('black')
            self.fractal.run()
            pg.display.flip()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick()
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')


if __name__ == '__main__':
    app = App()
    app.run()




#USING NUMBA
import numba as numba
import numpy as np
import pygame as pg

# setting
res = width, height = 640, 480
offset = np.array([1.3 * width, height]) // 2
max_iter = 30
zoom = 2.2 / height

# texture
texture = pg.image.load('texture.jpeg')
texture_size = min(texture.get_size()) - 1
texture_array = pg.surfarray.array3d(texture)


class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((width, height, 3), [0, 0, 0], dtype=np.uint8)
        self.x = np.linspace(0, width, num=width, dtype=np.float32)
        self.y = np.linspace(0, height, num=height, dtype=np.float32)

    @staticmethod
    @numba.njit(fastmath=True, parallel=True)
    def render(screen_array):
        for x in numba.prange(width):
            for y in range(height):
                c = (x - offset[0]) * zoom + 1j * (y - offset[1]) * zoom
                z = 0
                num_iter = 0
                for i in range(max_iter):
                    z = z ** 2 + c
                    if z.real ** 2 + z.imag ** 2 > 4:
                        break
                    num_iter += 1
                col = int(texture_size * num_iter / max_iter)
                screen_array[x, y] = texture_array[col, col]
        return screen_array

    def update(self):
        self.screen_array = self.render(self.screen_array)

    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res, pg.SCALED)  # позволит аппаратно увеличить изображение по разрешения экр.
        self.clock = pg.time.Clock()
        self.fractal = Fractal(self)

    def run(self):
        while True:
            self.screen.fill('black')
            self.fractal.run()
            pg.display.flip()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick()
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')


if __name__ == '__main__':
    app = App()
    app.run()





#USING TAICHI
import numpy as np
import pygame as pg
import taichi as taichi

# setting
res = width, height = 640, 480
offset = np.array([1.3 * width, height]) // 2
max_iter = 30
zoom = 2.2 / height

# texture
texture = pg.image.load('texture.jpeg')
texture_size = min(texture.get_size()) - 1
texture_array = pg.surfarray.array3d(texture)


@taichi.data_oriented
class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((width, height, 3), [0, 0, 0], dtype=np.uint8)
        self.x = np.linspace(0, width, num=width, dtype=np.float32)
        self.y = np.linspace(0, height, num=height, dtype=np.float32)
        # setting taichi
        taichi.init(arch=taichi.cpu)
        # taichi fields
        self.screen_field = taichi.Vector.field(3, taichi.uint8, (width, height))
        self.texture_field = taichi.Vector.field(3, taichi.uint8, texture.get_size())
        self.texture_field.from_numpy(texture_array)

    @taichi.kernel
    def render(self):
        for x, y in self.screen_field:#parall
                c = taichi.Vector([(x-offset[0])*zoom, (y - offset[1])*zoom])
                z = taichi.Vector([0.0, 0.0])
                num_iter = 0
                for i in range(max_iter):
                    z = taichi.Vector([(z.x**2 - z.y**2+c.x), (2*z.x*z.y+c.y)])
                    if z.dot(z) > 4:
                        break
                    num_iter += 1
                col = int(texture_size * num_iter / max_iter)
                self.screen_field[x, y] = self.texture_field[col, col]

    def update(self):
        self.render()
        self.screen_array = self.screen_field.to_numpy()

    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res, pg.SCALED)  # позволит аппаратно увеличить изображение по разрешения экр.
        self.clock = pg.time.Clock()
        self.fractal = Fractal(self)

    def run(self):
        while True:
            self.screen.fill('black')
            self.fractal.run()
            pg.display.flip()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick()
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')


if __name__ == '__main__':
    app = App()
    app.run()



#USING OPENGL
import numpy as np
import pygame as pg
import taichi as taichi

# setting
res = width, height = 1920, 1080
offset = np.array([1.3 * width, height]) // 2
max_iter = 30
zoom = 2.2 / height

# texture
texture = pg.image.load('texture.jpeg')
texture_size = min(texture.get_size()) - 1
texture_array = pg.surfarray.array3d(texture).astype(dtype=np.uint32)


@taichi.data_oriented
class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((width, height, 3), [0, 0, 0], dtype=np.uint32)
        self.x = np.linspace(0, width, num=width, dtype=np.float32)
        self.y = np.linspace(0, height, num=height, dtype=np.float32)
        # setting taichi
        taichi.init(arch=taichi.opengl)
        # taichi fields
        self.screen_field = taichi.Vector.field(3, taichi.uint32, (width, height))
        self.texture_field = taichi.Vector.field(3, taichi.uint32, texture.get_size())
        self.texture_field.from_numpy(texture_array)

    @taichi.kernel
    def render(self):
        for x, y in self.screen_field:#parall
                c = taichi.Vector([(x-offset[0])*zoom, (y - offset[1])*zoom])
                z = taichi.Vector([0.0, 0.0])
                num_iter = 0
                for i in range(max_iter):
                    z = taichi.Vector([(z.x**2 - z.y**2+c.x), (2*z.x*z.y+c.y)])
                    if z.dot(z) > 4:
                        break
                    num_iter += 1
                col = int(texture_size * num_iter / max_iter)
                self.screen_field[x, y] = self.texture_field[col, col]

    def update(self):
        self.render()
        self.screen_array = self.screen_field.to_numpy()

    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res, pg.SCALED)  # позволит аппаратно увеличить изображение по разрешения экр.
        self.clock = pg.time.Clock()
        self.fractal = Fractal(self)

    def run(self):
        while True:
            self.screen.fill('black')
            self.fractal.run()
            pg.display.flip()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick()
            pg.display.set_caption(f'FPS: {self.clock.get_fps()}')


if __name__ == '__main__':
    app = App()
    app.run()
"""



import pygame as pg
import numpy as np
import taichi as ti

# settings
res = width, height = 800, 450 # with modern video card with CUDA support - increase res '1600, 900' and set 'ti.init(arch=ti.cuda)'
offset = np.array([1.3 * width, height]) // 2
# texture
texture = pg.image.load('texture_3.jpg')
texture_size = min(texture.get_size()) - 1
texture_array = pg.surfarray.array3d(texture).astype(dtype=np.uint32)


@ti.data_oriented
class Fractal:
    def __init__(self, app):
        self.app = app
        self.screen_array = np.full((width, height, 3), [0, 0, 0], dtype=np.uint32)
        # taichi architecture, you can use ti.cpu, ti.cuda, ti.opengl, ti.vulkan, ti.metal
        ti.init(arch=ti.cpu)
        # taichi fields
        self.screen_field = ti.Vector.field(3, ti.uint32, (width, height))
        self.texture_field = ti.Vector.field(3, ti.uint32, texture.get_size())
        self.texture_field.from_numpy(texture_array)
        # control settings
        self.vel = 0.01
        self.zoom, self.scale = 2.2 / height, 0.993
        self.increment = ti.Vector([0.0, 0.0])
        self.max_iter, self.max_iter_limit = 30, 5500
        # delta_time
        self.app_speed = 1 / 4000
        self.prev_time = pg.time.get_ticks()

    def delta_time(self):
        time_now = pg.time.get_ticks() - self.prev_time
        self.prev_time = time_now
        return time_now * self.app_speed

    @ti.kernel
    def render(self, max_iter: ti.int32, zoom: ti.float32, dx: ti.float32, dy: ti.float32):
        for x, y in self.screen_field: # parallelization loop
            c = ti.Vector([(x - offset[0]) * zoom - dx, (y - offset[1]) * zoom - dy])
            z = ti.Vector([0.0, 0.0])
            num_iter = 0
            for i in range(max_iter):
                z = ti.Vector([(z.x ** 2 - z.y ** 2 + c.x), (2 * z.x * z.y + c.y)])
                if z.dot(z) > 4:
                    break
                num_iter += 1
            col = int(texture_size * num_iter / max_iter)
            self.screen_field[x, y] = self.texture_field[col, col]

    def control(self):
        pressed_key = pg.key.get_pressed()
        dt = self.delta_time()
        # movement
        if pressed_key[pg.K_a]:
            self.increment[0] += self.vel * dt
        if pressed_key[pg.K_d]:
            self.increment[0] -= self.vel * dt
        if pressed_key[pg.K_w]:
            self.increment[1] += self.vel * dt
        if pressed_key[pg.K_s]:
            self.increment[1] -= self.vel * dt

        # stable zoom and movement
        if pressed_key[pg.K_UP] or pressed_key[pg.K_DOWN]:
            inv_scale = 2 - self.scale
            if pressed_key[pg.K_UP]:
                self.zoom *= self.scale
                self.vel *= self.scale
            if pressed_key[pg.K_DOWN]:
                self.zoom *= inv_scale
                self.vel *= inv_scale

        # mandelbrot resolution
        if pressed_key[pg.K_LEFT]:
            self.max_iter -= 1
        if pressed_key[pg.K_RIGHT]:
            self.max_iter += 1
        self.max_iter = min(max(self.max_iter, 2), self.max_iter_limit)

    def update(self):
        self.control()
        self.render(self.max_iter, self.zoom, self.increment[0], self.increment[1])
        self.screen_array = self.screen_field.to_numpy()

    def draw(self):
        pg.surfarray.blit_array(self.app.screen, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class App:
    def __init__(self):
        self.screen = pg.display.set_mode(res, pg.SCALED)
        self.clock = pg.time.Clock()
        self.fractal = Fractal(self)

    def run(self):
        while True:
            self.screen.fill('black')
            self.fractal.run()
            pg.display.flip()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            self.clock.tick()
            pg.display.set_caption(f'FPS: {self.clock.get_fps() :.2f}')


if __name__ == '__main__':
    app = App()
    app.run()